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
        fields = [
            ["Enter the projects title", "input", "text", "project_title", "Project Title"],
            ["Enter the projects description", "textarea", "text", "project_description", 'Project Description']
        ]
        return render_template('create_modal.html', headerText="Create a new project", actionPath="/create_project", formFields=fields)
    elif type is 1:
        fields = [
            ["Enter the cards title", "input", "text", "card_title", "Card Title"],
            ["Enter the cards description", "textarea", "text", "card_description", "Card Description"]
        ]
        return render_template('create_modal.html', headerText="Add a new card", actionPath="/add_card", formFields=fields)



def prepareHtmlLayout(hash, htmlContent, type, modalActionMsg):
    return render_template(
        'index.html',
        greetMessage="Welcome,",
        userName=getUserName(hash),
        location="Dashboard",
        templateModal=Markup(getHtmlModal(type)),
        htmlMainContent=Markup(htmlContent),
        activeProjectLinks=Markup(getActiveProjectLinks()),
        createCardProject=modalActionMsg
    )