import os

import constant
from bot_nlp import nlp
from slack_client import client, event


class App():
    """
        Primary instance for refined-bot, glues together the components.
    """
    nlp = nlp.NLP()
    slackClient: client.Client = None

    def __init__(self):
        """
            Instantiate components.
        """
        self.slackClient = client.Client(
            token=os.environ[constant.BOT_ACCESS_TOKEN],
            onMessageFn=self.onMessage,
        )

    def start(self):
        """
            Application start, initialize Slack client communication.
        """
        self.slackClient.start()

    def onMessage(self, **payload: dict):
        """
            Handles an message event, apply NLP parsing in order to extract intent.
        """
        message = event.SlackEvent(**payload)
        intent = self.nlp.parse(message.text)
        print(intent)


if __name__ == '__main__':
    app = App()
    app.start()
