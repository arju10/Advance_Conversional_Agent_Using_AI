import openai
from flask import Flask, request, jsonify, render_template
from gtts import gTTS
import os
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

# OpenAI API key
# openai.api_key = 'OPENAI_API_KEY'
openai.api_key = os.getenv('OPENAI_API_KEY')

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

