import database
import util

from flask import Flask
from flask import render_template, Markup

"""
    Dashboard Class
    is responsible for handling the dashboard frontend and dashboard application logic

"""


def getUserName(hash):
    username = database.getUserInformation(hash)
    return username[0][0].title()


def getActiveProjectCards():
    getProjects = database.getActiveProjects()

    if getProjects is False:
        return "<div class='ui warning message'>There are currently no projects.</div>"
    else:
        returnHtml = []
        returnHtml.append('<div class="ui four cards">')  # four cards container

        for row in getProjects:
            html = render_template("project_cards.html", title=row[2], description=row[3], date=row[4], id=row[0])
            returnHtml.append(html)

        returnHtml.append('</div>')
        returnVal = ''.join(returnHtml)

        return returnVal


def getActiveProjectLinks():
    getProjects = database.getActiveProjects()

    if getProjects is False:
        return ""
    else:
        returnHtml = []
        returnHtml.append('<div class="item"><div class="header">Projects</div><div class="menu">')

        for row in getProjects:
            html = '<a href="/projects/' + str(row[0]) + '" class="item" title="' + str(row[2]) + '">' + str(row[2]) + '</a>'
            returnHtml.append(html)

        returnHtml.append('</div></div>')
        returnVal = ''.join(returnHtml)

        return returnVal


def renderDashboard(hash):
    return util.prepareHtmlLayout(hash, getActiveProjectCards(), 0, "Create new project")