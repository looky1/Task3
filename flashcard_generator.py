import pandas as pd

def generate_flashcards(csv_file):
    data = pd.read_csv(csv_file)
    flashcards = []

    for _, row in data.iterrows():
        flashcards.append({
            "student_id": row["Student_ID"],
            "type": row["Mistake_Type"],
            "question": row["Original_Sentence"],
            "answer": row["Corrected_Sentence"]
        })

    return flashcards

if __name__ == "__main__":
    flashcards = generate_flashcards("mistakes.csv")
    print(f"Generated {len(flashcards)} flashcards!")
    for card in flashcards[:5]:  # Display the first 5 flashcards
        print(card)
