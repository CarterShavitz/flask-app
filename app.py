from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'This is Lab 4, I am enchancing the application to talk about the Lab'
