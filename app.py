# This pages is where any configuration, registration, and other setup the application needs will happen. 
from flask import Flask, render_template, request, flash
import secrets
# Creates a flask application object in the current python module
app = Flask(__name__)

# Generate a secure random secret key of 16 bytes
app.secret_key = secrets.token_hex(16)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", total_sum=None)

def get_letter_value(letter):
    vowel = 'aeiou'
    consonant = 'bjkqvxyz'
    remainder = 'cdfghlmnprstw'
    
    if letter.lower() in vowel:
        return 2
    elif letter.lower() in consonant:
        return 4
    elif letter.lower() in remainder:
        return 1
    else:
        if flash and request:
            flash('Please enter a word')
        return 0

@app.route('/', methods=['GET', 'POST'])
def calculate_letter_sum():
    if request.method == 'POST':
        text = request.form.get('text')
        total_sum = 0

        for letter in text:
            total_sum += get_letter_value(letter)
    
        return render_template('index.html', total_sum=total_sum)
    # Pass total_sum as None for the initial rendering
    return render_template('index.html', total_sum=None)
# <= 5: cat image, 6 to 15: dog image, 16 to 25: third image, 26 to 35: fourth image, 36+ fifth image
# Defined in html

if __name__ == "__main__":
    app.run()