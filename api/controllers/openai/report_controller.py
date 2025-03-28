from flask import Flask, request, jsonify
import os
from openai import OpenAI

app = Flask(__name__)

# Load API Key securely from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
print(OPENAI_API_KEY)
client = OpenAI(api_key="")

@app.route('/search_stocks', methods=['GET'])
def search_stocks():
    """
    Fetch stock market news using OpenAI Web Search
    """
    market = request.args.get('market', 'NASDAQ')  # Default to NASDAQ
    query = f"Top companies in {market} based on revenue and growth percentage"
    
    try:
        response = client.responses.create(
            model="gpt-4o",
            tools=[{"type": "web_search_preview"}],
            input=query
        )
        result = response.output_text
        return jsonify({"market": market, "top_companies": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/process_report', methods=['POST'])
def process_report():
    """
    Process uploaded PDF file and extract relevant financial data
    """
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400
    
    file = request.files['file']
    # Save and process file (can integrate OpenAI File Search here)
    # For now, we return a placeholder response
    return jsonify({"message": "File received, processing logic to be implemented."})

if __name__ == '__main__':
    app.run(debug=True)
