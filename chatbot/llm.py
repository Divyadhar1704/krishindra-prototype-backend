import os

from dotenv import load_dotenv
from openai import OpenAI


class LLM:

    def __init__(self):

        load_dotenv()

        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=os.getenv("OPENROUTER_API_KEY")
        )

    def generate(self, prompt):

        response = self.client.chat.completions.create(

            model="openai/gpt-oss-20b:free",

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.3,
        )

        text = response.choices[0].message.content

        if text:
            text = text.replace("\\n", "\n")

        return text