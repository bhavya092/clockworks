
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("./index.html", title="HOME PAGE")


@app.route("/about")
def about():
    return render_template("about.html", title="about page")

if __name__ == "__main__":
    app.run(debug=True)
