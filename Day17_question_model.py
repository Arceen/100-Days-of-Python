class Question:
    def __init__(self, text, answer):
        self.question = text
        self.answer = answer
    def __str__(self):
        return f"{self.question} - {self.answer}"