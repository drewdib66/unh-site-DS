from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def home():
    personName = "Drew"
    itemList = ('cats','dogs','fish')
    return render_template('base.html' , person=personName,list=itemList) 

@app.route("/admin")
def admin():
    return render_template("base.html")
