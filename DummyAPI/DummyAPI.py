from flask import Flask
from flask import request
import json
import os

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST', 'DELETE'])
def state_name():
    if request.method == 'GET':

        if ("USER" in os.environ):
            USER = str(os.getenv('USER'))
        else:
            USER = "NotinLocal"

        if ("LASTNAME" in os.environ):
            LASTNAME = str(os.getenv('LASTNAME'))
        else:
            LASTNAME = "NotinLocal"

        if ("THIRDNAME" in os.environ):
            THIRDNAME = str(os.getenv('THIRDNAME'))
        else:
            THIRDNAME = "NotinLocal"

        json_string =  '{ "USER":"' + USER + '", "LASTNAME":"' + LASTNAME +'", "THIRDNAME":"' + THIRDNAME +'"}'
        
        data = json.loads(json_string)

        return(data)

    if request.method == 'POST':

        USER = request.args.get("USER")
        if not (isinstance(USER, str)):
            USER = "NonePosted"
        os.environ["USER"] = USER

        LASTNAME = request.args.get("LASTNAME")
        if not (isinstance(LASTNAME, str)):
            LASTNAME = "NonePosted"
        os.environ["LASTNAME"] = LASTNAME

        THIRDNAME = request.args.get("THIRDNAME")
        if not (isinstance(THIRDNAME, str)):
            THIRDNAME = "NonePosted"
        os.environ["THIRDNAME"] = THIRDNAME
        
        json_string =  '{ "USER":"' + USER + '", "LASTNAME":"' + LASTNAME +'", "THIRDNAME":"' + THIRDNAME +'"}'
        
        data = json.loads(json_string)

        return(data)

    if request.method == 'DELETE':

        os.environ.pop("USER")
        os.environ.pop("LASTNAME")
        os.environ.pop("THIRDNAME")

        json_string =  '{ "USER":"JustDeleted", "LASTNAME":"JustDeleted", "THIRDNAME":"JustDeleted"}'
        
        data = json.loads(json_string)

        return(data)

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port=3333, debug = True)