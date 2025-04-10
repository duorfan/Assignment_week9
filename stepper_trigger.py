from flask import Flask, request
from adafruit_crickit import crickit
from adafruit_motor import stepper
import time

app = Flask(__name__)

STEP_MOTOR = crickit.stepper_motor
INTERSTEP_DELAY = 0.01

@app.route("/trigger", methods=["POST"])
def move_motor():
    data = request.get_json()
    if data and data.get("move"):
        print("Trigger received: moving motor")
        for i in range(50):
            STEP_MOTOR.onestep(direction=stepper.FORWARD)
            time.sleep(INTERSTEP_DELAY)
        for i in range(50):
            STEP_MOTOR.onestep(direction=stepper.BACKWARD)
            time.sleep(INTERSTEP_DELAY)
        return "Motor moved."
    return "No action taken."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
