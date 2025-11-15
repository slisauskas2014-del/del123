from flask import Flask, render_template, request, redirect, url_for, flash
import logging

app = Flask(__name__)
app.secret_key = "change_me_to_a_random_string"

# Optional: make sure logger level is INFO (so info() logs appear)
app.logger.setLevel(logging.INFO)


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()

        # ⚠️ Don't log raw passwords in real apps!
        app.logger.info(
            "Login attempt: username=%s, password_length=%d, ip=%s",
            username,
            len(password),
            request.remote_addr
        )

        if username and password:
            flash(f"Welcome, {username}!", "success")
            return redirect(url_for("dashboard"))
        else:
            flash("Please enter a valid username and password.", "error")

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
