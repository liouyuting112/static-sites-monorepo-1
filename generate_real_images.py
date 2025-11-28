import os
import re
import time
import requests
import urllib.parse
from PIL import Image
from io import BytesIO

# Configuration
INPUT_FILE = 'image_prompts.txt'
# Using raw string for Windows path to avoid escape character issues
OUTPUT_DIR = r'C:\Users\yyutingliu\Downloads\AI生成網站測試\cursor\一個主題多個站\shared-assets'

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_and_download(filename, prompt):
    print(f"Generating: {filename}...")
    print(f"  Prompt: {prompt}")
    
    # Clean up prompt for URL
    clean_prompt = prompt.replace('Prompt:', '').strip()
    
    # Add style keywords if not already present
    if "realistic" not in clean_prompt.lower():
        full_prompt = f"{clean_prompt}, realistic photography, 4k, high quality"
    else:
        full_prompt = clean_prompt
        
    encoded_prompt = urllib.parse.quote(full_prompt)
    
    # Determine dimensions based on usage
    width = 1200
    height = 800
    if 'hero' in filename.lower():
        width, height = 1200, 600
    elif 'about' in filename.lower():
        width, height = 800, 800
    elif 'daily' in filename.lower(): # Square-ish for daily or small cards
        width, height = 800, 800
    
    # Using Pollinations.ai API
    # Random seed is automatically handled if not specified, ensuring variety
    url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width={width}&height={height}&nologo=true"
    
    try:
        response = requests.get(url, timeout=60)
        if response.status_code == 200:
            # Open as image
            img = Image.open(BytesIO(response.content))
            
            # Save as WebP
            output_path = os.path.join(OUTPUT_DIR, filename)
            img.save(output_path, 'WEBP', quality=85)
            print(f"  Success: {output_path}")
        else:
            print(f"  Failed to generate {filename}: Status {response.status_code}")
    except Exception as e:
        print(f"  Error generating {filename}: {e}")

def parse_and_process():
    if not os.path.exists(INPUT_FILE):
        print(f"Error: {INPUT_FILE} not found.")
        return

    print(f"Reading prompts from {INPUT_FILE}...")
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')
    current_filename = None
    current_prompt = None
    
    # Regex to find filename line: e.g. "1. site1-hero.webp"
    # And Prompt line: "   Prompt: ..."
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Match filename
        file_match = re.match(r'^\d+\.\s+(.+\.webp)', line)
        if file_match:
            # If we have a pending pair, process it
            if current_filename and current_prompt:
                generate_and_download(current_filename, current_prompt)
                time.sleep(2) # Polite delay
            
            current_filename = file_match.group(1)
            current_prompt = None
            continue
        
        # Match Prompt
        if line.startswith('Prompt:'):
            current_prompt = line.replace('Prompt:', '').strip()

    # Process the last one
    if current_filename and current_prompt:
        generate_and_download(current_filename, current_prompt)

if __name__ == "__main__":
    parse_and_process()
