import os
import time

import pytest

import constant

from .slack import SlackClient


def onMessageFn(**payload):
    print('onMessageFn')


def test_client():
    s = SlackClient(
        token=os.environ[constant.BOT_ACCESS_TOKEN],
        onMessageFn=onMessageFn,
    )
    s.start()
    time.sleep(300)
