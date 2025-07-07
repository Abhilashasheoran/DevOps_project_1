from flask import Flask 
app = Flask(__name__)

@app.route("/info")
def lwinfo():
	return "Hello How are you"

@app.route("/phone")
def lwphone():
    return "9306340864"

if __name__ == '__main__':
	app.run(host="0.0.0.0")