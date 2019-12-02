import pytest

from .nlp import NLP


def test_parse():
    issueId = 'XYZ-1234'
    text = 'lets poker %s?' % issueId

    n = NLP()
    intent = n.parse(text)

    assert intent.action == 'poker'
    assert intent.subject == issueId
    assert intent.text == text
