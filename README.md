discordBot

V0.03 WORK IN PROGRESS Feb 16, 2018

additions:
-gifs from gifycat
-songs playing through youtube in voice channel
-started on a math stack that could be used to make math function better in future
-keys are stored in text files on local machine but not uploaded to github so if you need examples please ask!

The bot is meant for simple commands using the $ prefix to issue commands to the bot inside the discord server. It's just a 
personal project meant for messing around and seeing how well it all works. Currently uses 5 APIs total for running the bot, providing jokes,trivia questions, gifs, and songs played through the voice channel in the server(Keep in mind the bot needs to have administrative rights in your server for some of this functionality to work properly). 

They can be found at:
https://icanhazdadjoke.com
https://opentdb.com/
http://discordpy.readthedocs.io/en/latest/api.html
https://developers.gfycat.com/
https://developers.google.com/youtube/

The bot also uses youtube links to play video audio over voice chat to users in a specific channel which works great when hosted on a 
desktop. The plan is to hopefully host this bot on my raspberry pi server at home but it will depend on how costly the encoding is on the
pi (would like to avoid overheating). 

Ideas for future implementation & necessary fixes:
- Need to fix/change when the bot is activated by one user, be able to cancel that order and also be able to progress that command from any user in the server.
- Sound playback doesn't like to stop if $stop command is issued by someone other than the issuer of the original $play command.(fixed)
- Hard exit of the server lags slightly (bot doesn't disconnect instantly). 
- Bot listens to all text channels (would like to make it specific to only one)
- Need to clean up the code (make alot of helper functions)

- Add gif api support, scan user input (any input even chat between users) and use keywords from input to search a gif api for related gifs. if something is relatable, post the gif, otherwise stay quiet. (Added gif search function, need to write text listener to conversations of users in discord).
- Standbye/on hold mode needs to be implemented. 
- Provide information on the host itself (temperature, date, time)
