import os
import requests

# Target directory
target_dir = r"靜態網頁修改測試\01\images"
if not os.path.exists(target_dir):
    os.makedirs(target_dir)

images = {
    "kipchoge.jpg": "https://images.unsplash.com/photo-1569517282132-25d22f4573e6?auto=format&fit=crop&q=80&w=1200&h=600",
    "street-basketball.jpg": "https://images.unsplash.com/photo-1519861531473-9200263931a2?auto=format&fit=crop&q=80&w=1200&h=600",
    "baseball-field.jpg": "https://images.unsplash.com/photo-1508345228704-935cc84bf55d?auto=format&fit=crop&q=80&w=1200&h=600",
    "healthy-food.jpg": "https://images.unsplash.com/photo-1490645935967-10de6ba17061?auto=format&fit=crop&q=80&w=1200&h=600",
    "soccer-match.jpg": "https://images.unsplash.com/photo-1579952363873-27f3bade8f55?auto=format&fit=crop&q=80&w=1200&h=600",
    "running-shoes.jpg": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&q=80&w=1200&h=600",
    "world-cup.jpg": "https://images.unsplash.com/photo-1518609878373-06d740f60d8b?auto=format&fit=crop&q=80&w=1200&h=600",
    "basketball-court.jpg": "https://images.unsplash.com/photo-1504450758481-7338eba7524a?auto=format&fit=crop&q=80&w=1200&h=600",
    "marathon.jpg": "https://images.unsplash.com/photo-1452626038306-3a2429c7894d?auto=format&fit=crop&q=80&w=1200&h=600",
    "gym.jpg": "https://images.unsplash.com/photo-1517836357463-d25dfeac3438?auto=format&fit=crop&q=80&w=1200&h=600",
    "home-workout.jpg": "https://images.unsplash.com/photo-1517836357463-d25dfeac3438?auto=format&fit=crop&q=80&w=1200&h=600",
    "injury.jpg": "https://images.unsplash.com/photo-1594882645126-14020914d58d?auto=format&fit=crop&q=80&w=1200&h=600"
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

for filename, url in images.items():
    file_path = os.path.join(target_dir, filename)
    try:
        print(f"Downloading {filename}...")
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            with open(file_path, 'wb') as f:
                f.write(response.content)
            print(f"Saved to {file_path}")
        else:
            print(f"Failed to download {filename}: Status {response.status_code}")
    except Exception as e:
        print(f"Error downloading {filename}: {e}")

