# from flask import Flask, request, jsonify, render_template
# from gtts import gTTS
# import os
# import requests

# app = Flask(__name__)

# # Folder to save the generated audio file
# STATIC_FOLDER = os.path.join(os.getcwd(), 'static')
# if not os.path.exists(STATIC_FOLDER):
#     os.mkdir(STATIC_FOLDER)

# # Your D-ID API URL and Authentication Key
# D_ID_API_URL = "https://studio.d-id.com/share?id=667985252804bf456d9241b7f17fb893&utm_source=copy"
# D_ID_API_KEY = "YXJqdWFyanU3MDVAZ21haWwuY29t:WCGLT-xu9KlByI3j8YvUa"  # Replace with your actual API key

# # Home Route - Serve the HTML page
# @app.route('/')
# def home():
#     return render_template('index.html')

# # Route to handle the query from the frontend
# @app.route('/ask', methods=['POST'])
# def ask():
#     query = request.json.get("query")  # Get user query from frontend

#     # Call the D-ID API to generate the avatar's response (this is a placeholder, you can integrate your own logic)
#     avatar_response = get_avatar_response(query)

#     # Convert response text to speech (TTS)
#     tts = gTTS(avatar_response, lang='en')
#     audio_path = os.path.join(STATIC_FOLDER, "response.mp3")
#     tts.save(audio_path)  # Save as response.mp3

#     # Send the response and audio file path to the frontend
#     return jsonify({
#         'response': avatar_response,
#         'audio_path': '/static/response.mp3'
#     })

# # Function to simulate getting a response from the avatar (you can customize this to pull from a database or API)
# def get_avatar_response(query):
#     # Example static response based on user query
#     if 'hello' in query.lower():
#         return "Hello! How can I assist you today?"
#     elif 'how are you' in query.lower():
#         return "I am doing great, thank you for asking!"
#     else:
#         return "Sorry, I didn't understand that. Can you please rephrase?"

# if __name__ == '__main__':
#     app.run(debug=True)


import openai
from flask import Flask, request, jsonify, render_template
from gtts import gTTS
import os

app = Flask(__name__)

# OpenAI API key
openai.api_key = 'YOUR_API_KEY'

# Folder to save the generated audio file
STATIC_FOLDER = os.path.join(os.getcwd(), 'static')
if not os.path.exists(STATIC_FOLDER):
    os.mkdir(STATIC_FOLDER)

# Home Route - Serve the HTML page
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle the query from the frontend
@app.route('/ask', methods=['POST'])
def ask():
    query = request.json.get("query")  # Get user query from frontend

    # Call OpenAI API to get a dynamic response
    bot_response = get_openai_response(query)

    # Check if OpenAI response is empty
    if not bot_response:
        return jsonify({
            'error': 'No response from OpenAI'
        }), 400

    # Convert response text to speech (TTS)
    try:
        tts = gTTS(bot_response, lang='en')
        audio_path = os.path.join(STATIC_FOLDER, "response.mp3")
        tts.save(audio_path)  # Save as response.mp3

        # Send the response and audio file path to the frontend
        return jsonify({
            'response': bot_response,
            'audio_path': '/static/response.mp3'
        })
    except Exception as e:
        return jsonify({
            'error': f'Error generating speech: {str(e)}'
        }), 500

# Function to get a response from OpenAI API
# def get_openai_response(user_query):
#     try:
#         response = openai.chat.Completion.create(
#             model="gpt-3.5-turbo",  # You can use a different model like "gpt-4"
#             messages=[{"role": "user", "content": user_query}]
#         )
#         return response['choices'][0]['message']['content']
#     except Exception as e:
#         return str(e)

# Function to get a response from OpenAI API
import openai

# Set your OpenAI API key
openai.api_key = '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'

# Function to get a response from OpenAI API
def get_openai_response(user_query):
    try:
        # Use the completions.create method (corrected syntax)
        response = openai.Completion.create(
            model="gpt-3.5-turbo",  # You can also try with "gpt-4" or another model
            prompt=user_query,  # Use prompt instead of messages
            max_tokens=150  # Optional parameter to control the length of the response
        )

        # Return the model's reply
        return response['choices'][0]['text']
    except Exception as e:
        return f"Error: {str(e)}"

# Example usage:
user_input = "How are you?"
print(get_openai_response(user_input))

if __name__ == '__main__':
    app.run(debug=True)

