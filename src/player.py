class Player:
    def __init__(self, name, role, team, isAlive, audioFile):
        self.name = name
        self.role = role
        self.team = team
        self.isAlive = isAlive
        self.audioFile = audioFile

    def die(self):
        self.isAlive = False

    def heal(self):
        if self.isAlive == False:
            self.isAlive = True

    def reveal(self):
        print(self.name + " is " + self.team)

    #def sayName(self):
    #    newAudio = audio.convertToWav(inputFile=self.audioFile, newName=self.name + ".wav")
    #    audio.playAudio(audio.newAudio)

# Player Object