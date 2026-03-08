import pandas as pd
from supabase import create_client

# Your Supabase Keys
url = "YOUR_SUPABASE_URL"
key = "YOUR_SUPABASE_KEY"
supabase = create_client(url, key)

def upload_bible():
    # Load your CSV (adjust filename to what you downloaded)
    df = pd.read_csv('t_kjv.csv') 
    
    # We loop through and send the data to Supabase
    for index, row in df.iterrows():
        data = {
            "book_name": "John", # You'll need a mapping for book numbers to names
            "chapter": row['c'],
            "verse": row['v'],
            "kjv_text": row['t']
        }
        supabase.table("bible_verses").insert(data).execute()
        print(f"Uploaded {row['c']}:{row['v']}")

# run it once
# upload_bible()
