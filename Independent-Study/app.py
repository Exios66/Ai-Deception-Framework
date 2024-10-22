# Import necessary modules and libraries
from flask import Flask, request, jsonify, abort, render_template, redirect, url_for
import sqlite3
import os
from flask_talisman import Talisman
from functools import wraps
from typing import List, Dict, Any
import logging
from werkzeug.utils import secure_filename
import json

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Flask app and enable HTTPS
app = Flask(__name__, static_folder='static', template_folder='templates')
Talisman(app, force_https=True)

# Decorator to validate file path
def validate_file_path(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        file_path = request.args.get('file_path')
        if not file_path:
            abort(400, description="file_path parameter is required")
        if not os.path.exists(file_path):
            abort(404, description="File not found")
        return func(*args, **kwargs)
    return wrapper

# Function to fetch questions from the database
def fetch_questions_from_db(file_path: str) -> List[Dict[str, Any]]:
    try:
        with sqlite3.connect(file_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, question, choice1, choice2, choice3, choice4 FROM questions")
            rows = cursor.fetchall()

        # Format the fetched data into a list of dictionaries
        return [
            {
                "id": row[0],
                "question": row[1],
                "choices": row[2:]
            }
            for row in rows
        ]
    except sqlite3.Error as e:
        logger.error(f"SQLite error: {str(e)}")
        raise

# Route to fetch local questions
@app.route('/fetch-local-questions')
@validate_file_path
def fetch_local_questions():
    file_path = request.args.get('file_path')
    try:
        questions = fetch_questions_from_db(file_path)
        return jsonify({
            "content": "File successfully read and parsed",
            "questions": questions
        })
    except sqlite3.Error:
        abort(500, description="Database error occurred")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {str(e)}")
        abort(500, description="An unexpected error occurred")

# Error handlers for common HTTP status codes
@app.errorhandler(400)
@app.errorhandler(404)
@app.errorhandler(500)
def handle_error(error):
    return jsonify({"error": error.description}), error.code

# Route for the root URL
@app.route('/')
def home():
    return render_template('index.html')

@app.before_request
def before_request():
    if not request.is_secure:
        url = request.url.replace('http://', 'https://', 1)
        return redirect(url, code=301)

# Run the Flask app
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, ssl_context='adhoc')

@app.route('/api/contact', methods=['POST'])
def contact():
    data = request.json
    # Process the contact form data
    # You might want to save it to a database or send an email
    return jsonify({"message": "Thank you for your message!"}), 200

@app.route('/api/features')
def get_features():
    # This could fetch feature data from your backend
    features = [
        {"name": "AI Model Analysis", "description": "..."},
        {"name": "Deception Detection Algorithms", "description": "..."},
        # ... more features
    ]
    return jsonify(features)

# Add these new routes
@app.route('/api/analyze-model', methods=['POST'])
def analyze_model():
    if 'model' not in request.files:
        return jsonify({"error": "No model file provided"}), 400
    
    file = request.files['model']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        # Here you would call your model analysis function
        # For now, we'll return a dummy result
        analysis_result = {
            "model_type": "Neural Network",
            "layers": 5,
            "parameters": 1000000,
            "potential_vulnerabilities": ["Adversarial attacks", "Data poisoning"]
        }
        
        return jsonify(analysis_result)

@app.route('/api/detect-deception', methods=['POST'])
def detect_deception():
    content = request.json.get('content')
    if not content:
        return jsonify({"error": "No content provided"}), 400
    
    # Here you would call your deception detection function
    # For now, we'll return a dummy result
    detection_result = {
        "deception_score": 0.75,
        "confidence": 0.85,
        "detected_techniques": ["Misdirection", "Omission"]
    }
    
    return jsonify(detection_result)

@app.route('/api/deception-metrics')
def deception_metrics():
    # Here you would fetch real metrics from your system
    # For now, we'll return dummy data
    metrics = [
        {"name": "Total Analyses", "value": 1000},
        {"name": "Average Deception Score", "value": 0.42},
        {"name": "Most Common Technique", "value": "Misdirection"},
        {"name": "Detection Accuracy", "value": "89%"}
    ]
    
    return jsonify(metrics)

# Add this configuration
app.config['UPLOAD_FOLDER'] = 'uploads'

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
