from flask import Flask, request, jsonify
import sqlite3
import os
from flask_talisman import Talisman

app = Flask(__name__)
Talisman(app)

@app.route('/fetch-local-questions')
def fetch_local_questions():
    file_path = request.args.get('file_path')
    if not file_path:
        return jsonify({"error": "file_path parameter is required"}), 400

    if not os.path.exists(file_path):
        return jsonify({"error": "File not found"}), 404

    try:
        conn = sqlite3.connect(file_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id, question, choice1, choice2, choice3, choice4 FROM questions")
        rows = cursor.fetchall()
        conn.close()

        questions = []
        for row in rows:
            questions.append({
                "id": row[0],
                "question": row[1],
                "choices": [row[2], row[3], row[4], row[5]]
            })

        return jsonify({
            "content": "File successfully read and parsed",
            "questions": questions
        })

    except sqlite3.Error as e:
        return jsonify({"error": f"SQLite error: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=8000, ssl_context='adhoc')
