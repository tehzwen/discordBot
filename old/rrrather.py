import requests
import json

def get_wyr():
    """ Gets a entry from the RRRather API and cleans up the data """
    r = requests.get("http://www.rrrather.com/botapi")
    data = r.json()

    title = data['title']
    choice1 = data['choicea']
    choice2 = data['choiceb']
    package = [title, choice1, choice2]
    return package