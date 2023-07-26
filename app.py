# This pages is where any configuration, registration, and other setup the application needs will happen. 
from flask import Flask, render_template, request, flash
# Creates a flask application object in the current python module
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")

# @app.route("/images", methods=["GET", "POST"])
# def images():
#     if request.method == "POST":
#         return render_template("images.html", text=text)
#     else:
#         return render_template("home.html")

def get_letter_value(letter):
    vowel = 'aeiou'
    consonant = 'bjkqvxz'
    remainder = 'cdfghlmnprstw'
    
    if letter.lower() in vowel:
        return 2
    elif letter.lower() in consonant:
        return 4
    elif letter.lower() in remainder:
        return 1
    else:
        flash("Please enter text only")

@app.route('/', methods=['GET', 'POST'])
def calculate_letter_sum():
    if request.method == 'POST':
        text = request.form.get('text')
        total_sum = 0

        for letter in text:
            total_sum += get_letter_value(letter)

        total_sum
    
    return render_template('index.html')
    # <= 5: cat image, 6 to 15: dog image, 16 to 25: third image, 26 to 35: fourth image, 36+ fifth image


if __name__ == "__main__":
    app.run()