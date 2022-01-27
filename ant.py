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

@app.route('/A1_K2_A2_mcHF')
def A1_K2_A2_mcHF():
    rpi.output(k1, 1)
    rpi.output(k2, 0)
    rpi.output(k3, 1)
    rpi.output(k4, 1)
    rpi.output(k5, 0)
    rpi.output(k6, 1)
    rpi.output(k7, 0)
    rpi.output(k8, 1)
    return render_template('mainx.html')

@app.route('/A1_mcHF_A2_K2')
def A1_mcHF_A2_K2():
    rpi.output(k1, 0)
    rpi.output(k2, 1)
    rpi.output(k3, 1)
    rpi.output(k4, 0)
    rpi.output(k5, 1)
    rpi.output(k6, 0)
    rpi.output(k7, 1)
    rpi.output(k8, 0)
    return render_template('mainx.html', utc_dt=datetime.datetime.utcnow())

if __name__=="__main__":
    print("Start")
    app.run(debug=True, host='192.168.1.39')


