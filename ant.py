from flask import Flask
from flask import render_template
import RPi.GPIO as rpi
import time
import datetime

app= Flask(__name__)

k1,k2,k3,k4,k5,k6,k7,k8= 3,5,7,11,13,15,19,21

rpi.setwarnings(False)
rpi.setmode(rpi.BOARD)
rpi.setup(k1, rpi.OUT)
rpi.setup(k2, rpi.OUT)
rpi.setup(k3, rpi.OUT)
rpi.setup(k4, rpi.OUT)
rpi.setup(k5, rpi.OUT)
rpi.setup(k6, rpi.OUT)
rpi.setup(k7, rpi.OUT)
rpi.setup(k8, rpi.OUT)
rpi.output(k1, 1)
rpi.output(k2, 1)
rpi.output(k3, 1)
rpi.output(k4, 1)
rpi.output(k5, 1)
rpi.output(k6, 1)
rpi.output(k7, 1)
rpi.output(k8, 1)

print("Done")

## all relays in parking mode which means antenna 1 connected to SDR1 and antenna 2 to SDR2
@app.route('/')
def parking():
    rpi.output(k1, 1)
    rpi.output(k2, 1)
    rpi.output(k3, 1)
    rpi.output(k4, 1)
    rpi.output(k5, 1)
    rpi.output(k6, 1)
    rpi.output(k7, 1)
    rpi.output(k8, 1)
    return render_template('main.html', parking='<img src="static/parking64.png" style="vertical-align: middle">')

## antennas connected to transceivers according to scheme 1
@app.route('/1')
def scheme_1():
    rpi.output(k1, 1)
    rpi.output(k2, 0)
    rpi.output(k3, 1)
    rpi.output(k4, 1)
    rpi.output(k5, 0)
    rpi.output(k6, 1)
    rpi.output(k7, 0)
    rpi.output(k8, 1)
    return render_template('main.html', active_1='<img src="static/antenna64.png" style="vertical-align: middle">')

## antennas connected to transceivers according to scheme 2
@app.route('/2')
def scheme_2():
    rpi.output(k1, 0)
    rpi.output(k2, 1)
    rpi.output(k3, 1)
    rpi.output(k4, 0)
    rpi.output(k5, 1)
    rpi.output(k6, 0)
    rpi.output(k7, 1)
    rpi.output(k8, 0)
    return render_template('main.html', active_2='<img src="static/antenna64.png" style="vertical-align: middle">')

## antennas connected to transceivers according to scheme 3
@app.route('/3')
def scheme_3():
    rpi.output(k1, 0)
    rpi.output(k2, 1)
    rpi.output(k3, 1)
    rpi.output(k4, 1)
    rpi.output(k5, 1)
    rpi.output(k6, 0)
    rpi.output(k7, 1)
    rpi.output(k8, 1)
    return render_template('main.html', active_3='<img src="static/antenna64.png" style="vertical-align: middle">')

## antennas connected to transceivers according to scheme 4
@app.route('/4')
def scheme_4():
    rpi.output(k1, 0)
    rpi.output(k2, 1)
    rpi.output(k3, 0)
    rpi.output(k4, 0)
    rpi.output(k5, 1)
    rpi.output(k6, 1)
    rpi.output(k7, 1)
    rpi.output(k8, 0)
    return render_template('main.html', active_4='<img src="static/antenna64.png" style="vertical-align: middle">')

## antennas connected to transceivers according to scheme 5
@app.route('/5')
def scheme_5():
    rpi.output(k1, 0)
    rpi.output(k2, 0)
    rpi.output(k3, 0)
    rpi.output(k4, 0)
    rpi.output(k5, 0)
    rpi.output(k6, 0)
    rpi.output(k7, 0)
    rpi.output(k8, 0)
    return render_template('main.html', active_5='<img src="static/antenna64.png" style="vertical-align: middle">')


if __name__=="__main__":
    print("Start")
    app.run(debug=True, host='0.0.0.0', port=5000)
