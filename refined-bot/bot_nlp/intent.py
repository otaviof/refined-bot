class Intent():
    action: str = None
    subject: str = None
    text: str = None

    def __init__(self, action: str, subject: str, text: str):
        self.action = action
        self.subject = subject
        self.text = text
