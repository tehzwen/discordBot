import discord
from discord.ext.commands import Bot
from discord.ext import commands
import re
import time
from utils import *
from Player import *
from joke import *
from trivia import *
from ytTest import *
from redditGrab import *
from gifs import *
from database import *
import random
from maps import *
import pymysql
from rrrather import *
from slots import *

client = discord.Client()
#bot_prefix = "?"
yTube = Player() #creating a Player object to hold values for player
dataBaseInfo = open_file('databaseKeys.txt')
password = dataBaseInfo[0]
print(password)


cnx = pymysql.connect(db= 'discordBot',user='zach', passwd=str(password), host='127.0.0.1')
#cnx = pymysql.connect(db= ,user=user, passwd=passwd, host=host)
d1 = dataSet(cnx)
#client = commands.Bot(command_prefix = bot_prefix)

@client.event
async def on_ready():
    count = False
    print("Bot Online!")
    print("Name: ",client.user.name)
    game = discord.Game(name = "learning from Skynet")
    await client.change_presence(game = game)
    for server in client.servers:
        for member in server.members:
            yTube.userList.append(member)
            addnewUser(d1, str(member))

        for channel in server.channels:
            if channel.name == "bot-testing-grounds" and count == False:
                await client.send_message(channel, "$intro")
                await client.send_message(channel, "$commands")
                count = True
                break
    
@client.event
async def on_member_join(member):
    addnewUser(d1, str(member))



@client.event
async def on_message(message):
###################################################################################
    if message.content.startswith('$greet'):
        await client.send_message(message.channel, 'Say hello')
        msg = await client.wait_for_message(author = message.author, content ='hello')
        await client.send_message(message.channel, 'Hey')

###################################################################################

    elif message.content.startswith('$info'):
        await client.send_message(message.channel, "*Long Drawn Out Sigh*... what do you need? Zwen is the admin, this is a simple quaint server... Either ask him or type $commands for a list of the commands currently available")
###################################################################################

    elif message.content.startswith('$commands'):
        await client.send_message(message.channel, "List of all Commands:\n$greet (simple greeting message)\n$info (self explanatory)\n$commands(list of all the commands)\n$joke (haha) \n$trivia (try your best)\n$TTS (get me to use my beautiful voice)\n$song (search youtube for top result and play it in voice chat)\n$gif(search for a gif)\n$video (search youtube for a video)\n$gamble (you feeling lucky boy?)\n$blackjack\n$maps(search a location)\n$points\n$standings")
################################################################################### 

    elif message.content.startswith('$intro'):
        await client.send_message(message.channel, "I'm the beginning of a discord bot written by Zwen to screw around and hopefully become self awar- I mean become intelligent")
###################################################################################

    elif message.content.startswith('$joke'):
        await client.send_message(message.channel, getData())
###################################################################################

    elif message.content.startswith('$trivia'):
        questionString, correct, answerList = getQuestion()
        optionsList = ['A', 'B', 'C', 'D']
        correctChar = ''
        await client.send_message(message.channel, questionString)
        for i in range(len(answerList)):
            await client.send_message(message.channel, optionsList[i] + ": " + answerList[i])

        msg = await client.wait_for_message(author = message.author)
        answer = msg.content.upper() #make their entry uppercase no matter what

        correctBool = False
        for i in range(len(optionsList)):

            if answer == optionsList[i] and answerList[i] == correct:
                correctChar = optionsList[i]
                await client.send_message(message.channel, "Correct! You got 10 points!")
                editPoints(d1.cnx, 10, str(message.author))
                correctBool = True
            
        if not correctBool:
            await client.send_message(message.channel, "Incorrect, the correct answer was: " + correctChar +' '+ correct)
###########################################################################################################

    elif message.content.startswith('$TTS'):
        newMsg = message.content.replace('$TTS ', '')
        if newMsg == '$TTS':
            await client.send_message(message.channel, "you're a dick, im not going into an infinite loop", tts = True)

        else:
            await client.send_message(message.channel, newMsg, tts = True)

###########################################################################################################
    
    elif message.content.startswith('$song'):
        newMsg = message.content.replace('$song ', '')
        
        count = False
        if not client.is_voice_connected(message.server):

            for server in client.servers:
                for channel in server.channels:
                    if channel.name == "General" and count == False: #can replace "General" with your desired voice channel here
                        voiceChan = channel
                        count = True
                        break

            voice = await client.join_voice_channel(voiceChan)
            yTube.addVoice(voice)

        else:
            print("already in channel")
            yTube.player.stop()
        
        songToPlay, songDesc = youtube_search(newMsg)

        if songToPlay == None:
            await client.send_message(message.channel, "No items found for search.")

        await client.send_message(message.channel, "Currently loading..... " + songDesc)
        voice = yTube.getVoice()
        yTube.player = await voice.create_ytdl_player(songToPlay)
        yTube.player.volume = 0.75
        yTube.player.start() 
        playing = True
        muted = False

        #handling commands once the audio is playing
        while playing:
            msg = await client.wait_for_message()

            if msg.content.startswith('$stop'):
                playing = False
                yTube.player.stop()
                await voice.disconnect()
            
            elif msg.content == '$volumeup':

                if yTube.player.volume >= 0 and yTube.player.volume < 2.0:
                    yTube.player.volume += 0.25


            elif msg.content == '$volumedown':
                

                if yTube.player.volume > 0 and yTube.player.volume <= 2.0:
                    yTube.player.volume += -0.25
                

            elif msg.content.startswith('$mute'):

                if not muted:
                    yTube.volume = yTube.player.volume
                    yTube.player.volume = 0.0
                    muted = True
                
                else:
                    yTube.player.volume = yTube.volume
                    muted = False

            elif msg.content.startswith('$pause'):
                yTube.player.pause()

            elif msg.content.startswith('$play'):
                yTube.player.resume()

            
            
###########################################################################################################

    elif message.content.startswith('$gif'):
        newMsg = message.content.replace('$gif ', '')

        gifurl = mainRun(newMsg)
        if gifurl == None:
            await client.send_message(message.channel, "Returned an empty search, type $gif to try again....")
        await client.send_message(message.channel, gifurl)

###########################################################################################################

    elif message.content.startswith('$video'):
        newMsg = message.content.replace('$video ', '')

        videoURL, videoDesc = youtube_search(newMsg)

        if videoURL == None:
            await client.send_message(message.channel, "No items found for search.")
        else:
            await client.send_message(message.channel, videoURL)
###########################################################################################################

    elif message.content.startswith('$points'):
        author = str(message.author)
        points = getPoints(d1.cnx, author)
        await client.send_message(message.channel, "You currently have "+ str(points) +" points.")

###########################################################################################################

    elif message.content.startswith('$gamble'):
        newMsg = message.content.replace('$gamble ', '')
        currentPoints = getPoints(d1.cnx, str(message.author))
        win = gambleFunc(currentPoints, int(newMsg))

        if win:
            await client.send_message(message.channel, "You won "+ str(newMsg) +" points.")
            editPoints(d1.cnx, int(newMsg), str(message.author))

        elif win == None:
            await client.send_message(message.channel, "You don't have enough points to gamble " + str(newMsg))
        
        elif win == False:
            await client.send_message(message.channel, "You lost "+ str(newMsg) +" points.")
            editPoints(d1.cnx, -(int(newMsg)), str(message.author))
            
###########################################################################################################
    elif message.content.startswith('$blackjack'):
        newMsg = message.content.replace('$blackjack ', '')
        currentPoints = getPoints(d1.cnx, str(message.author))
    
        if newMsg == '$blackjack' or (int(newMsg)) < 0:
            await client.send_message(message.channel, "Need to enter a valid bet amount (ie. $blackjack 50).")
            return

        if currentPoints < int(newMsg):
            await client.send_message(message.channel, "You dont have "+str(newMsg)+" points to gamble with.")
            return

        await client.send_message(message.channel, "Okay, the goal is to not go over 21, you can use $hitme, $stay to play the game and make points.")

    
        b1 = blackJack()
        b1.shuffle()
        win = None
        done = False

        dealerFirst = b1.deal()
        await client.send_message(message.channel, "Dealer has " + str(dealerFirst)+ " and 1 card facedown.")
        dealerTotal = b1.deal()
        b1.reset_value()
        
        while not done:

            msg = await client.wait_for_message(author = message.author)
            

            

            if msg.content.startswith('$hitme'):
                b1.deal()
                win = b1.checkStatus()
                
            
                if win:
                    newVal = (int(newMsg)) * 3
                    await client.send_message(message.channel, "BLACKJACK! You won " + str(newVal)+" points.")
                    editPoints(d1.cnx, (newVal), str(msg.author))
                    done = True

                elif win == None:
                    await client.send_message(message.channel, "You're at " + str(b1.currentVal))

                elif not win:
                    await client.send_message(message.channel, "BUST! You lost " + str(newMsg) + " points.")
                    editPoints(d1.cnx, -(int(newMsg)), str(msg.author))
                    done = True

            elif msg.content.startswith('$stay'):
                if b1.currentVal < dealerTotal:
                    await client.send_message(message.channel, "Dealer reveals facedown card and has a total of " + str(dealerTotal)+"."+" DEALER WINS! You lost " + str(newMsg) + " points.")
                    editPoints(d1.cnx, -(int(newMsg)), str(msg.author))
                    editPoints(d1.cnx, (int(newMsg)), 'zwenBot#0844')
                    done = True
                
                elif b1.currentVal == dealerTotal:
                    await client.send_message(message.channel, "Dealer reveals facedown card and has a total of " + str(dealerTotal)+"."+" DRAW! Points returned.")
                    done = True
                
                elif b1.currentVal > dealerTotal:
                    await client.send_message(message.channel, "Dealer reveals facedown card and has a total of " + str(dealerTotal)+"."+" YOU WIN! You won " + newMsg +" points.")
                    editPoints(d1.cnx, int(newMsg), str(msg.author))
                    done = True

###########################################################################################################

    elif message.content.startswith('$standings'):
        NAMELIST = getuserNames(d1.cnx)
        POINTSLIST = getuserPoints(d1.cnx)

        for i in range(len(NAMELIST)):
            await client.send_message(message.channel, "|Name: " + NAMELIST[i][0] + "| |Points: " + str(POINTSLIST[i][0]) + " |")

###########################################################################################################

    elif message.content.startswith('$give'):
        newMsg = message.content.replace('$give ', '')
        numAmount = []

        for char in newMsg:
            if char.isdigit():
                numAmount.append(char)

###########################################################################################################

    elif message.content.startswith('$maps'):
        await client.send_message(message.channel, "Where would you like the address to?")
        msg = await client.wait_for_message(author = message.author)
        address, map_location = addressLookup(msg.content)

        if address == None:
            await client.send_message(message.channel, "Returned an empty search.")
        else:

            await client.send_message(message.channel, address)
            await client.send_message(message.channel, map_location)

###########################################################################################################

    elif message.content.startswith('$image'):
        category = ''

        newMsg = message.content.replace('$image ', '')

        if newMsg.startswith('top'):
            newMsg = newMsg.replace('top ', '')
            category = 'top'

        elif newMsg.startswith('hot'):
            newMsg = newMsg.replace('hot ', '')
            category = 'hot'

        elif newMsg.startswith('new'):
            newMsg = newMsg.replace('new ', '')
            category = 'new'

        url = getImage(newMsg, category)
        if url == None:
            await client.send_message(message.channel, "Returned an empty search.Visit https://www.reddit.com/r/ListOfSubreddits/wiki/listofsubreddits for a list of subreddits.")
        await client.send_message(message.channel, url)

###########################################################################################################

    elif message.content.startswith('$listsubreddits'):
        subList = printSubreddits()
        for item in subList:
            await client.send_message(message.channel, item)

###########################################################################################################

    elif message.content.startswith('$rather'):
        pack = get_wyr()
        for item in pack:
            await client.send_message(message.channel, item)

###########################################################################################################

    elif message.content.startswith('$slots'):
        newMsg = message.content.replace('$slots ', '')

        slot = runSlots()

        for column in slot:
            for i in range(3):
                await client.send_message(message.channel, column[i])

        



keys = open_file('keys.txt')

client.run(keys[0])

cnx.close()


