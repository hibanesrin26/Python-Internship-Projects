import csv
from quiz import Quiz

class FileManager:

    @staticmethod
    def load_questions(filename="questions.csv"):
        questions = []

        try:
            with open(filename, "r") as file:
                reader = csv.reader(file)
                next(reader)

                for row in reader:
                    question = Quiz(
                        row[0],
                        row[1],
                        row[2],
                        row[3],
                        row[4],
                        int(row[5])
                    )
                    questions.append(question)

        except FileNotFoundError:
            print("Question file not found.")

        except Exception as e:
            print("Error:", e)

        return questions

    @staticmethod
    def save_result(score, total, filename="results.csv"):

        try:
            with open(filename, "a", newline="") as file:
                writer = csv.writer(file)

                writer.writerow([score, total])

            print("Result saved successfully.")

        except Exception as e:
            print("Error:", e)