from flask import Flask 
app = Flask(__name__)

@app.route("/info")
def lwinfo():
	return "Hello How are you"

@app.rout("/phone")
def lwphone():
	return"Hii, here is the number:- "

app.run(host="0.0.0.0")