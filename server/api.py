from flask import Flask, abort, Response

import Motor

api = Flask(__name__)

motor = Motor()


@api.route('/forward', methods=['POST'])
def forward():
    # return abort(400, description="test")
    motor.forward()
    return Response(status=200, mimetype='application/json')


api.run()
