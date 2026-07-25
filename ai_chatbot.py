from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "user", "content": "Hello"}
    ]
)

print(response.choices[0].message.content)


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

If the user asks to compare two locations, return ONLY:

COMPARE:Location1,Location2

Example:

COMPARE:Chennai,Mumbai

Do not explain anything else.

If the user asks:
- Which location is safest?
- Safest place
- Safe location

Return ONLY:

SAFEST

If the user asks:
- help
- what can you do
- commands
- examples
- how to use

Return ONLY:

HELP
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
       ]
    )

    return response.choices[0].message.content

    return response.text.strip()
