from flask import Flask, render_template
import os
import result_budget, result_calorie


app = Flask(__name__)

@app.route("/")
def index():

    return render_template("layout.html")

@app.route('/budget.html')
def budget():
    result_menu, money, budget, calorie = result_budget.calculation()
    result_amount = money - budget
    sum_calorie = calorie
    return render_template('budget.html', result_menu=result_menu, result_amount=result_amount, sum_calorie = sum_calorie)

@app.route('/calorie.html')
def calorie():
    result_menu, limit_calorie, budget, calorie = result_calorie.calculation()
    r_calorie = limit_calorie - calorie
    sum_budget = budget
    return render_template('calorie.html', result_menu=result_menu, r_calorie=r_calorie, sum_budget = sum_budget)    

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)