import random
from logger import Logger


class Busybody:
    source_questions = [
        "What is your name?",
        "How old are you?",
        "Where do you live?",
        "Which day were you born?",
        "What is your favorite food?",
        "Where do you go for vacation?",
        "What is your Zodiac sign?",
        "What is your favorite season?",
        "Where do you work?",
        "What is your favorite sport?",
    ]
    quit_prompt = "Type q to quit:"

    def __init__(self, name):
        self.name = name
        self.logger = Logger(name).logger

    def __str__(self):
        return f"Busybody.{self.name}"

    def run(self):
        self.questions = self.source_questions.copy()
        answer = None
        while answer != "q" and len(self.questions):
            # log random question
            random_question = random.choice(self.questions)
            formatted_question = f"{self.quit_prompt} {random_question} "
            self.logger.info(formatted_question)

            # ask question, log answer
            answer = input(formatted_question)
            self.logger.info(answer)

            # remove question from list
            self.questions.remove(random_question)

        if not len(self.questions):
            print("No more questions...")
        print("All done!")
