from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', siteTitle="Aladdin Planer!", greetMessage="Willkommen ", userName="Hannelore Heftig", locationMessage=", hier ist deine Übersicht!")


if __name__ == '__main__':
    app.debug(1)
    app.run()
