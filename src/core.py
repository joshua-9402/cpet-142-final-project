import abc
import re


class Redactor(abc.ABC):
    def __init__(self, file_location: str):
        self.file_location: str = file_location
        self.regex_email = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        self.regex_phone = r'\b(?:\+?\d{1,3}[-.\s]?)?\(?\d{2,4}\)?[-.\s]?\d{3,4}[-.\s]?\d{3,4}\b'
        self.regex_url = r'https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/[^\s]*)?'
        self.regex_location = r'\b\d+\s[A-Za-z\s]+(?:St|Street|Ave|Avenue|Rd|Road|Blvd|Boulevard|Dr|Drive|Ln|Lane)(?:,\s*[A-Za-z\s]+)?(?:,?\s*[A-Z]{2})?(?:\s*\d{5})?\b'
        self.regex_card = r'\b(?:\d{4}[-\s]?){3}\d{4}\b'
        self.regex_date = r'\b(?:\d{1,4}[-./]\d{1,2}[-./]\d{1,4}|(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\.?\s+\d{1,2},?\s+\d{4})\b'

    @abc.abstractmethod
    def readline(self):
        pass

    @abc.abstractmethod
    def writeline(self):
        pass

    @abc.abstractmethod
    def redact(self) -> str:
        pass