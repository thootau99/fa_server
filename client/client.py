import requests
import json
import time
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
        