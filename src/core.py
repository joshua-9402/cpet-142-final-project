import abc
import re


class RedactionEngine(abc.ABC):
    def __init__(self):
        self.__regex_email = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        self.__regex_phone = r'\b(?:\+?\d{1,3}[-.\s]?)?\(?\d{2,4}\)?[-.\s]?\d{3,4}[-.\s]?\d{3,4}\b'
        self.__regex_url = r'https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/[^\s]*)?'
        self.__regex_location = r'\b\d+\s[A-Za-z\s]+(?:St|Street|Ave|Avenue|Rd|Road|Blvd|Boulevard|Dr|Drive|Ln|Lane)(?:,\s*[A-Za-z\s]+)?(?:,?\s*[A-Z]{2})?(?:\s*\d{5})?\b'
        self.__regex_card = r'\b(?:\d{4}[-\s]?){3}\d{4}\b'
        self.__regex_date = r'\b(?:\d{1,4}[-./]\d{1,2}[-./]\d{1,4}|(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\.?\s+\d{1,2},?\s+\d{4})\b'

        self.REDACTION_MAP = {
            self.__regex_card: "[REDACTED_CARD]",
            self.__regex_url: "[REDACTED_URL]",
            self.__regex_email: "[REDACTED_EMAIL]",
            self.__regex_date: "[REDACTED DATE]",
            self.__regex_location: "[REDACTED_LOCATION]",
            self.__regex_phone: "[REDACTED_PHONE]"
        }

    @abc.abstractmethod
    def redact(self, text:str) -> str:
        pass


class TextRedactor(RedactionEngine):
    def redact(self, text: str) -> str:
        redacted_text = text
        for pattern, placeholder in self.REDACTION_MAP.items():
            redacted_text = re.sub(pattern, placeholder, redacted_text)
        return redacted_text


# # FOR INTERNAL TESTING ONLY !!!!!!
# if __name__ == "__main__":
#     redactor = TextRedactor()
#     print(redactor.redact("To: Customer Support (support@fintech-solutions.io)"))

