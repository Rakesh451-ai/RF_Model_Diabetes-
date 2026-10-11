# 🩺 Diabetes Prediction Using Machine Learning

A machine learning web application built with **Python and Streamlit** that predicts diabetes status based on 10 medical input features. The application loads a trained machine learning model and provides a prediction through a simple, interactive interface.

## 🚀 Features

- Predict diabetes status using a pre-trained ML model.
- Accept 10 medical parameters as input.
- Interactive web interface built with Streamlit.
- Load the trained model using Joblib.
- Display prediction results with clear success and error messages.

## 🛠️ Tech Stack

- **Python** — Core programming language
- **Streamlit** — Web application interface
- **Joblib** — Loading the trained machine learning model
- **Scikit-learn** — Model inference compatibility, if the model was trained using Scikit-learn

## 📊 Input Features

The application accepts the following 10 features:

| No. | Feature |
|---:|---|
| 1 | Insulin Levels |
| 2 | OGTT |
| 3 | Creatinine Levels |
| 4 | Random Blood Glucose |
| 5 | LDL Cholesterol |
| 6 | Uric Acid Levels |
| 7 | ALT |
| 8 | AST |
| 9 | Fasting Blood Glucose |
| 10 | HbA1c |

## 📁 Project Structure

```text
Diabetes-Prediction/
├── app.py
├── Diabetes_Status.pkl
├── requirements.txt
└── README.md
```

- `app.py` — Streamlit application code.
- `Diabetes_Status.pkl` — Pre-trained machine learning model.
- `requirements.txt` — Required Python dependencies.
- `README.md` — Project documentation.

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Diabetes-Prediction.git
cd Diabetes-Prediction
```

Replace `YOUR_USERNAME` with your GitHub username and use your actual repository name.

### 2. Create a virtual environment (optional)

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

On Linux or macOS:

```bash
source venv/bin/activate
```

### 3. Install dependencies

Create a `requirements.txt` file containing:

```text
streamlit
joblib
scikit-learn
pandas
numpy
```

Install the packages:

```bash
pip install -r requirements.txt
```

The exact dependencies may vary depending on the library used to train and save the model.

### 4. Run the application

Ensure `Diabetes_Status.pkl` is in the same directory as `app.py`, then execute:

```bash
streamlit run app.py
```

Streamlit will provide a local URL where you can open the application in your browser.

## 🧠 How It Works

1. The application loads the trained model from `Diabetes_Status.pkl`.
2. The user enters values for the 10 medical features.
3. When the **Predict** button is clicked, the inputs are organized into a two-dimensional array.
4. The trained model processes the input using `model.predict()`.
5. The application displays the predicted class:
   - **Class 1:** Diabetes detected.
   - **Class 0:** No diabetes detected.

The model's expected feature order, units, preprocessing, and class labels must match those used during training.

## 🔮 Future Improvements

- Add model evaluation metrics such as accuracy, precision, recall, and F1-score.
- Display prediction probabilities if supported by the model.
- Improve input validation and provide medical reference ranges where appropriate.
- Add visualizations for selected input parameters.
- Deploy the application using Streamlit Community Cloud.
- Improve the interface with a more responsive and user-friendly design.

## ⚠️ Disclaimer

This application is an educational machine learning project and is **not intended for medical diagnosis or treatment decisions**. Predictions may be inaccurate and should not replace professional medical evaluation or laboratory testing. Consult a qualified healthcare professional for medical advice.

## 👨‍💻 Author

**Rakesh Yadav**

B.Tech Computer Science and Business Systems Student

- GitHub: [Rakesh451-ai](https://github.com/Rakesh451-ai)

---
