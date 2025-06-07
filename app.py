
from flask import Flask, request, render_template, session, redirect, url_for
import joblib
import numpy as np
import csv
from io import StringIO

app = Flask(__name__)
app.secret_key = 'supersecretkey'
model = joblib.load("Best_Random_Forest_Model.pkl")

def get_user_history_key():
    username = request.cookies.get("username") or session.get("user", "default")
    session["user"] = username 
    return f"history_{username}"


@app.before_request
def clear_history_on_refresh():
    if request.endpoint == 'home' and request.method == 'GET':
        session.pop(get_user_history_key(), None)

@app.route("/")
def home():
    return render_template("index.html", form_values={}, history=[])

@app.route("/predict", methods=["POST"])
def predict():
    try:
        age = float(request.form["age"])
        bmi = float(request.form["bmi"])
        glucose = float(request.form["glucose"])
        resistin = float(request.form["resistin"])

        features = np.array([[age, bmi, glucose, resistin]])
        prediction = model.predict(features)[0]
        proba = model.predict_proba(features)[0]
        prob_no = proba[0]
        prob_yes = proba[1]

        result = "Νοσεί" if prediction == 1 else "Υγιής"
        message = (
            "⚠ Υψηλή πιθανότητα. Συνιστάται ιατρικός έλεγχος."
            if prob_yes > 0.7 else
            "🔍 Μέτρια πιθανότητα. Παρακολούθηση συνιστάται."
            if prob_yes > 0.4 else
            "✅ Χαμηλή πιθανότητα. Ενδείξεις υγείας."
        )

        entry = {
            "age": age,
            "bmi": bmi,
            "glucose": glucose,
            "resistin": resistin,
            "result": result,
            "prob_yes": round(prob_yes * 100, 2),
            "prob_no": round(prob_no * 100, 2),
            "message": message
        }

        key = get_user_history_key()
        if key not in session:
            session[key] = []
        session[key].append(entry)
        session.modified = True

        return render_template(
            "index.html",
            prediction_text=f"Αποτέλεσμα: {result} (πιθανότητα: {prob_yes:.2%})",
            prob_no=round(prob_no * 100, 2),
            prob_yes=round(prob_yes * 100, 2),
            eval_message=message,
            form_values=request.form,
            history=session[key]
        )

    except Exception as e:
        return render_template(
            "index.html",
            prediction_text=f"⚠ Σφάλμα: {str(e)}",
            form_values=request.form,
            history=session.get(get_user_history_key(), [])
        )

@app.route("/clear")
def clear_history():
    session.pop(get_user_history_key(), None)
    return redirect(url_for("home"))

@app.route("/export")
def export_history():
    key = get_user_history_key()
    history = session.get(key, [])

    if not history:
        return "No history to export.", 400

    from io import StringIO
    import csv

    csv_buffer = StringIO()
    writer = csv.DictWriter(csv_buffer, fieldnames=["age", "bmi", "glucose", "resistin", "result", "prob_yes", "prob_no", "message"])
    writer.writeheader()
    for row in history:
        writer.writerow(row)

    csv_data = csv_buffer.getvalue().encode("utf-8-sig")

    return (
        csv_data,
        200,
        {
            "Content-Type": "text/csv; charset=utf-8",
            "Content-Disposition": "attachment; filename=history.csv"
        }
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
