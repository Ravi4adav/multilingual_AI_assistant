import speech_recognition as sr
from src.exceptions import CustomException
import sys
import streamlit as st


class speech_to_text:
    def __init__(self):
        self.recognizer=sr.Recognizer()

    def get_speech(self):
        with sr.Microphone() as mic:
            print("Please wait, adjusting Background Noise...")
            st.write("Please wait, adjusting Background Noise...")
            self.recognizer.adjust_for_ambient_noise(mic, duration=2)
            
            print("Listening... Speak Now!")
            st.write("Listening... Speak Now")

            try:
                # Listen for speech and converting to text
                self.audio=self.recognizer.listen(mic)
                print("Processing...")
                st.write("Processing...")
                # Recognize speech using Google Web Speech API
                self.text = self.recognizer.recognize_google(self.audio)

                return self.text
            except sr.UnknownValueError:
                print("Sorry, I could not understand the audio.")

            except Exception as e:
                raise CustomException(e, sys)

