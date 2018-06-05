import database
import util

from flask import Flask
from flask import render_template, Markup

def content(hash):
    getUserInfo = database.getUserInformation(hash)

    if getUserInfo is not False:
        for row in getUserInfo:
            return render_template("profile.html", username=row[0], email=row[1], password=row[2])
    else:
        return False


def renderProfile(hash):
    return util.prepareHtmlLayout(hash, content(hash), 2, "Create new project")

