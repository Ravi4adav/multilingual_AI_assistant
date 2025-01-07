## Question/Answer System
- It is a simple assistant which uses <**Gemini 1.5 pro**> LLM model for query retrieval.

## How to Use
- Simply press **Ask Query** button and ask question when prompt show **Listening.. Speak Now!**

## How to setup
- Create python virtual environment.
        
        virtualenv ./venv

- Activate environment

        - cd ./venv/Scripts
        - activate

- Now get back from the virtual environment directory

        - cd ../..

- Run application at local device

        - streamlit run app.py


## Requirements
- User must setup <**.env**> file in the directory where app.py file is present.

- Create **GEMINI** model API key and paste inside <**.env**> file as following typecase:

        GEMINI_API_KEY="YOUR API KEY"



