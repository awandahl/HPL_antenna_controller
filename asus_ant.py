from flask import Flask
from flask import render_template
import ASUS.GPIO as GPIO
import time
import datetime

app= Flask(__name__)

k1,k2,k3,k4,k5,k6,k7,k8= 3,5,12,19,22,23,24,32


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(k1, GPIO.OUT)
GPIO.setup(k2, GPIO.OUT)
GPIO.setup(k3, GPIO.OUT)
GPIO.setup(k4, GPIO.OUT)
GPIO.setup(k5, GPIO.OUT)
GPIO.setup(k6, GPIO.OUT)
GPIO.setup(k7, GPIO.OUT)
GPIO.setup(k8, GPIO.OUT)
GPIO.output(k1, 1)
GPIO.output(k2, 1)
GPIO.output(k3, 1)
GPIO.output(k4, 1)
GPIO.output(k5, 1)
GPIO.output(k6, 1)
GPIO.output(k7, 1)
GPIO.output(k8, 1)

print("Done")

## all relays in parking mode which means antenna 1 connected to SDR1 and antenna 2 to SDR2
@app.route('/')
def parking():
    GPIO.output(k1, 1)
    GPIO.output(k2, 1)
    GPIO.output(k3, 1)
    GPIO.output(k4, 1)
    GPIO.output(k5, 1)
    GPIO.output(k6, 1)
    GPIO.output(k7, 1)
    GPIO.output(k8, 1)
    return render_template('main.html', parking='<img src="static/parking64.png" style="vertical-align: middle">')

## antennas connected to transceivers according to scheme 1
@app.route('/1')
def scheme_1():
    GPIO.output(k1, 1)
    GPIO.output(k2, 0)
    GPIO.output(k3, 1)
    GPIO.output(k4, 1)
    GPIO.output(k5, 0)
    GPIO.output(k6, 1)
    GPIO.output(k7, 0)
    GPIO.output(k8, 1)
    return render_template('main.html', active_1='<img src="static/antenna64.png" style="vertical-align: middle">')

## antennas connected to transceivers according to scheme 2
@app.route('/2')
def scheme_2():
    GPIO.output(k1, 0)
    GPIO.output(k2, 1)
    GPIO.output(k3, 1)
    GPIO.output(k4, 0)
    GPIO.output(k5, 1)
    GPIO.output(k6, 0)
    GPIO.output(k7, 1)
    GPIO.output(k8, 0)
    return render_template('main.html', active_2='<img src="static/antenna64.png" style="vertical-align: middle">')

## antennas connected to transceivers according to scheme 3
@app.route('/3')
def scheme_3():
    GPIO.output(k1, 0)
    GPIO.output(k2, 1)
    GPIO.output(k3, 1)
    GPIO.output(k4, 1)
    GPIO.output(k5, 1)
    GPIO.output(k6, 0)
    GPIO.output(k7, 1)
    GPIO.output(k8, 1)
    return render_template('main.html', active_3='<img src="static/antenna64.png" style="vertical-align: middle">')

## antennas connected to transceivers according to scheme 4
@app.route('/4')
def scheme_4():
    GPIO.output(k1, 0)
    GPIO.output(k2, 1)
    GPIO.output(k3, 0)
    GPIO.output(k4, 0)
    GPIO.output(k5, 1)
    GPIO.output(k6, 1)
    GPIO.output(k7, 1)
    GPIO.output(k8, 0)
    return render_template('main.html', active_4='<img src="static/antenna64.png" style="vertical-align: middle">')

## antennas connected to transceivers according to scheme 5
@app.route('/5')
def scheme_5():
    GPIO.output(k1, 0)
    GPIO.output(k2, 0)
    GPIO.output(k3, 0)
    GPIO.output(k4, 0)
    GPIO.output(k5, 0)
    GPIO.output(k6, 0)
    GPIO.output(k7, 0)
    GPIO.output(k8, 0)
    return render_template('main.html', active_5='<img src="static/antenna64.png" style="vertical-align: middle">')


if __name__=="__main__":
    print("Start")
    app.run(debug=True, host='0.0.0.0', port=5000)
