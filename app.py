# This pages is where any configuration, registration, and other setup the application needs will happen. 

from flask import Flask

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":
        ip_address = request.remote_addr
        entry_content = request.form.get("content")
        formatted_date = datetime.datetime.today().strftime("%Y-%m-%d/%H:%M")
        app.db.entries.insert({"content": entry_content, "date": formatted_date, "IP": ip_address})
        return "POST method called"

    return "GET method called"