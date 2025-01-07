import speech_recognition as sr
from src.exceptions import CustomException
import sys
import streamlit as st
from src.logger import logging


class speech_to_text:
    def __init__(self):
        self.recognizer=sr.Recognizer()

    def get_speech(self):
        with sr.Microphone() as mic:
            logging.info("Adjusting Background Noise parameters...")
            print("Please wait, adjusting Background Noise...")
            st.write("Please wait, adjusting Background Noise...")
            self.recognizer.adjust_for_ambient_noise(mic, duration=2)
            logging.info("Adjusting Background Noise parameter adjusted successfully!")
            
            print("Listening... Speak Now!")
            st.write("Listening... Speak Now")

            try:
                logging.info("Listening voice query...")
                # Listen for speech and converting to text
                self.audio=self.recognizer.listen(mic)
                logging.info("Processing Query--> Speech to Text...")
                print("Processing...")
                st.write("Processing...")
                # Recognize speech using Google Web Speech API
                self.text = self.recognizer.recognize_google(self.audio)
                logging.info("Speech to text Generated Successfully!")

                return self.text
            except sr.UnknownValueError:
                logging.info("Failed to Understand Voice!")
                print("Sorry, I could not understand the audio.")

            except Exception as e:
                logging.info("Speech to text Generation Failed!")
                raise CustomException(e, sys)

