import os
import requests
from PIL import Image
from io import BytesIO

SAVE_DIR = (
    r"C:\\Users\\natha\\ip\\web_dev\\betting_website_clone\\public\\game-grid\\fishing"
)

IMAGE_URLS = [
    "https://ossimg.91admin123admin.com/91club/gamelogo/JILI/60.png",
    "https://ossimg.91admin123admin.com/91club/gamelogo/JILI/74.png",
    "https://ossimg.91admin123admin.com/91club/gamelogo/MG_Fish/SFG_WDGoldBlastFishing.png",
    "https://ossimg.91admin123admin.com/91club/gamelogo/MG_Fish/SFG_WDFuWaFishing.png",
    "https://ossimg.91admin123admin.com/91club/gamelogo/JILI/71.png",
    "https://ossimg.91admin123admin.com/91club/gamelogo/MG_Fish/SFG_WDMerryIslandFishing.png",
    "https://ossimg.91admin123admin.com/91club/gamelogo/MG_Fish/SFG_WDGoldenFuwaFishing.png",
    "https://ossimg.91admin123admin.com/91club/gamelogo/MG_Fish/SFG_WDGoldenTyrantFishing.png",
    "https://ossimg.91admin123admin.com/91club/gamelogo/MG_Fish/SFG_WDGoldenFortuneFishing.png",
    "https://ossimg.91admin123admin.com/91club/gamelogo/JILI/82.png",
    "https://ossimg.91admin123admin.com/91club/gamelogo/JILI/42.png",
    "https://ossimg.91admin123admin.com/91club/gamelogo/JILI/32.png",
    "https://ossimg.91admin123admin.com/91club/gamelogo/JILI/212.png",
    "https://ossimg.91admin123admin.com/91club/gamelogo/JILI/20.png",
    "https://ossimg.91admin123admin.com/91club/gamelogo/JILI/119.png",
    "https://ossimg.yuk87k786d.com/sikkim/gamelogo/CQ9/AT05.png",
    "https://ossimg.yuk87k786d.com/sikkim/gamelogo/CQ9/AT01.png",
    "https://ossimg.91admin123admin.com/91club/gamelogo/JILI/1.png",
]

os.makedirs(SAVE_DIR, exist_ok=True)

headers = {"User-Agent": "Mozilla/5.0"}

for index, url in enumerate(IMAGE_URLS, start=1):
    try:
        print(f"Downloading {index}: {url}")

        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()

        image = Image.open(BytesIO(response.content)).convert("RGBA")

        filename = f"item{index}.png"
        filepath = os.path.join(SAVE_DIR, filename)

        image.save(filepath, "PNG")

        print(f"Saved -> {filepath}")

    except Exception as e:
        print(f"FAILED -> {url}")
        print(e)

print("\nAll downloads complete.")
