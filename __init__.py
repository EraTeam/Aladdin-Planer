"""
    __init__.py
    Main .py file that is handling the application logic.
    Is responsible for handling the routing and calling methods based on the rout.
"""


#   Flask modules
from flask import Flask
from flask import render_template, request, url_for, redirect, session

#   Sys modul for our custom made moudls
#   @TODO: wee need to find a workaround for that
import sys
#sys.path.append("/home/levent/PycharmProjects/Aladdin-Planer-2/")
sys.path.append("/home/kian/schule/dev/aladdin-planer/Aladdin-Planer/")

#   Aladding planer modules
import database
import dashboard
import projects


#   Flask secret key
#   NOTE: Change this key once you plan to put this application live. 
#   This key is responsible for the session-value encryption.
app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'


@app.route("/success/<name>")
def success(name):
    return "Herzlich Willkommen %s" % name


#   Main route when the url is called
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


#   Handling the request of a user login
#   NOTE: This is NOT the /login url!
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
    

#   Handling the request of a user registration
#   NOTE: This is NOT the /register url!
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


#   Handling the logout and removing the session-cookie
@app.route("/logout")
def logout():
    if session.get('hash'):
        session.pop('hash', None)
        return redirect("/", code=302)
    else:
        return redirect("/", code=302)


#   Handling the login and creating the session-cookie with the unique user hash
@app.route("/login")
def login():
    if session.get('hash'):
        return redirect("/", code=302)
    else:
        return render_template('login_form.html')


#   Display the /register html page
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
@app.route("/projects/")
def call_projects_page():
    return redirect("/", code=302)


#   Handling the call on a /project/<id> page
@app.route("/projects/<id>")
def call_projects_page_valid(id):

    if session.get('hash'):

        if(database.verifyUserHash(session.get('hash'))):
           
            validate = database.validateProject(id)
            if validate is True:
                return projects.renderProjects(session.get('hash'), validate, id)
            else:
                return redirect("/", code=302)                

        else:
            return redirect("/", code=302)
            
        
    else:
        return redirect("/", code=302)


#   Create a new dashboard-project
@app.route("/create_project", methods=['POST'])
def create_project():
    if session.get('hash'):

        if(database.verifyUserHash(session.get('hash'))):

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
            

    else:
        return redirect("/", code=302)        


@app.route("/add_card", methods=['POST'])
def add_card():
    if session.get('hash'):

        if(database.verifyUserHash(session.get('hash'))):

            if request.method == "POST":
                title = request.form["card_title"]
                description = request.form["card_description"]

                if title != "" and description != "":
                    getId = str(request.referrer).split("/")
                    database.createProjectCards(int(getId[4]), title, description) 
                    return redirect("/projects/" + getId[4], code=302)

                else:
                    return redirect("/", code=302)        
            else:
                return redirect("/", code=302)        
                    
    else:
        return redirect("/", code=302)        
        


@app.route("/profile")
def profile_page():
    if session.get('hash'):

        if(database.verifyUserHash(session.get('hash'))):
            return "profile page"

        else:
            return redirect("/", code=302)        

    else:
        return redirect("/", code=302)        
        



if __name__ == '__main__':

    app.debug(1)
    app.run()
