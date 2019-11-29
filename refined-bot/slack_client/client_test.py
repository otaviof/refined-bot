import os
import time

import pytest

import constant

from .client import Client


def onMessageFn(**payload):
    print('onMessageFn')


def test_client():
    c = Client(
        token=os.environ[constant.BOT_ACCESS_TOKEN],
        onMessageFn=onMessageFn,
    )
    c.start()
    time.sleep(300)
