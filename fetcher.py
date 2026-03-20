import requests
from PIL import Image
from io import BytesIO

API_KEY = "f79be76149db7ad5b3aabb097d0c7a7e"

def fetch_latest_image():
    try:
        index = 0
        tiles = [(3,4,2), (4,8,6), (4,9,6)]
        z, x, y = tiles[index % len(tiles)]
        url = f"https://tile.openweathermap.org/map/clouds_new/{z}/{x}/{y}.png?appid={API_KEY}"


        response = requests.get(url, timeout=10)
        response.raise_for_status()

        img = Image.open(BytesIO(response.content)).convert("RGB")
        return img

    except Exception as e:
        return None

