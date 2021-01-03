from flask import Flask, abort, Response

from Motor import Motor

api = Flask(__name__)

motor = Motor()

OK_RESPONSE = Response(status=200, mimetype='application/json')


@api.route('/forward', methods=['POST'])
def forward():
    motor.forward()
    return OK_RESPONSE


@api.route('/back', methods=['POST'])
def back():
    motor.back()
    return OK_RESPONSE


@api.route('/left', methods=['POST'])
def left():
    motor.left()
    return OK_RESPONSE


@api.route('/right', methods=['POST'])
def right():
    motor.right()
    return OK_RESPONSE


api.run(host="0.0.0.0")
