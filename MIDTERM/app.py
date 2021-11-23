from flask import Flask 
from flask import request
from flask import render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/Registration")
def Registration_Form():
    return render_template("registration.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1",port=5000)