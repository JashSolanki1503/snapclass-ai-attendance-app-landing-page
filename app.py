from flask import Flask, render_template

# initialize the flask application 
app = Flask(__name__)

# define one route 
@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug = True)