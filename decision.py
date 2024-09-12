import re
# regex


class Decision:

    def __init__(self, question: str, validation_rule: str, error_msg: str):
        self.question = question
        # Is Earth flat?
        self.validation_rule = validation_rule
        # [ynYN]
        self.error_msg = error_msg
        # 'Can you write...?'

    def validate(self, user_input: str) -> bool:
        match = re.match(self.validation_rule, user_input)
        return match is not None


