import database
import util

from flask import Flask
from flask import render_template, Markup

def content(hash):
    getUserInfo = database.getUserInformation(hash)

    if getUserInfo is not False:
        return "worked"
    else:
        return False



def renderProfile(hash):
    return util.prepareHtmlLayout(hash, content(hash), 2, "Create new project")

