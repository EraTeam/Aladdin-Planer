"""
    Util.PY - Utility
    Provides several methods that are used throughout the application
"""


import database

from flask import Flask
from flask import render_template, Markup


def getUserName(hash):
    username = database.getUserInformation(hash)
    return username[0][0].title()


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



def getHtmlModal(type):
    if type is 0:
        return render_template('create_project_modal.html')


def prepareHtmlLayout(hash, htmlContent, type):
    return render_template(
        'index.html',
        greetMessage="Willkommen,",
        userName=getUserName(hash),
        location="Dashboard",
        templateModal=Markup(getHtmlModal(type)),
        htmlMainContent=Markup(htmlContent),
        activeProjectLinks=Markup(getActiveProjectLinks())
    )