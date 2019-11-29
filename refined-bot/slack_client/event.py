from slack import WebClient, RTMClient


class SlackEvent():
    data: dict = None
    webClient: WebClient = None
    rtmClient: RTMClient = None
    channelId: str = None
    userId: str = None
    text: str = None

    def __init__(self, **payload: dict):
        self.data = payload['data']
        self.rtmClient = payload['rtm_client']
        self.webClient = payload['web_client']

        self.channelId = self.data.get("channel")
        self.userId = self.data.get("user")
        self.text = self.data.get("text")
