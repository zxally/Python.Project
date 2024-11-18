import speech_recognition as sr
import pyttsx3
import pygame
import random
import os

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Initialize the pygame mixer
pygame.mixer.init()

# Function to speak a given text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech
def recognize_speech():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not get that.")
            return ""
        except sr.RequestError:
            speak("Request error from Google Speech Recognition service")
            return ""

# Function to play music
def play_music(song):
    try:
        if os.path.exists(song):
            pygame.mixer.music.load(song)
            pygame.mixer.music.play()
            speak(f"Playing {os.path.basename(song)}")
        else:
            speak(f"{os.path.basename(song)} not found.")
    except Exception as e:
        speak(f"Unable to play {os.path.basename(song)}")
        print(e)

# Function to pause music
def pause_music():
    pygame.mixer.music.pause()
    speak("Music paused")

# Function to resume music
def resume_music():
    pygame.mixer.music.unpause()
    speak("Music resumed")

# Function to stop music
def stop_music():
    pygame.mixer.music.stop()
    speak("Music stopped")

# Function to shuffle and play random music
def shuffle_music(directory):
    try:
        songs = [os.path.join(directory, song) for song in os.listdir(directory) if song.endswith('.mp3')]
        if songs:
            random_song = random.choice(songs)
            play_music(random_song)
        else:
            speak("No music files found in the directory.")
    except Exception as e:
        speak("Unable to shuffle music")
        print(e)

# Function to process voice commands
def process_command(command, music_directory):
    if "play" in command:
        song = command.replace("play", "").strip()
        if song:
            play_music(os.path.join(music_directory, song + '.mp3'))
        else:
            speak("Please specify a song name after 'play'")
    elif "pause" in command:
        pause_music()
    elif "resume" in command:
        resume_music()
    elif "stop" in command:
        stop_music()
    elif "shuffle" in command:
        shuffle_music(music_directory)
    else:
        speak("Command not recognized")

# Main function
def main():
    music_directory = r'C:\Users\Mean.Un\Desktop\Python.Project\Music_Voice_Control_By_Py\music'
    print(f"Using music directory: {music_directory}")

    # Example songs for testing
    print("Example songs to test: Unstoppable.mp3, Love Me Like You Do.mp3, Let Her Go.mp3, I Like Me Better.mp3, Calm Down.mp3")

    while True:
        command = recognize_speech()
        if command:
            process_command(command, music_directory)

if __name__ == "__main__":
    main()
