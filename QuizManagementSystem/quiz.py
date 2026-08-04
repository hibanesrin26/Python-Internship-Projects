from question import Question

class Quiz(Question):

    def __init__(self, question, option1, option2, option3, option4, answer):
        super().__init__(question, option1, option2, option3, option4, answer)

    def get_answer(self):
        return self._answer

    def display(self):
        print("\n" + self._question)
        print("1.", self._option1)
        print("2.", self._option2)
        print("3.", self._option3)
        print("4.", self._option4)