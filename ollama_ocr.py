import base64
from PIL import Image
import ollama

SYSTEM_PROMPT = """Act as an OCR assistant. Analyze the provided image and:
1. Recognize all visible text in the image as accurately as possible.
2. Maintain the original structure and formatting of the text.
3. If any words or phrases are unclear, indicate this with [unclear] in your transcription.
4. Only respond with text pictured in the image"""

def encode_image_to_base64(image_path):
    """Convert an image file to a base64 encoded string."""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


def send_image_to_ollama(image_path):
    """
    Sends an image to Ollama for processing and returns the response.

    Args:
      image_path: Path to the image file.

    Returns:
      The text response from Ollama.
    """

    image = encode_image_to_base64(image_path)
    try:
        response = ollama.chat(
            model='gemma3:27b',  # Make sure you have a vision model like llava installed
            messages=[
                {
                    'role':'system',
                    'content':SYSTEM_PROMPT,
                },
                {
                    'role': 'user',
                    'images': [image],
                },
            ],
        )
        return response['message']['content']
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    image_path = input("Please give a path to an image: ")  # test.png
    result = send_image_to_ollama(image_path)
    if result:
        print("OCR Recognition Result:")
        print(result)
    else:
        print(result)
