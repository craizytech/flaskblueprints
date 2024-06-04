from flask import session, redirect, request, url_for, render_template, flash
from auth import bp

@bp.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form['nm']
        session["user"] = user
        flash("You have been logged in!", "info")
        return redirect(url_for("user.user"))
    else:
        if "user" in session:
            flash("Already logged in!")
            return redirect(url_for("user.user"))
        return render_template("login.html")
    
@bp.route("/logout")
def logout():
    flash("You have been logged out!", "info")
    session.pop("user", None)
    session.pop("email", None)
    return redirect(url_for("authentication.login"))