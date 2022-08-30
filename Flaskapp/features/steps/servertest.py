import json
import requests
from behave import *

url = "http://127.0.0.1:5000/all-caps"
headers = {"content-type":"application/json"}

@Given("{input_json}")
def given_request(context, input_json):
    response = requests.get(url, data=input_json, headers=headers)
    context.status_code = response.status_code
    context.reply_json = response.text
    context.input = input_json

@When("a {statusCode} status is received")
def when_request(context, statusCode):
    context.answer = str(context.status_code) == statusCode

@Then("the output-string should be in all caps")
def then_200(context):
    if context.answer:
        input_string = json.loads(context.input)
        out_string = json.loads(context.reply_json)
        assert input_string["input-string"].upper() == out_string["output-string"]

@Then("we should get an error message")
def then_400(context):
    assert context.answer is True
