#!/usr/bin/env python3
import os
import sys

def verify_filenames():
    base_dir = os.path.join(os.path.dirname(__file__), '..', 'src', 'data', 'blog')
    en_dir = os.path.join(base_dir, 'en')
    ko_dir = os.path.join(base_dir, 'ko')
    ja_dir = os.path.join(base_dir, 'ja')

    if not os.path.exists(en_dir):
        print("No English folder found. Skipping verification.")
        return

    en_files = {f for f in os.listdir(en_dir) if f.endswith('.md')}

    errors = []
    
    # Check Korean translations mapping
    if os.path.exists(ko_dir):
        for f in os.listdir(ko_dir):
            if f.endswith('.md') and f not in en_files:
                errors.append(f"Mismatched KO file: {f} does not exist in 'en' folder.")
                
    # Check Japanese translations mapping
    if os.path.exists(ja_dir):
        for f in os.listdir(ja_dir):
            if f.endswith('.md') and f not in en_files:
                errors.append(f"Mismatched JA file: {f} does not exist in 'en' folder.")

    if errors:
        print("\n[!] FATAL: Multilingual Filename Mismatch Detected!")
        print("Because Unified English Slugs are enforced in this architecture,")
        print("translated posts MUST have the EXACT SAME filename as the English source.")
        print("-" * 50)
        for err in errors:
            print(f" - {err}")
        print("-" * 50)
        sys.exit(1)
    else:
        print("[OK] All multilingual filenames correctly map to Unified English Slugs.")

if __name__ == "__main__":
    verify_filenames()
