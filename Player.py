
class Player:
    def __init__(self):
        self.name = "youtube player"
        self.voice = None
        self.player = None
        self.volume = None
        self.userList = []
    
    def addPlayer(self, player):
        self.player = player

    def addVoice(self, voice):
        self.voice = voice

    def getVoice(self):
        return self.voice