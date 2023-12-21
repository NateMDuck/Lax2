import random
import time

from gtts import gTTS
import os

list_side = [' right', ' left']

list_moves =[' shift', ' double shift', ' triple shift',
            ' roll dodge', ' question mark dodge',
            ' face dodge', ' split dodge', ' bull dodge']

list_shots = [' high', ' side', ' low']

list_goal = [' right upper ninety', ' left upper ninety',
             ' right lower ninety', ' left lower ninety', ' nutmeg']



list_statistics = []

#move = random.choice(list_moves)

def text_to_speech(text):
    # Initialize gTTS with the text to convert
    speech = gTTS(text)

    # Save the audio file to a temporary file
    speech_file = 'speech.mp3'
    speech.save(speech_file)

    # Play the audio file
    os.system('afplay ' + speech_file)

#num_rounds = int(input("Enter a number"))

for i in range(2):

    move = random.choice(list_side)
    move = move + " " + random.choice(list_moves)
    text_to_speech(move)

    list_statistics.append(move)

    time.sleep(1.0)


    shot = random.choice(list_side)
    shot = shot + " " + random.choice(list_shots) + " " + random.choice(list_goal)
    text_to_speech(shot)

    list_statistics.append(shot)

print(list_statistics)
