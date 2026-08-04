class QuizManager:

    def __init__(self):
        self.questions = []
        self.score = 0

    def add_question(self, question):
        self.questions.append(question)

    def conduct_quiz(self):
        self.score = 0

        if not self.questions:
            print("No questions available.")
            return

        for question in self.questions:
            question.display()

            try:
                answer = int(input("Enter your answer (1-4): "))

                if answer == question.get_answer():
                    self.score += 1

            except ValueError:
                print("Invalid input.")

        print(f"\nQuiz Completed!")
        print(f"Your Score: {self.score}/{len(self.questions)}")

    def get_score(self):
        return self.score