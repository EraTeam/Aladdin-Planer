from flask import Flask
from flask import render_template, request, url_for, redirect, session


import sys
#sys.path.append("/home/levent/PycharmProjects/Aladdin-Planer-2/")
sys.path.append("/home/kian/schule/dev/aladdin-planer/Aladdin-Planer/")

# @TODO: @theTruth777 Add comments
import database
import dashboard

app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'


@app.route("/success/<name>")
def success(name):
    return "Herzlich Willkommen %s" % name


@app.route("/")
def index():

    if session.get('hash'):

        if(database.verifyUserHash(session.get('hash'))):

            return dashboard.renderDashboard(session.get('hash'))

        else:
            session.pop('hash', None)
            return redirect("/login", code=302)    


    else:
        return redirect("/login", code=302)


@app.route("/login_request", methods=["POST", "GET"])
def login_request():
    if session.get('hash'):
        return redirect("/", code=302)
    else:    
        if request.method == "POST":
            user = request.form["username"]
            password = request.form["password"]
            
            if user != "" and password != "":
                verifyUser = database.get_registered_user(user, password)

                if verifyUser is False:
                    return "user does not exist"
                else:
                    session['hash'] = verifyUser[0][3]
                    return redirect("/", code=302)

            else:
                return "login failed, not every field was filled!"
    

@app.route("/register_request", methods=["POST"])
def register_request():
    if session.get('hash'):
        return redirect("/", code=302)
    else:
        if request.method == "POST":
            user = request.form["username"]
            password = request.form["password"]
            email = request.form["email"]

            if user != "" and password != "" and email != "":

                insert = database.insert_new_user(user, email, password)

                if insert is True:
                    return redirect("/login", code=302)
                else:
                    return redirect("/register", code=302)

            else:
                return redirect("/register", code=302)


        else:
            return redirect("/register", code=302)


@app.route("/logout")
def logout():
    if session.get('hash'):
        session.pop('hash', None)
        return redirect("/", code=302)
    else:
        return redirect("/", code=302)


@app.route("/login")
def login():
    if session.get('hash'):
        return redirect("/", code=302)
    else:
        return render_template('login_form.html')


@app.route("/register")
def register():
    if session.get('hash'):
        return redirect("/", code=302)
    else:
        return render_template('register_form.html')


def validation(username, password):
    if username == "admin" and password == "secret":
        return redirect(url_for("index", userName=username))
    else:
        return render_template("login.html", error="invalid credentials")


#   Redirect user on /project call to index
@app.route("/projects")
def call_projects_page():
    return redirect("/", code=302)


# Is handling the call of an project page
# @TODO: Create a project.py, create a global.py and put methods like hash validaten there to be called from
# other methods!
@app.route("/projects/<id>")
def call_projects_page_valid(id):
    if session.get('hash'):
        
        validate = database.validateProject(id)
        if validate is True:
            return "project exist"
        else:
            return "Project does not exist or is not active"
    else:
        return redirect("/", code=302)


#   Create a new dashboard-project
@app.route("/create_project", methods=['POST'])
def create_project():
    if session.get('hash'):

        if request.method == "POST":
            title = request.form["project_title"]
            description = request.form["project_description"]

            if title != "" and description != "":
                database.createNewProject(title, description)
                return redirect("/", code=302)
            else:
                return redirect("/", code=302)
                
        else:
            return redirect("/", code=302)
    else:
        return redirect("/", code=302)        


if __name__ == '__main__':

    app.debug(1)
    app.run()
