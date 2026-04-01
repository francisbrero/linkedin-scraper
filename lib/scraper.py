from openai import OpenAI
import base64
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Generate a detailed outline of the video
openai_api_key = os.getenv('OPENAI_API_KEY')
if openai_api_key is None:
    raise ValueError("OPENAI_API_KEY environment variable not set")
client = OpenAI()


def encode_image(image_path):
  with open(image_path, "rb") as image_file: 
    return base64.b64encode(image_file.read()).decode('utf-8') 

base64_image = encode_image('data/linkedin.png')

response = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {
      "role": "system",
      "content": [
        {
          "type": "text",
          "text": """
            You are a sales rep for MadKudu.
            Please extract the most important facts about this lead.

            Respond in the JSON format.
          """
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/png;base64,{base64_image}"
          }
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "Here are the most important facts about this lead:"
        }
      ]
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response.choices[0].message.content)