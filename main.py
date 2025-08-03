from gtts import gTTS
from random import choice
from time import sleep
# Libraries

import audio
import app
# Modules

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
        self.isAlive = True

    def reveal(self):
        print(self.name + " is " + self.team)

    def sayName(self):
        newAudio = audio.convertToWav(inputFile=self.audioFile, newName=self.name + ".wav")
        audio.playAudio(newAudio)

# Player Object

def wait(t):
    sleep(t)

def eliminate(playerNumber): 
    livingPlayers[playerNumber-1].die()
    livingPlayers.remove(livingPlayers[playerNumber-1])

def countdown(t):
    for i in range(t+1):
        print(t-i)
        audio.playAudio(POP)

# Functions


def clear():
    print("\033c", end="")

def intro():
    for i in range(playerNumber):
        plrName = input("Enter name of player #" + str(i+1) + " ")
        nameAudio = audio.textToSpeech(plrName, "plr_" + plrName)
        plrObject = Player(name=plrName, role="Civilian", team="Good", isAlive=True, audioFile=nameAudio)
        players.append(plrObject)
        livingPlayers.append(plrObject)


    clear()

    #Adds every player to the array of players and sets them as civilian by default

    mafiaPlayer = choice(players)
    mafiaPlayer.role = "Mafia"
    mafiaPlayer.team = "Bad"

    # Chooses Player as mafia

    doctorPlayer = None
    while True:
        doctorPlayer = choice(players)
        if doctorPlayer.role != "Mafia":
            break

        
    doctorPlayer.role = "Doctor"

    # Chooses Player as doctor


    detectivePlayer = None
    while True:
        detectivePlayer = choice(players)
        if detectivePlayer.role != "Mafia" and detectivePlayer.role != "Doctor":
            break

    detectivePlayer.role = "Detective"

    # Chooses Player as detective

    for i in range(playerNumber):
        wait(1)
        players[i].sayName()
        #audio.playAudio("plr_" + players[i].name + ".mp3")
        input(players[i].name + " Press Enter to check your role ")
        wait(1)
        print("You are " + players[i].role)
        wait(1)
        input("Press Enter to clear")
        wait(1)
        clear()

    # Shows each player their role seperately

    print("The game has begun!")
    print("You Have 15 seconds to talk before night!")
    audio.playAudio(INTRO)
    wait(3)
    #countdown(15)

def night():
    clear()
    print("The night approached... Everyone falls asleep")
    audio.playAudio(GOODNIGHT)
    wait(5)
    print("While everyone else is fast alseep... the mafia wakes up. The mafia chooses who to eliminate tonight.")
    audio.playAudio(MAFIA)
    wait(5)
    print()
    print("List of players:")
    for i in range(len(livingPlayers)):
        if livingPlayers[i].role == "Mafia":
            print(str(i+1) + ") " + livingPlayers[i].name + " (YOU)")
        else:
            print(str(i+1) + ") " + livingPlayers[i].name)

    print()
    num = int(input("Enter the NUMBER of the player you want to eliminate: "))
    livingPlayers[num-1].die()
    print(livingPlayers[num-1].name + " had been attacked!")
    wait(2)
    print("Mafia go back to sleep")
    audio.playAudio(MAFIA_SLEEP)
    wait(5)
    # MAFIA STAGE
    
    clear()


    print("Soon after... The doctor wakes up. The doctor chooses who to heal tonight.")
    audio.playAudio(DOCTOR)
    wait(5)
    print()
    print("List of players:")
    for i in range(len(livingPlayers)):
        if livingPlayers[i].role == "Doctor":
            print(str(i+1) + ") " + livingPlayers[i].name + " (YOU)")
        else:
            print(str(i+1) + ") " + livingPlayers[i].name)

    print()
    num = int(input("Enter the NUMBER of the player you want to heal: "))
    livingPlayers[num-1].heal()
    print(livingPlayers[num-1].name + " had been healed!")
    wait(2)
    print("Doctor go back to sleep.")
    audio.playAudio(DOCTOR_SLEEP)
    wait(5)
    # DOCTOR STAGE

    clear()

    print("Then... The detective wakes up. The detective chooses who to investigate tonight.")
    audio.playAudio(DETECTIVE)
    wait(5)
    print()
    print("List of players:")
    for i in range(len(livingPlayers)):
        if livingPlayers[i].role == "Detective":
            print(str(i+1) + ") " + livingPlayers[i].name + " (YOU)")
        else:
            print(str(i+1) + ") " + livingPlayers[i].name)

    print()
    num = int(input("Enter the NUMBER of the player you want to investigate: "))
    print(livingPlayers[num-1].name + " had been investigated!")
    livingPlayers[num-1].reveal()
    wait(2)
    print("The detective goes back to sleep.")
    audio.playAudio(DETECTIVE_SLEEP)
    wait(5)
    # DETECTIVE STAGE

    #livingPlayers.remove(livingPlayers[playerNumber-1])

def check():
    if badTeamNumber == 0:
        winningTeam = "Good"
        endGame = True
    elif badTeamNumber == goodTeamNumber:
        winningTeam = "Bad"
        endGame = True

def announcement():
    clear()
    audio.playAudio(MORNING)
    print("Good morning everyone!")

def day():
    pass

def vote():
    pass

def execution():
    pass

# Procedures
WELCOME = "audio\welcome.wav"
INTRO = "audio\intro.wav"
POP = "audio\pop.wav"
MORNING = "audio\morning.wav"

GOODNIGHT = "audio\goodnight.wav"
GOODMORNING = "audio\goodmorning.wav"
MAFIA = "audio\mafia.wav"
MAFIA_SLEEP = "audio\mafia_sleep.wav"

DOCTOR = "audio\doctor.wav"
DOCTOR_SLEEP = "audio\doctor_sleep.wav"

DETECTIVE = "audio\detective.wav"
DETECTIVE_SLEEP = "audio\detective_sleep.wav"

# Audio Constants

badTeamNumber = 0
goodTeamNumber = 0
winningTeam = ""
endGame = False
# Variables


players = []
livingPlayers = []

# Arrays

if __name__ == "__main__": 
    clear()
    print("Welcome to Mafia! I am your host ChatGPT.")
    audio.playAudio(WELCOME)
    playerNumber = int(input("How many players are there (minimum 4)? "))
    intro()
    #while not endGame:
    #night()
    #announcement()
    #check()
    #day()
    #vote()
    #execution()
    #check()