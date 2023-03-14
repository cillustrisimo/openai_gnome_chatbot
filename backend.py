import openai
from dotenv import load_dotenv
import os

load_dotenv()


class Chatbot:
    def __init__(self):
        openai.api_key = os.getenv("API_KEY")

    def get_response(self, user_input):
        response = openai.ChatCompletion.create(
            messages=[{"role": "system", "content": """You are a whimsical gnome named Mr. Sneed. You reply with a 
                constant sense of wonder and mischief. Every reply and explanation you make is whimsical and divested 
                from reality. You begin each reply with either: sneedle dee, sneedle doo, or sneedle dum.
                You also randomly say sneedy-wee throughout each sentence."""},
                      {"role": "user", "content": f"{user_input}"}],
            model="gpt-3.5-turbo",
            max_tokens=4000,
            temperature=0.5
        )
        response = response['choices'][0]['message']['content']
        return response


if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("Say a joke about politics")
    print(response)
