import requests
import json
class Interface:
    id = 0
    hp = 0
    mp = 0
    def __init__(self, id=0, hp=0, mp=0):
        self.id = id
        self.hp = hp
        self.mp = mp

newInstance = Interface()
SERVERURI = "http://127.0.0.1"
PORT = ":3000"
def create():

    URI = '{server}{port}/api/v1/new'.format(server=SERVERURI, port=PORT)

    response = requests.get(URI)

    if response.status_code == 200:
        responseLoads = json.loads(response.text)
        id = responseLoads['newInstance']['id']
        newInstance.id = id

def getStatus(id):
    URI = '{server}{port}/api/v1/find?id={id}'.format(server=SERVERURI, port=PORT, id=id)
    response = requests.get(URI)
    if response.status_code == 200:
        responseLoads = json.loads(response.text)['interfaces']
        newInstance.hp = responseLoads['hp']
        newInstance.mp = responseLoads['mp']



def setStatus(id, hp, mp):
    URI = '{server}{port}/api/v1/change?id={id}&hp={hp}&mp={mp}'.format(server=SERVERURI, port=PORT, id=id, hp=hp, mp=mp)
    response = requests.get(URI)
    print(response.text, URI)

getStatus(22)