#Angelo Facciponti-Mennella
#Ezechiel
#Snigdha Kalathur
# BostonHacks 2019
# 11/16/2019

from flask import Flask, Response, request, jsonify, render_template, make_response, flash, url_for, redirect
import time

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("welcome.html")

@app.route("/home")
def home():
    return render_template("home.html")





if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True)