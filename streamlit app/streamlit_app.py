import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpBinary, value 

st.set_page_config(page_title="Demand Forecasting and Battery Scheduling App", layout="wide")

st.title("Demand Forecasting and Battery Scheduling App")

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go to",
    ["Forecast Overview", "Optimization Planner", "Scenario Comparison"]
)
def run_battery_optimization(data, battery_capacity, max_charge_power, max_discharge_power,
                             charge_efficiency, discharge_efficiency, initial_soc):
    model = LpProblem("Battery_Scheduling", LpMinimize)

    charge = LpVariable.dicts("charge", range(len(data)), lowBound=0, upBound=max_charge_power)
    discharge = LpVariable.dicts("discharge", range(len(data)), lowBound=0, upBound=max_discharge_power)
    soc = LpVariable.dicts("soc", range(len(data)), lowBound=0, upBound=battery_capacity)
    is_charging = LpVariable.dicts("is_charging", range(len(data)), cat=LpBinary)

    model += lpSum([
        (data.loc[t, "forecast_load"] + charge[t] - discharge[t]) * data.loc[t, "price"]
        for t in range(len(data))
    ])

    model += soc[0] == initial_soc

    for t in range(1, len(data)):
        model += soc[t] == soc[t-1] + charge[t] * charge_efficiency - discharge[t] / discharge_efficiency

    model += soc[len(data)-1] == initial_soc

    for t in range(len(data)):
        model += charge[t] <= max_charge_power * is_charging[t]
        model += discharge[t] <= max_discharge_power * (1 - is_charging[t])
        model += discharge[t] <= data.loc[t, "forecast_load"]

    model.solve()

    result = data.copy()
    result["opt_charge"] = [charge[t].varValue for t in range(len(data))]
    result["opt_discharge"] = [discharge[t].varValue for t in range(len(data))]
    result["opt_soc"] = [soc[t].varValue for t in range(len(data))]
    result["opt_net_load"] = result["forecast_load"] + result["opt_charge"] - result["opt_discharge"]
    result["opt_cost"] = result["opt_net_load"] * result["price"]

    total_cost = result["opt_cost"].sum()

    return result, total_cost
opt_input_df = pd.read_csv("optimization_input_day.csv")
opt_input_df["time"] = pd.to_datetime(opt_input_df["time"])
if page == "Forecast Overview":
    st.header("Forecast Overview")

    col1, col2, col3 = st.columns(3)

    col1.metric("MAE", "376.09")
    col2.metric("RMSE", "571.42")
    col3.metric("MAPE", "1.31%")
    st.write("HistGradientBossting was the best forecasting model.")
    st.image("actual_vs_predicted.png", caption="Actual vs Predicted Load")

if page == "Optimization Planner":
    st.header("Optimization Planner")

    battery_capacity = st.number_input("Battery capacity (kWh)", min_value=100, max_value=2000, value=500, step=100)
    max_charge_power = st.number_input("Max charge power (kW)", min_value=50, max_value=500, value=100, step=50)
    max_discharge_power = st.number_input("Max discharge power (kW)", min_value=50, max_value=500, value=100, step=50)
    initial_soc = st.number_input("Initial state of charge (kWh)", min_value=0, max_value=int(battery_capacity), value=min(250, int(battery_capacity)), step=50)
    charge_efficiency = st.slider("Charge efficiency", min_value=0.80, max_value=1.00, value=0.95, step=0.01)
    discharge_efficiency = st.slider("Discharge efficiency", min_value=0.80, max_value=1.00, value=0.95, step=0.01)

    baseline_cost = (opt_input_df["forecast_load"] * opt_input_df["price"]).sum()

    result_df, optimized_cost = run_battery_optimization(
        opt_input_df,
        battery_capacity,
        max_charge_power,
        max_discharge_power,
        charge_efficiency,
        discharge_efficiency,
        initial_soc
    )

    Savings = baseline_cost - optimized_cost

    col1, col2, col3 = st.columns(3)
    col1.metric("Baseline Cost", f"{baseline_cost:,.2f}")
    col2.metric("Optimized Cost", f"{optimized_cost:,.2f}")
    col3.metric("Savings", f"{Savings:,.2f}")

    if Savings > 0:
        st.success("Optimization reduced cost relative to the baseline.")
    else:
        st.warning("Optimization did not reduce cost relative to the baseline.")

    fig1, ax1 = plt.subplots(figsize=(10, 4))
    ax1.plot(result_df["time"], result_df["opt_charge"], label="Charge")
    ax1.plot(result_df["time"], result_df["opt_discharge"], label="Discharge")
    ax1.set_title("Battery Charge and Discharge Schedule")
    ax1.set_xlabel("Time")
    ax1.set_ylabel("Energy (kWh)")
    ax1.legend()
    st.pyplot(fig1)

    fig2, ax2 = plt.subplots(figsize=(10, 4))
    ax2.plot(result_df["time"], result_df["opt_soc"])
    ax2.set_title("Battery State of Charge")
    ax2.set_xlabel("Time")
    ax2.set_ylabel("SOC (kWh)")
    st.pyplot(fig2)

if page == "Scenario Comparison":
    st.header("Scenario Comparison")

    col1, col2, col3 = st.columns(3)

    col1.metric("500 kWh Savings", "9.31K")
    col2.metric("1000 kWh Savings", "11.51K")
    col3.metric("1000 kWh, 200 kW Savings", "18.61K")

    st.write("Savings increased as battery capacity and charge/discharge power increased. The 1000 kWh battery with 200 kW charge/discharge power produced the highest savings among the tested scenarios.")

    st.image("scenario_comparison.png", caption="Savings by Battery Scenario")