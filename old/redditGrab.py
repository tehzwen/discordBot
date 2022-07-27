import praw
import random
import json
from utils import *

def getImage(subreddit, category):
    keyData = open_file('redditData.txt')

    cID = keyData[0].replace('\n', '')
    cSecret = keyData[1].replace('\n', '')
    passW = keyData[2].replace('\n', '')
    usrAgent = keyData[3].replace('\n', '')
    userNm = keyData[4].replace('\n', '')

    reddit = praw.Reddit(client_id = cID,
                    client_secret = cSecret,
                    password = passW,
                    user_agent = usrAgent,
                    username= userNm)

    try:
        if category == 'top' or category == '':

            imageList = []
            sub = reddit.subreddit(subreddit)
            for submission in sub.top(limit=25):

                imageList.append(submission.url)

            randNum = random.randint(0, len(imageList)-1)

            return imageList[randNum]

        elif category == 'hot':

            imageList = []
            sub = reddit.subreddit(subreddit)
            for submission in sub.hot(limit=25):

                imageList.append(submission.url)

            randNum = random.randint(0, len(imageList)-1)

            return imageList[randNum]

        elif category == 'new':

            imageList = []
            sub = reddit.subreddit(subreddit)
            for submission in sub.new(limit=25):

                imageList.append(submission.url)

            randNum = random.randint(0, len(imageList)-1)

            return imageList[randNum]

    except:
        return None
