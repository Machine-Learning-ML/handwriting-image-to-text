# Image to text (Llama 3.2 Vision & OCR)

This repo contains:

- **`image-text.py`** — send an image to a local or remote **Ollama** API (`llama3.2-vision`) and print streamed text.
- **`handwrite.py`** — **TrOCR** (`microsoft/trocr-base-handwritten`) for offline handwritten text (PyTorch + Hugging Face).
- **`image-to-text.ipynb`** — **OpenCV + Tesseract** experiments on sample images under `image/`.

## Prerequisites

1. **Python 3.10+** recommended.
2. **Tesseract OCR** installed and on your `PATH` (for the notebook and `pytesseract`). On Windows, install [Tesseract](https://github.com/tesseract-ocr/tesseract) and uncomment the `tesseract_cmd` line in the notebook if needed.
3. For **`image-text.py`**: Ollama running with **`llama3.2-vision`** (or compatible vision model), reachable at your API URL.

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Optional: copy **`.env.example`** to **`.env`** and set `OLLAMA_URL`, or export the variable in your shell.

## Run

```bash
# From this directory; uses image/ and OLLAMA_URL (default in .env.example)
python image-text.py
python handwrite.py
```

Open **`image-to-text.ipynb`** in Jupyter or VS Code. Run the notebook from **this project folder** so paths like `image/handnote-10.png` resolve. The notebook is kept **without stored outputs** for cleaner Git diffs.

## Git hygiene

Do not commit `.env`, API keys, or downloaded model weights. See **`.gitignore`**.
