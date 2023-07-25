# This pages is where any configuration, registration, and other setup the application needs will happen. 
from flask import Flask, render_template, request
# Creates a flask application object in the current python module
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")

@app.route("/images", methods=["GET", "POST"])
def images():
    if request.method == "POST":
    # Code below starts the development server
        return render_template("images.html")
    else:
        return render_template("home.html")



if __name__ == "__main__":
    app.run()