import os
import re
import random
from PIL import Image, ImageDraw, ImageFont

# Configuration
INPUT_FILE = 'image_prompts.txt'
OUTPUT_DIR = 'shared-assets'
FONT_SIZE = 40

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Helper to generate random pastel color
def get_random_color():
    r = random.randint(200, 255)
    g = random.randint(200, 255)
    b = random.randint(200, 255)
    return (r, g, b)

def create_placeholder(filename, usage, prompt):
    # Determine size based on usage (simple heuristics)
    width, height = 800, 600
    if 'hero' in filename.lower():
        width, height = 1200, 600
    elif 'about' in filename.lower():
        width, height = 800, 800
    
    img = Image.new('RGB', (width, height), color=get_random_color())
    d = ImageDraw.Draw(img)
    
    # Try to load a font, fallback to default
    try:
        font = ImageFont.truetype("arial.ttf", FONT_SIZE)
        small_font = ImageFont.truetype("arial.ttf", 20)
    except IOError:
        font = ImageFont.load_default()
        small_font = ImageFont.load_default()

    # Text content
    text = f"{filename}\n({usage})"
    
    # Calculate text position (center)
    # PIL's textbbox is newer, textsize is deprecated. Using basic estimation if needed or textbbox if available.
    try:
        bbox = d.textbbox((0, 0), text, font=font)
        text_w = bbox[2] - bbox[0]
        text_h = bbox[3] - bbox[1]
    except AttributeError:
        # Fallback for older PIL
        text_w, text_h = d.textsize(text, font=font)

    x = (width - text_w) / 2
    y = (height - text_h) / 2
    
    d.text((x, y), text, fill=(50, 50, 50), font=font, align="center")
    
    # Add prompt text at bottom
    prompt_preview = (prompt[:70] + '...') if len(prompt) > 70 else prompt
    d.text((20, height - 50), f"Prompt: {prompt_preview}", fill=(100, 100, 100), font=small_font)

    # Save
    filepath = os.path.join(OUTPUT_DIR, filename)
    img.save(filepath, 'WEBP')
    print(f"Generated: {filepath}")

def parse_and_generate():
    if not os.path.exists(INPUT_FILE):
        print(f"Error: {INPUT_FILE} not found.")
        return

    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to find blocks. 
    # Format: 
    # 1. filename.webp
    #    Usage: ...
    #    Prompt: ...
    
    # We'll split by numbers followed by dot e.g. "\n\d+\. "
    # But first, let's just go line by line for simplicity
    
    lines = content.split('\n')
    current_filename = None
    current_usage = None
    current_prompt = None
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Match filename line: "1. site1-hero.webp"
        file_match = re.match(r'^\d+\.\s+(.+\.webp)', line)
        if file_match:
            # Save previous if exists
            if current_filename:
                create_placeholder(current_filename, current_usage, current_prompt)
            
            current_filename = file_match.group(1)
            current_usage = "Unknown"
            current_prompt = "No prompt"
            continue
            
        if line.startswith('Usage:'):
            current_usage = line.replace('Usage:', '').strip()
        elif line.startswith('Prompt:'):
            current_prompt = line.replace('Prompt:', '').strip()

    # Save last one
    if current_filename:
        create_placeholder(current_filename, current_usage, current_prompt)

if __name__ == "__main__":
    parse_and_generate()
