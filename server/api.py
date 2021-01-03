from flask import Flask, abort, Response

from Motor import Motor

api = Flask(__name__)

motor = Motor()


@api.route('/forward', methods=['POST'])
def forward():
    # return abort(400, description="test")
    motor.forward()
    return Response(status=200, mimetype='application/json')


api.run(host="0.0.0.0")
