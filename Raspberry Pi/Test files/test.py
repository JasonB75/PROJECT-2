from flask import Flask, request
import json


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/get_data/')
def get_data():
    volume = request.args.get('bit_request')
    print(requested_bits)
    x = [1,0,1,0,1,0,1,0,1]
    output = {'output': x}
    return json.dumps(output)