import google.generativeai as genai
from dotenv import load_dotenv
import os
import sys
from src.exceptions import CustomException
from src.logger import logging

load_dotenv()

GEMINI_KEY=os.getenv("GEMINI_API_KEY")

class Model:
    def __init__(self):
        genai.configure(api_key=GEMINI_KEY)

    def generate_response(self, query):
        try:
            self.query=query
            logging.info("Initiating Response Generation...")
            self.model = genai.GenerativeModel("gemini-1.5-pro")
            self.response = self.model.generate_content(self.query, 
                                    generation_config = genai.GenerationConfig(
                                    max_output_tokens=1500,
                                    temperature=0.1,
                                    )
                            )
            logging.info("Response Generated Successfully!")
            return self.response.text
        except Exception as e:
            logging.info("Response Generation Failed!")
            raise CustomException(e,sys)