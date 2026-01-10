from flask import Flask, request, render_template
import pandas as pd
import os
import math
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')

    try:
       
        data = CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('reading_score')),
            writing_score=float(request.form.get('writing_score')),
        )

        pred_df = data.get_data_as_data_frame()
        print("Input DataFrame:\n", pred_df)

       
        if not os.path.exists('artifacts/model.pkl') or not os.path.exists('artifacts/preprocessor.pkl'):
            raise FileNotFoundError("Model or preprocessor not found in artifacts folder.")

       
        # Prediction
       
        predict_pipeline = PredictPipeline()
        predicted_math_score = float(predict_pipeline.predict(pred_df)[0])
        print("Predicted Math Score:", predicted_math_score)


        # SIGMOID RISK CALCULATION
        
        midpoint = 50     
        steepness = 10    

        risk_percentage = round(
            100 / (1 + math.exp((predicted_math_score - midpoint) / steepness)),
            2
        )

        
        if risk_percentage <= 30:
            academic_risk = "Low Risk"
        elif risk_percentage <= 60:
            academic_risk = "Medium Risk"
        else:
            academic_risk = "High Risk"

        
        warnings = []

        if predicted_math_score < 40:
            warnings.append("🚨 Critical Maths Risk")

        if float(request.form.get('writing_score')) < 50:
            warnings.append("⚠ Writing Skills Weak")

        if float(request.form.get('reading_score')) < 50:
            warnings.append("⚠ Reading Skills Weak")

        if not warnings:
            warnings.append("✅ No Immediate Academic Risks")

        
        return render_template(
            'home.html',
            results=round(predicted_math_score, 2),
            academic_risk=academic_risk,
            risk_percentage=risk_percentage,
            warnings=warnings
        )

    except Exception as e:
        return render_template('home.html', results="Error: " + str(e))


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, threaded=False)  #http://127.0.0.1:5000/
