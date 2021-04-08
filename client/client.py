import requests
import json
import time
SERVERURI = 'http://127.0.0.1'
PORT = ':3000'

def create():
    URI = '{server}{port}/api/v1/new'.format(server=SERVERURI, port=PORT)

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
    print(response.text, URI)
