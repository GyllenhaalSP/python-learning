"""
Question Class
"""


class Question:
    """
    Gets a hold of the actual question and answer values.
    """
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer
