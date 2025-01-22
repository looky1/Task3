from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Load flashcards from the CSV file
def load_flashcards():
    data = pd.read_csv('mistakes.csv')
    flashcards = []
    for _, row in data.iterrows():
        flashcards.append({
            'student_id': row['Student_ID'],
            'type': row['Mistake_Type'],
            'question': row['Original_Sentence'],
            'answer': row['Corrected_Sentence']
        })
    return flashcards

flashcards = load_flashcards()

@app.route('/flashcards', methods=['GET'])
def get_flashcards():
    return jsonify(flashcards)

if __name__ == '__main__':
    app.run(debug=True)
