import requests
from flask import Flask, render_template, request
import json
import os

text1 = "The VM instance is successfully created. Check your linode Workspace."
text2 = "The VM instance is destroyed successfully"


app = Flask(__name__)

@app.route('/<DeviceName>/')
def action(DeviceName):
    if DeviceName == 'provision':
        os.system("./automate.sh")
        provision(text1)
    if DeviceName == 'destroy':
        os.system("./destroy.sh")
        destroy(text2)
    


def provision(text):
    json = { 'text': text }
    response1 = requests.post($SLACK_WEBHOOK,json=json)

def destroy(text):
    json = { 'text': text }
    response2 = requests.post($SLACK_WEBHOOK,json=json)



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8081)
