class Intent():
    action = None
    subject = None
    text = None

    def __init__(self, action, subject, text):
        self.action = action
        self.subject = subject
        self.text = text
