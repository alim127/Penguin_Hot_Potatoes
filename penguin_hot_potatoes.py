from flask import Flask
from flask.templating import render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("penguinhotpotatoes.html")

@app.route("/rawr")
def rawr():
    return "rawr"

if __name__ == "__main__":
    app.run(debug=True)