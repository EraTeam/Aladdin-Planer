from flask import Flask
from flask import render_template, request, url_for, redirect

app = Flask(__name__)


@app.route("/success/<name>")
def success(name):
    return "Herzlich Willkommen %s" % name


@app.route("/")
def index():
    return render_template('index.html', siteTitle="Aladdin Planer!", greetMessage="Willkommen ", userName="Hannelore Heftig", locationMessage=", hier ist deine Übersicht!")


@app.route("/login_request", methods=["POST", "GET"])
def login_request():
    if request.method == "POST":
        user = request.form["username"]
        password = request.form["password"]
        return validation(username=user, password=password)
    else:
        user = request.args.get("username")
        password = request.args.get("password")
        return validation(username=user, password=password)


@app.route("/register_request", methods=["POST", "GET"])
def register_request():
    if request.method == "POST":
        user = request.form["username"]
        password = request.form["password"]
        return validation(username=user, password=password)
    else:
        user = request.args.get("username")
        password = request.args.get("password")
        return validation(username=user, password=password)


@app.route("/login")
def login():
    return render_template('login_form.html')


@app.route("/register")
def register():
    return render_template('register_form.html')


def validation(username, password):
    if username == "admin" and password == "secret":
        return redirect(url_for("index", userName=username))
    else:
        return render_template("login.html", error="invalid credentials")


if __name__ == '__main__':
    app.debug(1)
    app.run()
