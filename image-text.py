import base64
import io
import json
import os
from pathlib import Path

import requests
from PIL import Image

ROOT = Path(__file__).resolve().parent
OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://localhost:9009/api/chat")
IMAGE_PATH = ROOT / "image" / "handnote-12.png"


def encode_image_to_base64(image_path, fmt="PNG"):
    with Image.open(image_path) as img:
        buffered = io.BytesIO()
        img.save(buffered, format=fmt)
        return base64.b64encode(buffered.getvalue()).decode("utf-8")


def run_remote_ollama_vision(image_path):
    b64img = encode_image_to_base64(image_path, fmt="PNG")
    data = {
        "model": "llama3.2-vision:latest",
        "messages": [
            {
                "role": "user",
                "content": "What is in this image?",
                "images": [b64img],
            }
        ],
    }
    resp = requests.post(OLLAMA_URL, json=data)
    resp.raise_for_status()

    collected = []
    for line in resp.text.strip().splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
            if "message" in obj and "content" in obj["message"]:
                collected.append(obj["message"]["content"])
        except Exception as e:
            print("JSON error:", str(e), "Line:", line)
            continue

    if collected:
        final_text = "".join(collected)
        print("Extracted text:\n", final_text)
    else:
        print("No message.")


if __name__ == "__main__":
    run_remote_ollama_vision(IMAGE_PATH)
