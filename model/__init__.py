from app import app
from flask import request, session
from helpers.database import *
from helpers.hashpass import *
from helpers.mailer import *
from bson import json_util, ObjectId
import json
import random

def checkloginusername():
    username = request.form["username"]
    check = db.users.find_one({"username": username})
    if check is None:
        return "No User"
    else:
        return "User exists"

def checkloginpassword():
    username = request.form["username"]
    check = db.users.find_one({"username": username})
    password = request.form["password"]
    hashpassword = getHashed(password)
    if hashpassword == check["password"]:
        sendmail(subject="Login on Flask Admin Boilerplate", sender="Flask Admin Boilerplate", recipient=check["email"], body="You successfully logged in on Flask Admin Boilerplate")
        session["username"] = username
        return "correct"
    else:
        return "wrong"
    

def checkusername():
    username = request.form["username"]
    check = db.users.find_one({"username": username})
    if check is None:
        return "Available"
    else:
        return "Username taken"

def registerUser():
    fields = [k for k in request.form]                                      
    values = [request.form[k] for k in request.form]
    data = dict(zip(fields, values))
    user_data = json.loads(json_util.dumps(data))
    user_data["password"] = getHashed(user_data["password"])
    user_data["confirmpassword"] = getHashed(user_data["confirmpassword"])
    # TASK 4: EXTEND USER SIGNUP
    """
    Extend standard user signup with apps and companies. 
    If a new user will register, it should show by default MSA with app_name “Monitoring” and module “Connection”.
    """
    user_data["permissions"] = default_permissions
    db.users.insert(user_data)
    sendmail(subject="Registration for Flask Admin Boilerplate", sender="Flask Admin Boilerplate", recipient=user_data["email"], body="You successfully registered on Flask Admin Boilerplate")
    print("Done")

def getUserData(username):
    """
    getUserData() function returns user companies
    :return: user permissions in json
    """
    data = db.users.find_one({"username": username})
    if data != None:
        permissions = data['permissions']

        return permissions

    else:
        return {"error":"User not found"}

def getBarData():

    data = {
        "projects": [
            {
                "Server Migration": random.randint(80, 100)
            },
            {
                "Sales Tracking": random.randint(80, 100)
            },
            {
                "Customer Database": random.randint(80, 100)
            },
            {
                "Payout Details": random.randint(80, 100)
            },
            {
                "Account Setup": random.randint(80, 100)
            }
        ]
    }
    return data


