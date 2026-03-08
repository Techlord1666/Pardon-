import os
import time
from dotenv import load_dotenv
from supabase import create_client
from faster_whisper import WhisperModel
import speech_recognition as sr
import io
from parser import parse_bible_reference

load_dotenv()

# Initialize Supabase
supabase = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))

# Initialize Whisper (using 'base' for speed)
model = WhisperModel("base", device="cpu", compute_type="int8")
recognizer = sr.Recognizer()
mic = sr.Microphone()

def update_screen(ref_obj):
    # For a real production app, you'd query your Bible DB here.
    # For this demo, we'll simulate the text lookup.
    verse_text = f"Simulated text for {ref_obj['book']} {ref_obj['chapter']}:{ref_obj['verse']}"
    
    supabase.table("display_state").update({
        "reference": f"{ref_obj['book']} {ref_obj['chapter']}:{ref_obj['verse']}",
        "content": verse_text,
        "version": ref_obj['version']
    }).eq("id", 1).execute()
    print(f"Updated screen to {ref_obj['book']}")

print("Listening...")
with mic as source:
    recognizer.adjust_for_ambient_noise(source)
    while True:
        audio = recognizer.listen(source)
        data = io.BytesIO(audio.get_wav_data())
        segments, _ = model.transcribe(data)
        text = " ".join([s.text for s in segments])
        
        if text.strip():
            print(f"Heard: {text}")
            ref = parse_bible_reference(text)
            if ref:
                update_screen(ref)
