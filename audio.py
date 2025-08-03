from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play 

# Import an audio file 
# Format parameter only
# for readability 
#detective_file = AudioSegment.from_file(file = "audio/goodnight.mp3", format = "mp3") 
                                  
#GOODMORNING = AudioSegment.from_file(file = "audio/morning.wav", format = "wav")

# Play the audio file
#play(GOODMORNING)
#print("EEEEEEEEEEEEEE")
#play(detective_sleep_file)
#print("EEEEEEEEEEEEEE")

def convertToWav(inputFile, newName):
    # Load your MP3 file
    audio = AudioSegment.from_mp3(inputFile)

    outputFile = audio.export(newName, format="wav")
    # Export as WAV
    return outputFile


def playAudio(audioFile):
    file = AudioSegment.from_file(file = audioFile, format = "wav")
    play(file)
    


def textToSpeech(text, filename):
    tss = gTTS(text, lang='en', tld="co.uk")
    return tss.save(filename + ".mp3")


#textToSpeech("Good Morning everyone!", "goodmorning")
#goodmorningWav = convertToWav(goodmorning, "goodmorning.wav")

#playAudio(goodmorningWav)

#file = textToSpeech("The game has begun! You Have 15 seconds to talk before night!", "intro")
#wavFile = convertToWav(file, "intro.wav")

#playAudio(wavFile)


#POP = "C:\\Users\\hashi\\OneDrive\\Documents\\Mafia\\audio\\pop.mp3"
#GOODNIGHT = "C:\\Users\\hashi\\OneDrive\\Documents\\Mafia\\audio\\goodnight.mp3"
#MAFIA = "C:\\Users\\hashi\\OneDrive\\Documents\\Mafia\\audio\\mafia.mp3"
#MAFIA_SLEEP = "C:\\Users\\hashi\\OneDrive\\Documents\\Mafia\\audio\\mafia_sleep.mp3"

#playsound(POP)