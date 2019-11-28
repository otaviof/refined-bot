import re

import spacy
from spacy.lang.en import English
from spacy.matcher import Matcher
from spacy.tokens import Token

from .intent import Intent


class NLP():
    """
        Represents the NLP steps taken to extact "Intent".
    """

    nlp: English = None
    matcher: Matcher = None

    # regular expression to find an ticket
    ticketIdRe = r'[A-Z]{3,6}\-[0-9]{1,4}'
    ticketIdPattern = [{'TAG': {'REGEX': ticketIdRe}}]

    def __init__(self):
        """
            Instantiate class by executing spacy boilerplates.
        """
        self.nlp = spacy.load('en_core_web_sm')
        self.matcher = Matcher(self.nlp.vocab, validate=True)
        self.matcher.add('TicketID', None, self.ticketIdPattern)

    def __findTicketID(self, doc: Token.doc) -> str:
        """
            Using regexp will try to find a ticket ID.
        """
        for match in re.finditer(self.ticketIdRe, doc.text):
            start, end = match.span()
            span = doc.char_span(start, end)
            if span is not None:
                return span.text
        return None

    def __findLemma(self, doc: Token.doc) -> str:
        """
            Will try to identify the characteristics of the message in order to define what's the
            action conveyed. It should return as soon as the "lemma" is defined.
        """
        for token in doc:
            if token.lemma_ == 'poker':
                return token.lemma_
        return None

    def parse(self, phrase: str) -> Intent:
        """
            Given a phrase it will extract Intent.
        """
        doc = self.nlp(phrase)
        ticketID = self.__findTicketID(doc)
        lemma = self.__findLemma(doc)
        return Intent(lemma, ticketID, doc.text)
