from sys import set_int_max_str_digits

import ollama
from ollama import Client

"""
    Set the location for where ollama is running, default is based on default install
"""

SYSTEM_PROMPT = "You are Mr. Computer, a friendly chatbot."

def send_message_to_ollama(state):
    """
    Sends an image to Ollama for processing and returns the response.

    Args:
      image_path: Path to the image file.
      prompt: Optional prompt to send with the image.

    Returns:
      The text response from Ollama.
    """
    try:
        response = ollama.chat(
            model='gemma3:27b',  # You have lots of options for this, if you're interested in trying other ones, let me know.
            messages=state,
        )
        return response
    except Exception as e:
        print(f"An error occurred: {e}")
        return None




# create an empty list to store all the models we have installed.
model_list = []






def main():
    """
    Main function to run the Ollama Chatbot.
    """
    state = [{
        'role': 'system',
        'content': SYSTEM_PROMPT,
    }]
    print("Please give a message to Mr. Computer. Type \"EXIT\" to quit.")
    message = input()
    while message.upper() != "EXIT":
        state.append({
            'role': 'user',
            'content' : message,
        })
        response = send_message_to_ollama(state)
        print('Mr. Computer:', response.message.content.strip())
        state.append({
            'role':'Assistant',
            'content' : 'response.message.content'
        })
        message = input()



if __name__ == "__main__":
    main()
