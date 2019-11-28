import pytest
from .nlp import NLP


def test_parse():
    ticketId = 'XYZ-1234'
    text = 'lets poker %s?' % ticketId

    n = NLP()
    intent = n.parse(text)

    assert intent.action == 'poker'
    assert intent.subject == ticketId
    assert intent.text == text
