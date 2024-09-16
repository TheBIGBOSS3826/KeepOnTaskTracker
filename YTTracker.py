#  This  project tracks how long I am on Youtube for on my computer.
"""
Goal: Automatically Track Time spent on apps or sites

differientiate between sites

Time on email and time on code
"""

import time
import pygame
import os

# Update 6/21/24 we just worked on the audio file and now we have incorporate the audio into our code.
# We also have to beef up the audio file. I would like to know how we can finesse the file paths and then
# handle exceptions with the possibility of downloading multiple of the same type of files.
# We also need to better understand the code that we have.

audioSounds = [
    r'C:\NewChomeApp\“Daddy Chill”  Meme.mp3', 
    r'C:\NewChomeApp\🛠️ Get back to work! themaryburke.mp3', 
    r'C:\NewChomeApp\Get back to work 🔥 keepsupporting.mp3'
    ]
# Pass in filepath as an argument  and then audioSounds will be passed in during defCount
def sound(filepath):
    # Initialize pygame mixer
    pygame.mixer.init()

# Load the audio file
    pygame.mixer.music.load(filepath)

# Play the audio file
    pygame.mixer.music.play()

def count(tracking, label, sound, audioSounds):
    elapsedTime = 0
    
    try:
        # We changed this to [0] this allows tracking to access the mutable surface.
        while tracking[0]:
            time.sleep(1)
            elapsedTime += 1 
            if elapsedTime == 600:
                label.text = "Get off Youtube"
                sound(audioSounds[0])
            elif elapsedTime == 1200:
                label.text = "This is your last warning"
                sound(audioSounds[1])
            elif elapsedTime == 1800:
                label.text = "Get off Youtube we need to get to work!"
                sound(audioSounds[2])
                os.system("taskkill /im chrome.exe /f")
                time.sleep(10)
                break
            else:
                print(elapsedTime)
    except KeyboardInterrupt:
        label.text = "The program has been manually interrupted!"
        pygame.mixer.music.stop()  # Ensure audio stops
    except SystemExit:
        label.text = "The program has been closed!"
        pygame.mixer.music.stop()  # Ensure audio stops
    if elapsedTime % 60 == 0:
        label.text = f"The program ran for {elapsedTime//60} minutes!"
    else:
        label.text = f"The program ran for {elapsedTime} seconds!"


#It seems the terminal only displays a certain amount of lines.
