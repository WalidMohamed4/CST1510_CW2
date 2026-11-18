import requests
import pandas as pd

URL = "https://api.github.com/orgs/python/repos"
PARAMS = {"per_page": 100}
RECORDS_KEY = None

response = requests.get(URL, params=PARAMS)
response.raise_for_status()
data = response.json()

records = data if RECORDS_KEY is None else data[RECORDS_KEY]

df = pd.json_normalize(records)
df.to_csv("DATA/raw.csv", index=False)

print(f"Saved {len(df)} rows and {len(df.columns)} columns to DATA/raw.csv")