from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# Load your image
image_path = 'pictures/trailerid1.png'  # Replace with your image file
image = Image.open(image_path)

# Perform OCR
text = pytesseract.image_to_string(image)

# Output the result
print("Detected Text:")
print(text)