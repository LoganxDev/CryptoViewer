import os
from flask import Flask, jsonify

# instantiate the app
app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')