from groq import Groq
from dotenv import load_dotenv
import logging
import os

# load api key from .env
load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")
if not API_KEY:
     raise ValueError("API key not found. Make sure GROQ_API_KEY is set in .env")
# Initialize Groq client
client = Groq(api_key=API_KEY)


messages = [
         {
        "role": "system",
        "content": (
            "You are a chatbot. "
            "You MUST NOT use headings, titles, topics, bullet points, or labels. "
            "Respond in plain sentences only. "
            "If you include headings or topic names, it is an error."
        )
         }
]
def send_ai(content):
              logging.info("send content to ai")
                
                #Send file content to AI for summarization 
              messages.append({"role":"user",
                             "content":f"Please summarize this content:\n{content}"})

        
    # Call the agent with streaming enabled
              completion = client.chat.completions.create(
            model="openai/gpt-oss-120b",  # replace if your agent is different
            messages = messages,
            temperature=1,
            max_completion_tokens=8192,
            top_p=1,
            reasoning_effort="medium",
            stream=False
            )
    # Extract and print the AI's answer
              ai_response = completion.choices[0].message.content

              messages.append({"role":"assistant", "content" :ai_response })
              return ai_response