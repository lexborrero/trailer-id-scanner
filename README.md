# Trailer ID Scanner

## Full-Stack Architecture

- **Backend:** FastAPI (Python) for OCR, AI, and Excel export
- **Frontend:** React.js (Create React App) for file upload, results display, and Excel download

### Quickstart

#### Backend (API)
1. Install dependencies:
   ```bash
   pip install fastapi uvicorn easyocr opencv-python pandas openpyxl
   ```
2. Run the API:
   ```bash
   uvicorn backend.main:app --reload
   ```

#### Frontend (Web UI)
1. Install dependencies:
   ```bash
   cd frontend
   npm install
   ```
2. Start the React app:
   ```bash
   npm start
   ```

---

## Table of Contents
- [Project Overview](#project-overview)
- [Backend (FastAPI)](#backend-fastapi)
- [Frontend (React)](#frontend-react)
- [OCR/AI](#ocrai)
- [Excel Export](#excel-export)
- [How to Run](#how-to-run)
- [License](#license)

This project provides a simple Python script to extract trailer ID numbers from images using Optical Character Recognition (OCR).

## Features
- Uses Tesseract OCR to detect and extract text from images of trailers.
- Includes image preprocessing (grayscale, thresholding) for improved accuracy.
- Works with common image formats (PNG, JPG, etc.).

## Requirements
- Python 3.7+
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) (must be installed and available in your system PATH)
- Python packages: `pytesseract`, `Pillow`, `opencv-python`, `numpy`

Install Python dependencies with:
```
pip install pytesseract pillow opencv-python numpy
```

## Usage
1. Place your trailer image in the `pictures/` directory.
2. Update the `image_path` variable in `testOCR.py` to point to your image file (e.g., `pictures/trailerid1.png`).
3. Run the script:
   ```
   python testOCR.py
   ```
4. The script will preprocess the image, perform OCR, and print the detected text (trailer ID) to the console.

## Notes
- For best results, use clear, high-contrast images with the trailer ID upright and unobstructed.
- You can adjust preprocessing parameters in `testOCR.py` for different image conditions.

---

**Example output:**
```
Detected Text:
LR7634
``` 