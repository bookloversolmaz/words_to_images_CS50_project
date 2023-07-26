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
    # Code here assigns values to users input and outputs an image depending on those values
    # a, e, i, o, u = 2 points
    # b, j, k, q, v, x, y, z = 4 points
    # c, d, f, g, h, l, m, n, p, r, s, t, w = 1 point
    # <= 5: cat image, 6 to 15: dog image, 16 to 25: third image, 26 to 35: fourth image, 36+ fifth image
        return render_template("images.html")
    else:
        return render_template("home.html")


if __name__ == "__main__":
    app.run()