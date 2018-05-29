import database
import util

from flask import Flask
from flask import render_template, Markup


def verifyProjectState(verifyId):
    if verifyId is True:

        htmlBody = "project exist"

        getCards = database.getProjectCards(verifyId)

        if getCards is False:
            return "<div class='ui warning message'>There are currenlty no cards in your project.</div>"
        else:
            # @TODO: Create a method to parse the rows, method will be called here and returned
            returnHtml = []
            returnHtml.append('<div class="ui three cards">')  # three cards container

            returnHtml.append("<div class='ui success message'>There is something.</div>")

            returnHtml.append('</div>')
            returnVal = ''.join(returnHtml)

            return returnVal

    else:
        htmlBody = "false"

    return htmlBody


def renderProjects(hash, verifyId):
    return util.prepareHtmlLayout(hash, verifyProjectState(verifyId), 1)