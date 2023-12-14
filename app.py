from flask import Flask
from flask import request

app = Flask(__name__)
@app.route('/')
def hello_world():
    for x in range(110):
        print(x)
    return 'Hello, World!'
@app.route("/async-test", methods=['PUT'])
def result():
    print('------->' + str(request.headers) + '<------------')
    print('------->' + str(request.data) + '<------------')
    print('------->' + str(request.form) + '<------------')
    return 'OK'
