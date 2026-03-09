import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

prompt = open("../prompts/odin_symbolic_test.md").read()

response = client.responses.create(
    model="gpt-4.1",
    input=prompt,
    temperature=0.5
)

print(response.output_text)
