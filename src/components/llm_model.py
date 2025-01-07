import google.generativeai as genai
from dotenv import load_dotenv
import os
import sys
from src.exceptions import CustomException

load_dotenv()

GEMINI_KEY=os.getenv("GEMINI_API_KEY")

class Model:
    def __init__(self):
        genai.configure(api_key=GEMINI_KEY)

    def generate_response(self, query):
        try:
            self.query=query
            self.model = genai.GenerativeModel("gemini-1.5-pro")
            self.response = self.model.generate_content(self.query, 
                                    generation_config = genai.GenerationConfig(
                                    max_output_tokens=1500,
                                    temperature=0.1,
                                    )
                            )
            return self.response.text
        except Exception as e:
            raise CustomException(e,sys)
