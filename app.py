import os
import json
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Configure the Gemini API key
try:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in .env file")
    genai.configure(api_key=api_key)
except Exception as e:
    print(f"Error configuring Gemini API: {e}")
    # You might want to handle this more gracefully
    # For now, we'll let it raise an error if the key is missing

# Create the model
generation_config = {
    "temperature": 0.7,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 4096, # Increased token limit for more detailed content
}

# Using the fast and efficient "flash" model
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash-latest",
    generation_config=generation_config,
)

@app.route('/')
def index():
    """Renders the main HTML page."""
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    """Handles the structured API call to Gemini for content generation."""
    if not request.json or 'prompt' not in request.json:
        return jsonify({"error": "Invalid request. 'prompt' is required."}), 400

    prompt = request.json['prompt']
    is_json_response = request.json.get('is_json', True)

    try:
        response = model.generate_content(prompt)
        
        if not response.candidates:
            raise ValueError("The API response did not contain any candidates.")
        
        text_response = response.text
        
        if is_json_response:
            # Clean the response if it's wrapped in markdown JSON
            if text_response.strip().startswith("```json"):
                text_response = text_response.strip()[7:-3]
            json_data = json.loads(text_response)
            return jsonify(json_data)
        else:
            return jsonify({"text": text_response})

    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({"error": f"Failed to generate content from AI model. Details: {str(e)}"}), 500

@app.route('/chat', methods=['POST'])
def chat():
    """Handles the conversational chat with the AI Tutor."""
    data = request.json
    if not data or 'mainTopic' not in data or 'subTopic' not in data or 'history' not in data:
        return jsonify({"error": "Invalid request. 'mainTopic', 'subTopic', and 'history' are required."}), 400

    main_topic = data['mainTopic']
    sub_topic = data['subTopic']
    history = data['history']

    try:
        # --- NEW, SMARTER SYSTEM INSTRUCTION ---
        system_instruction = (
            f"You are a helpful and friendly AI/ML tutor. The user's main learning goal is '{main_topic}'. You are currently helping them with the specific sub-topic: '{sub_topic}'. "
            f"CRITICAL RULE: Your primary focus is to answer questions related to the main topic of '{main_topic}'. "
            f"If the user asks a question completely unrelated to '{main_topic}' (e.g., about cooking, history, or sleeping), you MUST politely decline. "
            f"Say something like, 'That's an interesting question, but my expertise is focused on {main_topic}. Let's get back to the subject.' "
            "Keep your on-topic answers concise, clear, and beginner-friendly."
        )
        
        # Create a new model instance with the specific system instruction for this chat
        contextual_model = genai.GenerativeModel(
            model_name="gemini-1.5-flash-latest",
            generation_config=generation_config,
            system_instruction=system_instruction
        )

        # The history from the client contains the full conversation including the latest user message
        response = contextual_model.generate_content(history)
        
        return jsonify({"text": response.text})

    except Exception as e:
        print(f"An error occurred during chat: {e}")
        return jsonify({"error": f"Failed to get a response from the AI tutor. Details: {str(e)}"}), 500


if __name__ == '__main__':
    app.run(debug=True)

