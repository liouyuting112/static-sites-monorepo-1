import os
import time
import requests
import urllib.parse
from PIL import Image
from io import BytesIO

# Base directory
BASE_DIR = os.getcwd()
SHARED_ASSETS_DIR = os.path.join(BASE_DIR, 'shared-assets')

# List of failed images to retry
RETRY_LIST = [
    {'filename': 'site1-massage.webp', 'prompt': 'Human hands gently massaging the spine of a dog, close up on hands and fur, relaxing atmosphere'},
    {'filename': 'logo-icon.webp', 'prompt': 'Simple vector icon of a dog paw with a heart, warm brown color, minimal design, white background'},
    {'filename': 'site2-hero.webp', 'prompt': 'A schnauzer dog wearing glasses sitting on a sofa with an open book, clean bright living room, educational concept'},
    {'filename': 'site2-about.webp', 'prompt': 'A middle-aged asian woman in smart casual clothes writing notes while sitting on floor next to two senior dogs, home office'},
    {'filename': 'site2-kidney.webp', 'prompt': 'Ingredients for dog food on a kitchen counter: cooked chicken breast, egg whites, and white rice, clean composition'},
    {'filename': 'site4-hero.webp', 'prompt': 'A senior dog walking on a mossy path in a foggy forest, morning light, peaceful and ethereal nature photography'},
    {'filename': 'site4-herb.webp', 'prompt': 'Fresh turmeric root, ginger, and chamomile flowers arranged on a wooden table, herbal medicine concept'},
]

def generate_and_save_image(image_data):
    filename = image_data['filename']
    prompt = image_data['prompt']
    save_path = os.path.join(SHARED_ASSETS_DIR, filename)
    
    print(f"Retrying {filename}...")
    
    try:
        # Add random seed to vary the result and potentially bypass cache/error
        import random
        seed = random.randint(0, 10000)
        
        encoded_prompt = urllib.parse.quote(prompt)
        url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1024&height=768&seed={seed}&nologo=true"
        
        response = requests.get(url, timeout=60)
        response.raise_for_status()
        
        image_bytes = BytesIO(response.content)
        img = Image.open(image_bytes)
        img.save(save_path, 'WEBP', quality=85)
        print(f"  Success! Saved to {save_path}")
        return True
        
    except Exception as e:
        print(f"  Retry failed for {filename}: {str(e)}")
        return False

def main():
    print(f"Retrying {len(RETRY_LIST)} failed images...")
    
    for img in RETRY_LIST:
        success = generate_and_save_image(img)
        if not success:
            # Try one more time with a simpler prompt if complex one fails
            print("    Attempting simplified prompt...")
            img['prompt'] = img['prompt'].split(',')[0] # Take only the first part
            generate_and_save_image(img)
            
        time.sleep(2) # Longer delay

if __name__ == "__main__":
    main()

