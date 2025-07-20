from flask import Flask, flash, render_template, request
from flask_sqlalchemy import SQLAlchemy


subjects = []
passwords = []
app = Flask(__name__)
app.secret_key = "password-app-key"


@app.route("/", methods=["GET", "POST"])
def home():
    display = "none"
    if request.method == "POST":
        display = "block"
        subject = request.form.get("subject-input")
        password = request.form.get("password-input")
        if subject and password:
            subjects.append(subject)
            passwords.append(password)
        else:
            display = "none" if len(passwords) == 0 else "block"
    return render_template("home.html", display_type=display, subjects=subjects, passwords=passwords)


if __name__ == '__main__':
    app.run(debug=True)
