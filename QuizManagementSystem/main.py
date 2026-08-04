from quiz_manager import QuizManager
from file_manager import FileManager

manager = QuizManager()

# Load questions from CSV
manager.questions = FileManager.load_questions()

while True:
    print("\n===== Quiz Management System =====")
    print("1. Start Quiz")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        manager.conduct_quiz()
        FileManager.save_result(manager.get_score(), len(manager.questions))

    elif choice == "2":
        print("Thank you for using Quiz Management System.")
        break

    else:
        print("Invalid choice. Please try again.")