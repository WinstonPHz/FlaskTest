from app import app
from flask import request
import json

@app.route("/all-caps")
def mkcaps():
    try:
        body = request.json
    except:
        return"Return Error 400: Body was not a json", 400
    if "input-string" not in body.keys():
        return "Return Error 400: Json did not contain input-string", 400
    else:
        return_body = {}
        return_body["output-string"] = body["input-string"].upper()
        print(json.dumps(return_body))
        return json.dumps(return_body), 200

