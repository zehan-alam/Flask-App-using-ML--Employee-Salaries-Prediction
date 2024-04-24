from salary_predict import app
from flask import render_template, request # type: ignore
import pickle
import pandas as pd
import os

current_dir = os.path.dirname(__file__)
model_path = os.path.join(current_dir, 'salary_predict.pkl')
with open(model_path, 'rb') as file:
    model = pickle.load(file)

@app.route('/', methods=['GET', 'POST'])
def home_page():
    predicted_salary = None
    department = ''
    division = ''
    grade = ''
    gender = ''
    overtime_pay = ''
    longevity_pay = ''
    
    if request.method == 'POST':
        # Extract input values from the form
        department = request.form['department']
        division = request.form['division']
        grade = request.form['grade']
        gender = request.form['gender']
        overtime_pay = float(request.form['overtime_pay'])
        longevity_pay = float(request.form['longevity_pay'])

        # Perform prediction using the model
        input_data = pd.DataFrame({
            'Department': [department],
            'Division': [division],
            'Grade': [grade],
            'Gender': [gender],
            'Overtime_Pay': [overtime_pay],
            'Longevity_Pay': [longevity_pay]
        })
        predicted_salary = model.predict(input_data)[0]

    return render_template('home.html', predicted_salary=predicted_salary,
                           department=department,
                           division=division,
                           grade=grade,
                           gender=gender,
                           overtime_pay=overtime_pay,
                           longevity_pay=longevity_pay)