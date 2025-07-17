from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# Load your image
image_path = 'C:/Users/Lex/OneDrive/Documents/GitHub/trailer-id-scanner/pictures/trailerid2.png'  # Replace with your image file
image = Image.open(image_path)

# If you don't have OpenCV, install it with:
# pip install opencv-python
import cv2
import numpy as np

# Load image with OpenCV for preprocessing
cv_img = cv2.imread(image_path)
if cv_img is None:
    raise FileNotFoundError(f'Could not load image at {image_path}')
# Convert to grayscale
gray = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)
# Apply thresholding to make text stand out
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
# Optionally, you can try adaptive thresholding for more complex backgrounds:
# thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

# Convert back to PIL Image for pytesseract
preprocessed_image = Image.fromarray(thresh)
preprocessed_image.show()  # This will display the preprocessed image for you to check

# Perform OCR on the preprocessed image
text = pytesseract.image_to_string(preprocessed_image, lang='eng')

# Output the result
print("Detected Text:")
# Expected ouput: "AV2204"
print(text)