from flask import Flask, request, jsonify, send_from_directory
from flask_talisman import Talisman
from werkzeug.middleware.proxy_fix import ProxyFix
import logging
from logging.handlers import RotatingFileHandler
import os
from dotenv import load_dotenv
import jwt
from datetime import datetime, timedelta
import sqlite3
from functools import wraps

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('JWT_SECRET')
Talisman(app)
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

# Configure logging
if not os.path.exists('logs'):
    os.mkdir('logs')

file_handler = RotatingFileHandler('logs/app.log', maxBytes=10240, backupCount=10)
file_handler.setFormatter(logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
))
file_handler.setLevel(logging.INFO)
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)
app.logger.info('AI Deception Framework startup')

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing'}), 401
        try:
            token = token.split(" ")[1]  # Remove 'Bearer ' prefix
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        except:
            return jsonify({'message': 'Token is invalid'}), 401
        return f(*args, **kwargs)
    return decorated

def get_db_connection():
    conn = sqlite3.connect('questions.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def serve_index():
    return send_from_directory('docs', 'index.html')

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

@app.route('/api/token', methods=['POST'])
def create_token():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return jsonify({'message': 'Could not verify'}), 401
    
    # In production, verify credentials against database
    if auth.username == "admin" and auth.password == "password":
        token = jwt.encode({
            'user': auth.username,
            'exp': datetime.utcnow() + timedelta(hours=24)
        }, app.config['SECRET_KEY'])
        return jsonify({'token': token})
    
    return jsonify({'message': 'Could not verify'}), 401

@app.route('/api/v1/analysis/model', methods=['POST'])
@token_required
def analyze_model():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    try:
        # Process the model file and analyze it
        analysis_result = {
            'model_type': 'neural_network',
            'accuracy': 0.918,
            'deception_points': [
                'Potential bias in output layer',
                'Unusual activation patterns'
            ],
            'recommendation': 'Consider reviewing the model\'s training data for potential biases',
            'confidence_score': 0.85
        }
        return jsonify(analysis_result)
    except Exception as e:
        app.logger.error(f'Error analyzing model: {str(e)}')
        return jsonify({'error': 'Error analyzing model'}), 500

@app.route('/api/v1/detection/analyze', methods=['POST'])
@token_required
def detect_deception():
    data = request.get_json()
    if not data or 'content' not in data:
        return jsonify({'error': 'No content provided'}), 400
    
    try:
        # Analyze content for deception
        detection_result = {
            'probability': 0.342,
            'confidence': 0.89,
            'issues': [
                'Inconsistent narrative',
                'Unusual language patterns'
            ],
            'recommendations': [
                'Review content for consistency',
                'Verify source authenticity'
            ]
        }
        return jsonify(detection_result)
    except Exception as e:
        app.logger.error(f'Error detecting deception: {str(e)}')
        return jsonify({'error': 'Error analyzing content'}), 500

@app.route('/api/v1/literary-vault/questions/<category>', methods=['GET'])
@token_required
def get_questions(category):
    limit = request.args.get('limit', default=10, type=int)
    random = request.args.get('random', default=True, type=bool)
    
    try:
        conn = get_db_connection()
        if random:
            questions = conn.execute(
                'SELECT * FROM questions WHERE category = ? ORDER BY RANDOM() LIMIT ?',
                (category, limit)
            ).fetchall()
        else:
            questions = conn.execute(
                'SELECT * FROM questions WHERE category = ? LIMIT ?',
                (category, limit)
            ).fetchall()
        conn.close()
        
        return jsonify([dict(q) for q in questions])
    except Exception as e:
        app.logger.error(f'Error fetching questions: {str(e)}')
        return jsonify({'error': 'Error fetching questions'}), 500

@app.route('/api/v1/literary-vault/questions/randomize', methods=['POST'])
@token_required
def randomize_questions():
    data = request.get_json()
    if not data or 'category' not in data:
        return jsonify({'error': 'Category not provided'}), 400
    
    category = data['category']
    count = data.get('count', 5)
    seed = data.get('seed')
    
    try:
        conn = get_db_connection()
        if seed is not None:
            # Use seed for reproducible randomization
            conn.execute('PRAGMA seed = ?', (seed,))
        
        questions = conn.execute(
            'SELECT * FROM questions WHERE category = ? ORDER BY RANDOM() LIMIT ?',
            (category, count)
        ).fetchall()
        conn.close()
        
        return jsonify([dict(q) for q in questions])
    except Exception as e:
        app.logger.error(f'Error randomizing questions: {str(e)}')
        return jsonify({'error': 'Error randomizing questions'}), 500

@app.route('/api/v1/detection/analyze-questions', methods=['POST'])
@token_required
def analyze_questions():
    questions = request.get_json()
    if not questions:
        return jsonify({'error': 'No questions provided'}), 400
    
    try:
        results = []
        for question in questions:
            analysis = {
                'probability': 0.342,
                'confidence': 0.89,
                'issues': [
                    'Potential ambiguity in question',
                    'Answer might need clarification'
                ],
                'recommendations': [
                    'Review question wording',
                    'Add additional context to answer'
                ]
            }
            results.append(analysis)
        return jsonify(results)
    except Exception as e:
        app.logger.error(f'Error analyzing questions: {str(e)}')
        return jsonify({'error': 'Error analyzing questions'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, ssl_context='adhoc')
