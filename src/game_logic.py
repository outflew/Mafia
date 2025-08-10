from random import choice
import random
from time import sleep
from collections import Counter
import os
from pathlib import Path
import glob

import audio
import player

def mostFrequent(List):
    occurence_count = Counter(List)
    most_common = occurence_count.most_common()
    if len(most_common) > 1 and most_common[0][1] == most_common[1][1]:
        print("Its a tie, chadGPT will randomly choose someone to kill")
        sleep(1)
        return random.choice([most_common[0][0], most_common[1][0]])
    else:
        return most_common[0][0]


def wait(t):
    sleep(t)


def countdown(t):
    for i in range(t+1):
        print(t-i)
        audio.playAudio(audio.POP)


def clear():
    print("\033c", end="")


def printPlayerList(list, exception=None):
    for i in range(len(list)):
        if list[i].role == exception:
            print(str(i+1) + ") " + list[i].name + " (YOU)")
        else:
            print(str(i+1) + ") " + list[i].name)


def checkIfDead():
    for i in range(livingPlayers):
        if livingPlayers[i].isAlive == False:
            return livingPlayers[i].name
            # Assuming 1 player MAX dies each night


def eliminate(playerNumber): 
    livingPlayers[playerNumber-1].die()
    livingPlayers.remove(livingPlayers[playerNumber-1])

# Functions

def hasGameEnded():
    global winningTeam
    if badTeamNumber == 0:
        winningTeam = "Good"
        return True
    elif goodTeamNumber == badTeamNumber:
        winningTeam = "Bad"
        return True
    else:
        return False
    # Check to see if game ended

def intro():
    files = glob.glob('assets\\plrNames\\*')
    for f in files:
        os.remove(f)
    clear()
    print("Welcome to Mafia! I am your host ChadGPT.")
    audio.playAudio(audio.WELCOME)
    
    
    playerNumber = int(input("How many players are there (minimum 4)? "))
    global goodTeamNumber 
    goodTeamNumber = playerNumber - 1

    global badTeamNumber 
    badTeamNumber = 1

    for i in range(playerNumber):
        plrName = input("Enter name of player #" + str(i+1) + " ")
        #nameAudio = audio.textToSpeech(plrName, "plr_" + plrName)
        plrObject = player.Player(name=plrName, role="Civilian", team="Good", isAlive=True, audioFile=None) #nameAudio)
        players.append(plrObject)
        livingPlayers.append(plrObject)
        clear()

    for i in livingPlayers:
        audio.textToSpeech(i.name, f'{i.name}_tts')
        audio.convertToWav(str(Path(f'assets\\plrNames\\{i.name}')))
        os.remove(str(Path(f'assets\\plrNames\\{i.name}_tts.mp3')))
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
        #players[i].sayName()
        audio.playAudio(f"assets\\plrNames\\{players[i].name}_tts.wav")
        audio.playAudio(f"assets\\audio\\role.wav")
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
    audio.playAudio(audio.INTRO)
    wait(3)
    countdown(0)

def night():
    clear()
    print("The night approached... Everyone falls asleep")
    audio.playAudio(audio.GOODNIGHT)
    wait(5)
    print("While everyone else is fast alseep... the mafia wakes up. The mafia chooses who to eliminate tonight.")
    audio.playAudio(audio.MAFIA)
    wait(1)
    print()
    print("List of players:")
    printPlayerList(livingPlayers, "Mafia")

    print()
    #------------- changes by ali
    try:
        victimNum = int(input("Enter the NUMBER of the player you want to eliminate: "))
        victim = livingPlayers[victimNum-1]
        victim.die()
        print(victim.name + " had been attacked!")
        wait(2)
        print("Mafia go back to sleep")
        audio.playAudio(audio.MAFIA_SLEEP)
        wait(4)
        # MAFIA STAGE
    except Exception as e:
        print(e)
    
    clear()


    print("Soon after... The doctor wakes up. The doctor chooses who to heal tonight.")
    audio.playAudio(audio.DOCTOR)
    wait(1)
    print()
    print("List of players:")
    printPlayerList(livingPlayers, "Doctor")
    print()
    healedNum = int(input("Enter the NUMBER of the player you want to heal: "))
    healed = livingPlayers[healedNum-1]
    healed.heal()
    print(healed.name + " had been healed!")
    wait(2)
    print("Doctor go back to sleep.")
    audio.playAudio(audio.DOCTOR_SLEEP)
    wait(4)
    # DOCTOR STAGE

    clear()

    print("Then... The detective wakes up. The detective chooses who to investigate tonight.")
    audio.playAudio(audio.DETECTIVE)
    wait(1)
    print()
    print("List of players:")
    printPlayerList(livingPlayers, "Detective")

    print()
    investigatedNum = int(input("Enter the NUMBER of the player you want to investigate: "))
    investigated = livingPlayers[investigatedNum-1]
    print(investigated.name + " had been investigated!")
    investigated.reveal()
    wait(2)
    print("The detective goes back to sleep.")
    audio.playAudio(audio.DETECTIVE_SLEEP)
    wait(4)
    # DETECTIVE STAGE
    movePlayer = None
    for i in range(len(livingPlayers)):
        currentPlayer = livingPlayers[i]
        if currentPlayer.isAlive == False:
            movePlayer = currentPlayer

    if movePlayer != None:
        livingPlayers.remove(movePlayer)
        deadPlayers.append(movePlayer)
        
        if movePlayer.team == "Bad":
            global badTeamNumber
            badTeamNumber -= 1
        elif movePlayer.team == "Good":
            global goodTeamNumber
            goodTeamNumber -= 1
    
    # Moves dead player to correct list
    clear()
    

def announcement():
    wait(1)
    audio.playAudio(audio.GOODMORNING)
    print("Good morning everyone!")
    wait(2)
    if len(deadPlayers) == 0:
        print("Luckly, no players died.")
    else:
        print("Unfortunately, the following players are no longer alive:")
        audio.playAudio(audio.ANNOUNCEMENT)
        printPlayerList(deadPlayers)
        for i in deadPlayers:
            audio.playAudio(f"assets\\plrNames\\{i.name}_tts.wav")
        wait(4)


def day():
    print("You have 30 seconds to discuss who you think is the Mafia!")
    audio.playAudio(audio.DISCUSS)
    wait(2)
    countdown(30)

def vote():
    print("Times up! Now you must vote on which player to execute!")
    audio.playAudio(audio.VOTE)
    wait(1)
    while True:
        try:
            for i in range(len(livingPlayers)):
                print(livingPlayers[i].name + " choose who to vote.")
                print("List of players:")
                printPlayerList(livingPlayers)
                audio.playAudio(f"assets\\plrNames\\{livingPlayers[i].name}_tts.wav")
                audio.playAudio("assets\\audio\\voting.wav")
                vote = input("Enter the NUMBER of the player you want to vote: ")
                votedNum = int(vote)
                voted.append(votedNum)
                wait(2)
                clear()
            break
        except Exception as e:
            print(e)
            print("invalid input")
            continue
    

def execution():
    print("It's execution time! The player being executed is...")
    audio.playAudio(audio.EXECUTION)
    executedPlayer = livingPlayers[mostFrequent(voted)-1]
    print(executedPlayer.name)
    audio.playAudio(f"assets\\plrNames\\{executedPlayer.name}_tts.wav")
    executedPlayer.die()
    movePlayer = None
    for i in range(len(livingPlayers)):
        currentPlayer = livingPlayers[i]
        if currentPlayer.isAlive == False:
            movePlayer = currentPlayer

    if movePlayer != None:
        livingPlayers.remove(movePlayer)
        deadPlayers.append(movePlayer)
        
        if movePlayer.team == "Bad":
            global badTeamNumber
            badTeamNumber -= 1
        elif movePlayer.team == "Good":
            global goodTeamNumber
            goodTeamNumber -= 1
    wait(5)

def endGame():
    print("THE " + str(winningTeam) + " TEAM HAS WON!!!")

# Procedures

badTeamNumber = 0
goodTeamNumber = 0
winningTeam = ""
# Variables


players = []
livingPlayers = []
deadPlayers = []
voted = []

# Arrays