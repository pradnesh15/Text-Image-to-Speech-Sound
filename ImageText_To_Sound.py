import pytesseract
from PIL import Image
from gtts import gTTS
import os


def text_to_audio(text, output_file="output.mp3", lang="en"):
    
    tts = gTTS(text=text, lang=lang)
    tts.save(output_file)
    print(f"Audio saved as {output_file}")

# Path to the Tesseract executable (may vary based on your system)
pytesseract.pytesseract.tesseract_cmd = r'tesseract.exe'

def read_text_from_image(image_path):
    # Open the image file
    with Image.open(image_path) as img:
        # Use pytesseract to do OCR on the image
        text = pytesseract.image_to_string(img)
        return text

if __name__ == "__main__":
    # Path to the image file
    image_path = 'img.png'

    # Read text from the image
    text = read_text_from_image(image_path)
    
    # Print the extracted text
    print("Text extracted from image:")
    print(text)
    text_to_audio(text)

