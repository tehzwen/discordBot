from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
from utils import *


# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
lines = open_file("youtubeKeys.txt")

DEVELOPER_KEY = lines[0]
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def youtube_search(keyword):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  # Call the search.list method to retrieve results matching the specified
  # query term.
  search_response = youtube.search().list(
    q=keyword,
    part="id,snippet",
    maxResults=10
  ).execute()

  videos = []
  channels = []
  playlists = []

  # Add each result to the appropriate list, and then display the lists of
  # matching videos, channels, and playlists.
  for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video":
      videos.append("%s (%s)" % (search_result["snippet"]["title"],
                                 search_result["id"]["videoId"]))

 
  searchURL = ""
  defaultURL = "https://www.youtube.com/watch?v="
  foundBracket = False

  try:
    for i in range(len(videos[0])):
        if videos[0][i] == '(':
            #print("found bracket")
            foundBracket = True
            continue
        
        if videos[0][i] == ')':
            #print("end bracket")
            foundBracket = False
            continue
        
        if foundBracket:
            searchURL += videos[0][i]

  except:
    return None, None

  #print(searchURL)
  tempVal = ['','','','','','','','','','','','']
  tempList = list(searchURL)
  counter = 0

# use this part of logic to get videos that are official music videos
  for x in range(-11, 0, 1): 
      #print(tempList[x])
      tempVal[counter] = (tempList[x])
      counter += 1

  searchURL = defaultURL + ''.join(tempVal)
 
  return searchURL, videos[0]

'''def returnSearchURL(keyword):
    

    if SEARCHED == False:
        argparser.add_argument("--q", help="Search term", default="Google")
        argparser.add_argument("--max-results", help="Max results", default=25)
        args = argparser.parse_args()

    try:
        searchURL = youtube_search(args, keyword)
        
        return searchURL

    except HttpError as e:
        print ("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)) '''

    