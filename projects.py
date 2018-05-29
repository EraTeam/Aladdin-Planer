import database
import util

from flask import Flask
from flask import render_template, Markup






def verifyProjectState(verifyId):
    if verifyId is True:

        htmlBody = "project exist"

        getCards = database.getProjectCards(verifyId)

        if getCards is False:
            return "<big>There are currenlty not cards in your project!</big>"
        else:
            # @TODO: Create a method to parse the rows, method will be called here and returned
            return "true"

    else:
        htmlBody = "false"

    return htmlBody


def renderProjects(hash, verifyId):


    return util.prepareHtmlLayout(hash, verifyProjectState(verifyId), 0)        