import sqlite3

def init_db():
    conn = sqlite3.connect('questions.db')
    c = conn.cursor()
    
    # Create questions table
    c.execute('''
        CREATE TABLE IF NOT EXISTS questions (
            id TEXT PRIMARY KEY,
            category TEXT NOT NULL,
            question TEXT NOT NULL,
            correct_answer TEXT NOT NULL,
            options TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Add some sample questions
    sample_questions = [
        ('q1', 'astronomy', 'What is the closest star to Earth?', 'The Sun', 
         '["The Sun", "Proxima Centauri", "Alpha Centauri", "Sirius"]'),
        ('q2', 'mathematics', 'What is the value of π (pi) to two decimal places?', '3.14',
         '["3.14", "3.16", "3.12", "3.18"]'),
        ('q3', 'literature', 'Who wrote "Romeo and Juliet"?', 'William Shakespeare',
         '["William Shakespeare", "Charles Dickens", "Jane Austen", "Mark Twain"]')
    ]
    
    c.executemany('''
        INSERT OR REPLACE INTO questions (id, category, question, correct_answer, options)
        VALUES (?, ?, ?, ?, ?)
    ''', sample_questions)
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db() 