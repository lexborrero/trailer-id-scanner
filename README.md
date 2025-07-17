# Trailer ID Scanner

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