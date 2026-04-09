Project Title: Demand Forecasting and Battery Scheduling Optimization Using Machine Learning: A Decision Support Tool
Purpose of This Folder
This folder contains the supporting documents and technical files used in the capstone project. These files are included as backup material and to show the full workflow behind the final report, including data preparation, forecasting, optimization, dashboard development, and application development.
Main File for Review
Please review the final report first, as it explains the project objectives, methodology, results, discussion, and conclusions in a complete and reader-friendly format.
Description of Supporting Files
1.	streamlit app
The decision-making support application developed within Streamlit is located within this folder and includes the Python application code that was created to represent and present forecasting and battery scheduling results in a manner that allows for easy interaction with the information provided by these results.
 To run the Streamlit application, open the folder located in either a Jupyter-compatible environment or a Visual Studio Code environment, install any required Python libraries that have not already been installed, and use the Streamlit command to run the streamlit_app.py file located within this same folder. In this folder, you will find the Python coding files for executing this application.
2.	capstone_eda.ipynb
The notebook, capstone_eda. ipynb, contains the exploratory analysis of the dataset. This exploratory analysis was used to understand the structure of the dataset, examine electricity demand and price patterns, identify and analyze trends within the dataset, as well as check for the quality of the dataset prior to the model being created.
3.	capstone_forecasting.csv
This CSV file contains the forecasting data or outputs generated during the forecasting effort in this project. This CSV file will serve as a supporting document for the generation of forecasts and may contain values used for reporting, comparison and/or preparing for analysis.
4.	capstone_forecasting.ipynb
This Jupyter notebook contains the forecasting model development process. It was used to train and evaluate the machine learning model for short-term electricity demand prediction. It also includes model performance checks and forecasting results.
This is a Python coding file used for forecasting work.
5.	capstone_optimization.ipynb
This notebook contains the work done to optimize the scheduling of battery usage for the project through its analysis. The results of these analyses can help determine how a 500-kWh battery can be most cost-effectively charged/discharged based on current conditions of demand and price for the electricity supplied to it. This notebook is written in Python for use in optimization analysis.
6.	Dashboard.pbix
This Power BI dashboard file was developed for the project. This file presents the output, trends, and summary results from the project visually so that non-technical readers can better understand the results. To access: Access the .pbix file using Microsoft Power BI Desktop. If you are prompted to refresh your data in the dashboard you should use the CSV files provided in this folder.
7.	data_cleaning.ipynb
This notebook documents the steps taken to clean the data and pre-process it for the project’s analysis. Specifically, this notebook details the actions taken to prepare the raw data for future analysis by organizing the raw data, addressing any missing values, and preparing the dataset for future analysis. This notebook is written in Python for use in the preparation of the data.
8.	energy_clean.csv
This file is the cleaned dataset produced after the preprocessing stage. It contains the prepared data used as the base for further feature engineering and analysis.
9.	energy_features.csv
This file contains the cleaned dataset together with additional variables created during feature engineering. These added variables help the forecasting model capture useful historical and time-based patterns.
10.	feature_engineering.ipynb
The notebook will demonstrate feature engineering used in this project and how we created new features, or predictor variables from existing data, to improve the performance of our model. This is a Python file used to generate features.
11.	powerbi_dataset.csv
This CSV file has been created to be the input to the Power BI dashboard. It contains all of the data needed to create dashboard visualizations as well as summary output for reporting and interpretation.
12.	predictions_histgb.csv
This file contains the predicted outputs of our model that were generated because of forecasting. This file allows users to interpret results by showing the predicted value(s) they generated versus the actual value(s).
13.	Python Coding Files Included in This Folder
The following files are Python-based project working files and were used to perform the technical analysis:
•	capstone_eda.ipynb
•	capstone_forecasting.ipynb
•	capstone_optimization.ipynb
•	data_cleaning.ipynb
•	feature_engineering.ipynb
•	files inside the streamlit app folder
Suggested Review Order
1.	Final Report
2.	Dashboard.pbix
3.	streamlit app
4.	 notebooks
5.	CSV supporting files
Note
These supporting files are submitted to provide full project backup and documentation of the analytical workflow used in the capstone project.
