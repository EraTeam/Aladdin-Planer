import database
import util

from flask import Flask
from flask import render_template, Markup


def verifyProjectState(verifyId, projectId):
    if verifyId is True:

        htmlBody = "project exist"

        getCards = database.getProjectCards(projectId)

        if getCards is False:
            return "<div class='ui warning message'>There are currenlty no cards in your project.</div>"
        else:
            returnHtml = []
            returnHtml.append('<div class="ui four link cards">')  # four cards container

            for row in getCards:

                cardMetaData = [
                    ["date", row[5]],
                    ["","test"]
                ]

                html = render_template(
                    "list_cards.html",
                    title=row[3],
                    description=row[4],
                    metaData=cardMetaData
                )
                returnHtml.append(html)

            returnHtml.append('</div>')
            returnVal = ''.join(returnHtml)

            return returnVal

    else:
        htmlBody = "false"

    return htmlBody


def renderProjects(hash, verifyId, projectId):
    return util.prepareHtmlLayout(hash, verifyProjectState(verifyId, projectId), 1, "Create new card")