import re

def parse_bible_reference(text):
    # Regex to catch "John 3:16" or "1 John 3 16"
    ref_pattern = r"(\d?\s?[a-zA-Z]+)\s(\d+)[:\s](\d+)"
    ver_pattern = r"(in|version)\s(niv|kjv|msg|nlt)"
    
    ref_match = re.search(ref_pattern, text, re.IGNORECASE)
    ver_match = re.search(version_pattern, text, re.IGNORECASE) if 'ver_pattern' in locals() else None
    
    if ref_match:
        return {
            "book": ref_match.group(1).strip(),
            "chapter": ref_match.group(2),
            "verse": ref_match.group(3),
            "version": ver_match.group(2).upper() if ver_match else "KJV"
        }
    return None
