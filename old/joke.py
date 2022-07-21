import requests
import urllib
import urllib3
import json



def getData():
    r = requests.get("https://icanhazdadjoke.com/slack")
    data = json.loads(r.text)


    jokeString = ""
    for element in data['attachments']:
        for item in element['fallback']:
            jokeString += item

    return jokeString



