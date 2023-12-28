import pandas as pd
from faker import Faker
import random

fake = Faker()

# Function to generate a synthetic diary entry
def generate_diary_entry():
    date = fake.date_this_decade()
    entry = fake.paragraphs(nb=random.randint(5, 10))
    return {"Date": date, "Entry": entry}

# Generate 100 synthetic diary entries
entries = [generate_diary_entry() for _ in range(100)]

# Create a DataFrame and save it to a CSV file
df = pd.DataFrame(entries)
df.to_csv("diary_entries.csv", index=False)
