#openAI-diary-generator
import openai
import pandas as pd
from faker import Faker

fake = Faker()

# Set your OpenAI GPT-3 API key
api_key = "redacted"
openai.api_key = api_key

# Function to generate a synthetic diary entry using GPT-3
def generate_diary_entry(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.7,
        max_tokens=200,
        n=1,
        stop=None,
    )
    return response.choices[0].text.strip()

# Generate 100 synthetic diary entries using GPT-3
entries = [generate_diary_entry("Dear Diary, " + fake.paragraph()) for _ in range(10)]

# Create a DataFrame and save it to a CSV file
df = pd.DataFrame(entries, columns=["Entry"])
df.to_csv("diary_entries_gpt3.csv", index=False)
