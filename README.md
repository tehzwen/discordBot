discordBot

The bot is meant for simple commands using the $ prefix to issue commands to the bot inside the discord server. It's just a 
personal project meant for messing around and seeing how well it all works. Currently uses APIs for running the bot, providing jokes,trivia questions, gifs, and songs played through the voice channel in the server(Keep in mind the bot needs to have administrative rights in your server for some of this functionality to work properly). Keys are stored in text files on local machine but not uploaded to github so if you need examples please ask!

They can be found at:
- https://icanhazdadjoke.com
- https://opentdb.com/
- http://discordpy.readthedocs.io/en/latest/api.html
- https://developers.gfycat.com/
- https://developers.google.com/youtube/
- https://developers.google.com/maps/
- http://www.rrrather.com/
- https://dev.mysql.com/ (documentation on the MySQL server, currently running Rasbian Stretch on the RPI and database is a MariaDB)


V0.04 WORK IN PROGRESS Feb 23, 2018



Additions:
- youtube video searching, reddit image searching, mysql database for handling points systems for users on server, gambling, blackjack and slots have all been added for gaining and spending points as well as a standings menu to list the scores of all users on the server, google maps integration for looking up locations using description or coordinates, and would you rather questions for conversation starters.
- Andy Yip is now working on the project with me. Worked on the maps, gambling mechanics and would you rather API integration.
- RPI server has heatsinks and fans now, sitting at a nice cool 40C while running the bot and other services.

Bug fixes:
- Trivia now awards points for correct answers and answers are no longer case sensitive(C == c).
- Infinite loops no longer occur when $TTS command is issued with no arguments.
- Most commands now follow the structure of $command argument. (example: $TTS "hey there" will issue a TTS message of hey there (no need for quotes when using the bot).
- Negative and empty bets aren't rewarded with points (but empty can be used for debugging).

Ideas for future implementation & necessary fixes:
- Server has been randomly terminating the python script once in a while. 
- Need to clean up the code (make alot of helper functions).
- Add gif api support, scan user input (any input even chat between users) and use keywords from input to search a gif api for related gifs. if something is relatable, post the gif, otherwise stay quiet. (Added gif search function, need to write text listener to conversations of users in discord).
- Standbye/on hold mode needs to be implemented. 
- Provide information on the host itself (temperature, date, time).
- Points trading and gifting.
