# Final Corrected Version: PaperBridge Server Code (Error Safe)
# -------------------------------------------------

from flask import Flask, request, jsonify
import openai
import base64
import os
import json
from datetime import datetime
import traceback

# Initialize Flask app
app = Flask(__name__)

# Set up OpenAI API key from Replit Secrets
oai_api_key = os.getenv("OPENAI_API_KEY")
if not oai_api_key:
    raise ValueError("Missing OpenAI API Key! Please set OPENAI_API_KEY in your Replit environment.")
openai.api_key = oai_api_key

# Main OCR Endpoint
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return "PaperBridge Server is running. Please send POST requests with image data."

    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Missing JSON payload"}), 400

        image_base64 = data.get("image_base64")
        if not image_base64:
            return jsonify({"error": "Missing image_base64 field"}), 400

        # Step 2: Generate transcription + structure using GPT-4-turbo
        client = openai.OpenAI()
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a journal OCR and note structurer. Extract the text from the handwritten image and return a JSON response with this structure:\n\n"
                        "{\n"
                        "  \"filename\": \"type-notes-YYYY-MM-DD\",\n"
                        "  \"body\": \"(Markdown formatted text)\",\n"
                        "  \"attachment_link\": \"(path to uploaded image file)\",\n"
                        "  \"hashtags\": [\"#example1\", \"#example2\"]\n"
                        "}\n\n"
                        "Use the format 'Type: __' and 'Date: __' to infer the type and date. If not found, default to 'Unknown' and today's date.\n\n"
                        "Your job is also to suggest 2 relevant hashtags for the note based on its tone, purpose, and keywords. These should be short, lowercase, Obsidian-friendly (no spaces or symbols), and meaningful (e.g. #reflection, #morningpages, #focus, #faith, #executivetherapy). Return the hashtags in an array exactly as shown above."
                    )
                },
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "Here is the image for OCR and structuring."},
                        {"type": "image_url", "image_url": {"url": "data:image/png;base64," + image_base64}},
                    ]
                }
            ],
            max_tokens=1500,
        )

        gpt_output = response.choices[0].message.content
        print(f"✅ GPT Raw Output: {gpt_output}")
        # ✨ Remove Markdown wrapping if present (triple backticks and 'json' language label)
        if gpt_output.startswith("```") and gpt_output.endswith("```"):
            gpt_output = gpt_output.strip("`")  # Remove backticks
            gpt_output = gpt_output.replace("json", "", 1).strip()  # Remove optional 'json' after backticks

        print(f"✅ GPT Cleaned Output: {gpt_output}")
        # Step 3: Parse the GPT output string into a dictionary
        try:
            note_data = json.loads(gpt_output)
            print(f"✅ Parsed Note Data: {note_data}")
        except json.JSONDecodeError as e:
            print(f"❌ JSON Parse Error: {e}\nRaw Output:\n{gpt_output}")
            return jsonify({"error": "Failed to parse GPT response", "details": str(e), "raw": gpt_output}), 500

        # Step 4: Return the final note info to Shortcuts
        return jsonify(note_data)

    except Exception as e:
        error_trace = traceback.format_exc()
        print(f"❌ Server Error: {str(e)}\nTraceback:\n{error_trace}")
        return jsonify({
            "error": "Server crashed",
            "details": str(e),
            "traceback": error_trace
        }), 500

# Enable error tracking
app.config['PROPAGATE_EXCEPTIONS'] = True

# Run app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)