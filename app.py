from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    for x in range(50):
        print(x)
    return 'Hello, World!'
