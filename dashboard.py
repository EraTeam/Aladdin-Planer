import database

from flask import Flask
from flask import render_template, Markup

"""
    Dashboard Class
    is responsible for handling the dashboard frontend and dashboard application logic

"""


def getUserName(hash):
    username = database.getUserInformation(hash)
    return username[0][0].title()


def getActiveProjects():
    getProjects = database.getActiveProjects()

    if getProjects is False:
        return "<br /><br /><big>There are currently no projects.</big>"
    else:
        returnHtml = []

        for row in getProjects:
            html = render_template("dashboard_project_cards.html", title=row[2], description=row[3], date=row[4], id=row[1])
            returnHtml.append(html)

        returnVal = ''.join(returnHtml)

        return returnVal


def renderDashboard(hash):
    return render_template('index.html', greetMessage="Willkommen,", userName=getUserName(hash), location="Dashboard", activeProjects=Markup(getActiveProjects()))