# 🧠 Disease Prediction System (ML-Powered)

This is a machine learning-powered web application that predicts the likelihood of a person being diseased based on biomedical indicators such as **Age**, **BMI**, **Glucose**, and **Resistin**. The system is built using **Flask** and a pre-trained **Random Forest Classifier**, and it supports bilingual (Greek & English) user interface and dark mode.

## 🚀 Features

- ✅ Simple and responsive user interface
- 🔁 Live prediction results with probability breakdown
- 🌐 Bilingual support (Greek / English toggle)
- 🌙 Dark mode for comfortable viewing
- 📊 Probability chart using Chart.js
- 📦 Docker-ready deployment

## 🧪 Input Features

- **Age** (years)
- **BMI** (Body Mass Index)
- **Glucose** level
- **Resistin** level

## 🧠 Model

The application uses a pre-trained **Random Forest** model (`Best_Random_Forest_Model.pkl`) built using `scikit-learn`. It outputs:
- Predicted class: `Healthy` or `Diseased`
- Probability (%) for each class
- A recommendation message based on confidence

## 📁 Project Structure

```
.
├── app.py                   # Flask backend logic
├── requirements.txt         # Python dependencies
├── Dockerfile               # Docker configuration
├── Best_Random_Forest_Model.pkl  # Trained ML model
├── templates/
│   └── index.html           # Frontend HTML page
└── static/
    └── favicon.ico          # Favicon for the app
```

## 🧰 Installation

### ⚙️ Local Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/disease-prediction-app.git
   cd disease-prediction-app
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the app:
   ```bash
   python app.py
   ```

5. Visit `http://localhost:5000` in your browser.

### 🐳 Docker Setup

1. Build the Docker image:
   ```bash
   docker build -t disease-predictor .
   ```

2. Run the container:
   ```bash
   docker run -p 5000:5000 disease-predictor
   ```

## 📜 License

This project is licensed under the GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007 License.

---

© 2025 DSS - ML Powered Health
