def load_questions():
    questions = [
        {
            "question": "What is the capital of India?",
            "options": ["A. Mumbai", "B. Delhi", "C. Chennai", "D. Kolkata"],
            "answer": "B"
        },
        {
            "question": "Which language is used for web development?",
            "options": ["A. Python", "B. HTML", "C. C++", "D. Java"],
            "answer": "B"
        },
        {
            "question": "Who is known as the Father of Computers?",
            "options": ["A. Charles Babbage", "B. Elon Musk", "C. Bill Gates", "D. Steve Jobs"],
            "answer": "A"
        }
    ]
    return questions


def welcome_message():
    print("=================================")
    print("     WELCOME TO QUIZ GAME 🎉")
    print("=================================")
    print("Rules:")
    print("1. Each question has 4 options (A, B, C, D).")
    print("2. Type the correct option letter.")
    print("3. Each correct answer gives 1 point.")
    print()


def play_quiz():
    questions = load_questions()
    score = 0

    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)

        user_answer = input("Enter your answer (A/B/C/D): ").upper()

        if user_answer == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print("❌ Wrong!")
            print("Correct answer is:", q["answer"])

    print("\n=================================")
    print("Quiz Completed!")
    print("Your Final Score:", score, "/", len(questions))

    if score == len(questions):
        print("Excellent Performance! 🎉")
    elif score >= 2:
        print("Good Job! 👍")
    else:
        print("Keep Practicing! 💪")
    print("=================================")


def main():
    while True:
        welcome_message()
        play_quiz()

        again = input("Do you want to play again? (yes/no): ").lower()
        if again != "yes":
            print("Thank you for playing! 😊")
            break


main()