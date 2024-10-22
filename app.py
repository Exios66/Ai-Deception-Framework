from flask import jsonify, Flask, render_template

app = Flask(__name__)

@app.route('/api/features')
def get_features():
    features = [
        {"name": "AI Model Analysis", "description": "Comprehensive analysis of AI models to detect potential vulnerabilities"},
        {"name": "Deception Detection Algorithms", "description": "Advanced algorithms to identify deceptive patterns in AI-generated content"},
        {"name": "Real-time Monitoring", "description": "Continuous monitoring of AI systems for anomalous behavior"},
        {"name": "Explainable AI Integration", "description": "Tools to enhance transparency and interpretability of AI decision-making processes"}
    ]
    return jsonify(features)

@app.route('/api/deception-metrics')
def deception_metrics():
    # In a real application, you would fetch this data from your database or analytics system
    metrics = [
        {"name": "Total Analyses", "value": 1000},
        {"name": "Average Deception Score", "value": 0.42},
        {"name": "Most Common Technique", "value": "Misdirection"},
        {"name": "Detection Accuracy", "value": "89%"}
    ]
    return jsonify(metrics)

@app.route('/analysis')
def analysis():
    return render_template('analysis.html')

@app.route('/detection')
def detection():
    return render_template('detection.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
