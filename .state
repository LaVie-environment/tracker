#!/usr/bin/python

from flask import Flask, render_template
import math
app = Flask(__name__)

def cosecant(x):
    return 1/math.sin(x)

def cosecant_degrees(x):
    return 1/math.sin(x*math.pi/180)

@app.route('/')
def index():
    result_radians = cosecant(0.5)
    result_degrees = cosecant_degrees(30)
    return render_template('index.html', result_radians=result_radians, result_degrees=result_degrees)

if __name__ == '__main__':
    app.run(debug=True)

