import requests
import json
import time
import os
import base64, io
from PIL import Image
SERVERURI = 'http://192.168.76.16'
PORT = ':3000'

def create(name=""):
    URI = '{server}{port}/api/v1/new?name={name}'.format(server=SERVERURI, port=PORT, name=name)

    response = requests.get(URI)

    if response.status_code == 200:
        responseLoads = json.loads(response.text)
        id = responseLoads['newInstance']['id']
        return id
    else:
        return "error"

def getStatus(id):
    URI = '{server}{port}/api/v1/find?id={id}'.format(server=SERVERURI, port=PORT, id=id)
    response = requests.get(URI)
    if response.status_code == 200:
        responseLoads = json.loads(response.text)['interfaces']
        return [responseLoads['hp'], responseLoads['mp']]
    else:
        return 'error'


def setStatus(id, hp, mp):
    URI = '{server}{port}/api/v1/change?id={id}&hp={hp}&mp={mp}'.format(server=SERVERURI, port=PORT, id=id, hp=hp, mp=mp)
    response = requests.post(URI)


def quit(id):
    URI = '{server}{port}/api/v1/exit?id={id}'.format(server=SERVERURI, port=PORT, id=id)
    response = requests.get(URI)

def all():
    URI = '{server}{port}/api/v1/all'.format(server=SERVERURI, port=PORT)
    response = requests.get(URI)
    if response.status_code == 200:
        interfaces = json.loads(response.text)['interfaces']
        return interfaces
    else:
        return []

def pause(id):
    URI = '{server}{port}/api/v1/pause?id={id}'.format(server=SERVERURI, port=PORT, id=id)
    response = requests.get(URI)
    if response.status_code == 200:
        return True
    else:
        return False

def play(id):
    URI = '{server}{port}/api/v1/play?id={id}'.format(server=SERVERURI, port=PORT, id=id)
    response = requests.get(URI)
    if response.status_code == 200:
        return True
    else:
        return False
        
def getDialog():
    URI = '{server}{port}/api/v1/dialog/get'.format(server=SERVERURI, port=PORT, id=id)

    response = requests.get(URI)
    if response.status_code == 200:
        dialogStatus = json.loads(response.text)['lock']
        return dialogStatus


def offDialog():
    URI = '{server}{port}/api/v1/dialog/off'.format(server=SERVERURI, port=PORT, id=id)
    response = requests.get(URI)

def dialoging(screen):
    def tobase64(img):
	    return base64.b64encode(img).decode('ascii')
    headers = {'Content-type': 'text/xml'}

    URI = '{server}{port}/api/v1/dialog/create'.format(server=SERVERURI, port=PORT, id=id)
    im = Image.open(screen)
    imgByteArr = io.BytesIO()
    im.save(imgByteArr, format="PNG")
    encode = tobase64(imgByteArr.getvalue())
    files = {
        'dialog_checker[image]': encode
    }
    response = requests.post(URI, files=files, headers=headers)
    if response.status_code == 200:
        return True
    else:
        return False

def getAction():
    URI = '{server}{port}/api/v1/action/get'.format(server=SERVERURI, port=PORT)
    response = requests.get(URI)
    if response.status_code == 200:
        action = json.loads(response.text)
        return action
    else:
        return False

def offAction():
    URI = '{server}{port}/api/v1/action/off'.format(server=SERVERURI, port=PORT)
    response = requests.get(URI)
    if response.status_code == 200:
        return True
    else:
        return False