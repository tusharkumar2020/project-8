from flask import Flask, render_template, request
from Math.mathematics import addition, subtraction, multiply

app = Flask("Mathematics Problem Solver")

@app.route("/sum")
def sum_route():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    result = addition(num1, num2)
    return str(result)

@app.route("/sub")
def sub_route():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    result = subtraction(num1, num2)
    return str(result)

@app.route("/mul")
def mul_route():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    result = multiply(num1, num2)
    return str(result)

@app.route("/")
def render_index_page():
    return render_template("index.html")
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
