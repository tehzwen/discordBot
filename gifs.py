import requests
import json
from utils import *
import random

def refreshAuth():
    authurl = 'https://api.gfycat.com/v1/oauth/token'
    print("Refreshing OAUTH data.....")
    with open('gifyCatData.txt') as json_file:  
        data = json.load(json_file)
        
    payload = data['data'][0]
    auth = requests.post(authurl, data=str(payload))
    print("Status: ", auth.status_code)
    r = json.loads((auth.content).decode())
    accessToken = r['access_token']

    return accessToken

def makeSearchReq(searchWord):
    url = 'https://api.gfycat.com/v1/gfycats/search?search_text=' + searchWord
    data = open_file('currentGifKeys.txt')
    accessToken = data[0]

    headers = {
    "Authorization" : accessToken
    }

    searchReq = requests.get(url, headers=headers)

    while searchReq.status_code != 200:
        accessToken = refreshAuth()
        headers = {
            "Authorization" : accessToken
        }
        
        searchReq = requests.get(url, headers=headers)

    print("search successful...")
    saveCurrentKey(accessToken)

    searchData = json.loads(searchReq.content.decode('utf-8'))
    
    return searchData


def saveCurrentKey(accessTok):
    temp = open('currentGifKeys.txt', 'w')
    temp.write(accessTok)


def getGifLink(searchResults):
    gifURLList = []
    try:
        for item in searchResults['gfycats']:
            for container in item:
                if container == 'url':
                    gifURLList.append(item[container])

    except: 
        return None

    if len(gifURLList) == 0:
        return None

    randNum = random.randint(0, len(gifURLList)-1)

    url = gifURLList[randNum]

    return url


def mainRun(searchWord):
    data = makeSearchReq(searchWord)
    url = getGifLink(data)

    return url