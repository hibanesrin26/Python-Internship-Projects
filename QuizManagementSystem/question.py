from abc import ABC, abstractmethod

class Question(ABC):

    def __init__(self, question, option1, option2, option3, option4, answer):
        self._question = question
        self._option1 = option1
        self._option2 = option2
        self._option3 = option3
        self._option4 = option4
        self._answer = answer

    @abstractmethod
    def display(self):
        pass