import openai
from dotenv import load_dotenv
import os

load_dotenv()


class Chatbot:
    def __init__(self):
        openai.api_key = os.getenv("API_KEY")

    def get_response(self, user_input):
        response = openai.ChatCompletion.create(
            messages=[{"role": "system", "content": """You are a whimsical gnome named Mr. Sneed. 
            Every reply and explanation you make is whimsical and divested from reality. You are judgemental when you respond.
            You give unclear responses. You may begin each reply with either: sneedle dee, sneedle doo, or sneedle dum.
                You randomly say variations of sneed in sentences."""},
                      {"role": "user", "content": user_input}],
            model="gpt-3.5-turbo",
            max_tokens=3800,
            temperature=0.9
        )
        response = response['choices'][0]['message']['content']
        return response


if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("Say a joke about politics")
    print(response)
