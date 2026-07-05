from flask import Flask, render_template, request, send_from_directory
import joblib
import numpy as np

    
app = Flask(__name__)

# Load the trained model
model = joblib.load("loan_prediction_model.pkl")


@app.route('/')
def home():
    return render_template("index.html")



@app.route('/predict', methods=['POST'])
def predict():

    data = [
        float(request.form['ApplicantIncome']),
        float(request.form['CoapplicantIncome']),
        float(request.form['LoanAmount']),
        float(request.form['Loan_Amount_Term']),
        float(request.form['Credit_History']),
        float(request.form['Gender']),
        float(request.form['Married']),
        float(request.form['Dependents']),
        float(request.form['Education']),
        float(request.form['Self_Employed']),
        float(request.form['Property_Area'])
    ]
    
    print(data)
    prediction = model.predict([data])

    if prediction[0] == 1:
        result = "✅ Loan Approved"
    else:
        result = "❌ Loan Rejected"

    return render_template("index.html", prediction=result)


if __name__ == '__main__':
    app.run(debug=True)
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
