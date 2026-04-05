📊 System Capacity & Care Load Analytics for Unaccompanied Children

📌 Overview

This project analyzes the operational flow of unaccompanied children within the CBP and HHS care system. The objective is to monitor system capacity, identify pressure points, and evaluate how efficiently children are processed from intake to discharge.

By transforming raw daily data into structured metrics and visual insights, the project provides a data-driven framework for understanding system behavior and supporting decision-making.

⸻

🎯 Objectives
	•	Quantify total system load across CBP and HHS
	•	Analyze inflow vs outflow dynamics
	•	Identify periods of system stress and backlog accumulation
	•	Evaluate system stability using key performance indicators (KPIs)
	•	Develop an interactive dashboard for monitoring
	•	Forecast future system load

⸻

🧠 System Understanding

The system operates as a pipeline:

CBP (Intake) → HHS (Care) → Discharge (Exit)

An imbalance between intake and discharge leads to increased system pressure, backlog formation, and potential capacity issues.

⸻

📂 Dataset

The dataset contains daily time-series records of:
	•	Children apprehended and placed in CBP custody
	•	Children currently in CBP custody
	•	Children transferred to HHS care
	•	Children in HHS care
	•	Children discharged from HHS care

⸻

⚙️ Methodology

Data Preparation
	•	Cleaned column names and data formats
	•	Converted date fields into datetime
	•	Handled missing and inconsistent values
	•	Structured dataset into a continuous time-series

Feature Engineering

Derived key metrics:
	•	Total Load = CBP Custody + HHS Care
	•	Net Intake = Transfers − Discharges
	•	Backlog = Rolling accumulation of net intake
	•	Growth Rate = Day-to-day percentage change

Exploratory Analysis
	•	Time-series trend analysis
	•	CBP vs HHS load comparison
	•	Identification of high-load periods

KPI Framework
	•	Total Children Under Care
	•	Net Intake Pressure
	•	Care Load Volatility
	•	Backlog Accumulation
	•	Discharge Efficiency Ratio

Forecasting
	•	Implemented time-series forecasting to estimate future load
	•	Used model-based predictions to support proactive planning

⸻

📊 Key Insights
	•	System load is strongly influenced by intake fluctuations
	•	Sustained positive net intake leads to backlog accumulation
	•	High-load periods indicate potential system stress
	•	Efficient discharge is critical for maintaining system balance

⸻

🖥️ Dashboard

An interactive dashboard was developed using Streamlit to visualize system performance.

Features:
	•	Real-time KPI monitoring
	•	Time-series visualization of system load
	•	CBP vs HHS comparison
	•	Net intake and backlog trends
	•	Alert system for high-pressure conditions

⸻

🚀 Getting Started


Installation
pip install pandas numpy matplotlib streamlit prophet

Run Analysis
python analysis.py

Launch Dashboard
streamlit run app.py

📁 Project Structure
UAC_System_Analytics/
│
├── data/
│   └── dataset.csv
├── notebooks/
│   └── analysis.ipynb

🏁 Conclusion

This project demonstrates how operational data can be transformed into actionable insights for system monitoring and capacity planning. It highlights the importance of balancing intake and discharge to ensure efficient and sustainable care delivery.

⸻

👤 Author

Afsar Azam
B.Tech Artificial Intelligence
Data Analysis | Machine Learning | Data science

⸻

📌 Note

This project was developed as part of an internship to explore real-world data challenges and apply analytical techniques to a healthcare-focused system.
:::
