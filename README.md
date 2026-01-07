# ⚡ PowerPulse: Household Energy Usage Forecast

PowerPulse is a machine learning–based application that predicts **household electricity consumption (kW)** using historical energy usage patterns. The project leverages time-based features and regression modeling to provide accurate short-term energy forecasts through an interactive **Streamlit web interface**.

---

## 📌 Problem Statement

Accurate energy consumption forecasting is essential for:

* Household energy management
* Reducing electricity bills
* Load planning for energy providers
* Promoting energy-efficient behavior

This project aims to build a **predictive regression model** that estimates household energy usage based on historical data, time features, and optional weather information.

---

## 🏠 Dataset

**Dataset Name:** Individual Household Electric Power Consumption
**Source:** UCI Machine Learning Repository

🔗 Download link:
[https://archive.ics.uci.edu/dataset/235/individual+household+electric+power+consumption](https://archive.ics.uci.edu/dataset/235/individual+household+electric+power+consumption)

📍 **Location:**
Household located in **Sceaux, France (≈7 km from Paris)**

📁 **Note:**
The dataset is **not included** in this repository due to GitHub file size limits.

After downloading, place the file as:

```
data/household_power_consumption.txt
```
---

## 🔗 **Live Streamlit App:**  
👉 [streamlit household energy usage forecast Link.](https://household-energy-usage-forecast.streamlit.app/)

---

## 🛠️ Project Approach

### 1. Data Understanding & EDA

* Loaded raw household power consumption data
* Analyzed trends, seasonality, and missing values
* Studied correlations between energy usage and time features

### 2. Data Preprocessing

* Parsed `Date` and `Time` into datetime format
* Handled missing values
* Resampled data where required
* Normalized and cleaned numerical features

### 3. Feature Engineering

Key features used:

* `hour`
* `dayofweek`
* `month`
* `rolling_mean_24h` (last 24 hours energy usage)
* `avg_temperature` (optional, if available)

### 4. Model Training

Trained multiple regression models and selected the best-performing one:

* Linear Regression
* Random Forest Regressor
* **Gradient Boosting Regressor** ✅ (final model)

### 5. Model Evaluation

Evaluation metrics:

* RMSE (Root Mean Squared Error)
* MAE (Mean Absolute Error)
* R² Score

---

## 🤖 Final Model

* **Model Used:** Gradient Boosting Regressor
* **Reason:** Best trade-off between accuracy and generalization
* **Saved Artifacts:**

  * `gradient_boosting_energy_model.pkl`
  * `feature_cols.pkl`

---

## 🖥️ Streamlit Web Application

The project includes an interactive **Streamlit UI** that allows users to:

* Select a **date**
* Choose **hour of the day (0–23)**
* Optionally adjust **average temperature**
* Predict household energy consumption in **kilowatts (kW)**

### 🔮 Example Output

```
Predicted Energy Consumption: 1.41 kW
```

The prediction is based on historical household energy patterns from Sceaux, France.

---

## 🚀 How to Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/sakthignanaprakasamv/Household-Energy-Usage-Forecast.git
cd Household-Energy-Usage-Forecast
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Streamlit app

```bash
streamlit run app.py
```

---

## 📁 Repository Structure

```
Household-Energy-Usage-Forecast/
│
├── app.py                          # Streamlit application
├── PowerPulse_Household_Energy_Forecast.ipynb  # EDA & model notebook
├── gradient_boosting_energy_model.pkl
├── feature_cols.pkl
├── data/
│   └── household_power_consumption.txt  (not included)
├── README.md
├── .gitignore
└── .gitattributes
```

---

## 📊 Business Use Cases

* Household energy monitoring
* Demand forecasting
* Peak hour identification
* Smart grid analytics
* Energy conservation and sustainability

---

## 📈 Skills & Tools Used

* Python
* Pandas, NumPy
* Scikit-learn
* Matplotlib / Seaborn
* Streamlit
* Feature Engineering
* Regression Modeling
* Model Evaluation
* Git & GitHub

---

## 🧾 Project Status

✅ Data preprocessing completed
✅ Feature engineering implemented
✅ Model trained and evaluated
✅ Streamlit app deployed locally
✅ GitHub repository finalized

---

## 👤 Author

**Sakthi Gnana Prakasam V**
Domain: Energy Analytics & Machine Learning


