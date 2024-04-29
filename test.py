from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return '<p>Hello, World!<p>'



from markupsafe import escape

@app.route("/name")
def hello(name):
    return f"hello,{escape(name)}!"





