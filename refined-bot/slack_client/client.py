import ssl

import certifi
import slack
from slack import RTMClient


class Client():
    """
        Represents Slack client instance.
    """
    rtmClient: RTMClient = None

    def __init__(self, token: str, onMessageFn):
        self.rtmClient = slack.RTMClient(
            token=token,
            ssl=ssl.create_default_context(cafile=certifi.where()),
            auto_reconnect=True,
        )
        slack.RTMClient.run_on(event='message')(onMessageFn)

    def start(self):
        self.rtmClient.start()
        time.sleep(60)
