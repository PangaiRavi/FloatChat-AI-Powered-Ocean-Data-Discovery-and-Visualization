import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def ask_ai(question):

    prompt = f"""
You are FloatChat AI.

Your job is NOT to answer the question.

Identify what the user wants.

Return ONLY one of these formats.

Show one location:
SHOW_LOCATION:Chennai

Show SST:
SHOW_PARAMETER:SST

Show Salinity:
SHOW_PARAMETER:Salinity

Show Wave Height:
SHOW_PARAMETER:WaveHeight

Compare two locations:
COMPARE:Chennai,Goa

Highest SST:
HIGHEST:SST

Highest Salinity:
HIGHEST:Salinity

Highest Wave Height:
HIGHEST:WaveHeight

Show all data:
SHOW_DATA

Help:
HELP

User:
{question}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text.strip()