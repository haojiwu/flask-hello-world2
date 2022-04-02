from flask import Flask
app = Flask(__name__)
exit()
@app.route('/')
def hello_world():
    return 'Hello, World!'
