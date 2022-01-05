from flask import Flask, jsonify, session, escape
app = Flask(__name__)
app.config["SECRET_KEY"] = "camila"

@app.route("/")
def index():
    return jsonify({"msg":"ok","route":"index"})


@app.route("/login/<string:user>")
def login(user):
    session["username"] = user
    return jsonify({"msg":"ok",
    "data":"you logged good"})


@app.route("/home")
def home():
    if "username" in session:
        return f"You are {escape(session['username'])}"
    return "you are not logged"


@app.route("/logout")
def logout():
    session.pop("username",None)
    return "You have been logged out"

@app.errorhandler(Exception)
def error(e):
    return jsonify({"error":f"{e}"})



if __name__ == "__main__":
    app.run(debug=True)