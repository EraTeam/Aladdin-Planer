"""
    Security.Py
    Security Module, responsible for hash verify and session verify.
"""

from flask import Flask
from flask import redirect, session

import database

def verify_request():
    if session.get('hash'):

        if(database.verifyUserHash(session.get('hash'))):
            
            return True

        else:
            return False        

    else:
        return False 
        