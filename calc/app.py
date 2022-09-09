# Put your app in here.
from flask import Flask, request
from operations import *

app = Flask(__name__)

@app.route('/add')
def add_route():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(add(a, b))

@app.route('/sub')
def sub_route():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(sub(a, b))

@app.route('/mult')
def mult_route():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(mult(a, b))

@app.route('/div')
def div_route():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(div(a, b))

OPERATORS = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}

@app.route('/math/<op>')
def do_math(op):
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(OPERATORS[op](a, b))
