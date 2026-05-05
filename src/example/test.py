import re

regex_email = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
regex_phone = r'\b(?:\+?\d{1,3}[-.\s]?)?\(?\d{2,4}\)?[-.\s]?\d{3,4}[-.\s]?\d{3,4}\b'
regex_url = r'https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/[^\s]*)?'
regex_location = r'\b\d+\s[A-Za-z\s]+(?:St|Street|Ave|Avenue|Rd|Road|Blvd|Boulevard|Dr|Drive|Ln|Lane)(?:,\s*[A-Za-z\s]+)?(?:,?\s*[A-Z]{2})?(?:\s*\d{5})?\b'
regex_card = r'\b(?:\d{4}[-\s]?){3}\d{4}\b'
regex_date = r'\b(?:\d{1,4}[-./]\d{1,2}[-./]\d{1,4}|(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\.?\s+\d{1,2},?\s+\d{4})\b'

REDACTION_MAP = {
    regex_card: "[REDACTED_CARD]",
    regex_url: "[REDACTED_URL]",
    regex_email: "[REDACTED_EMAIL]",
    regex_date: "[READCTED DATE]",
    regex_location: "[REDACTED_LOCATION]",
    regex_phone: "[REDACTED_PHONE]"
}

output = ""

with open("test.txt", "r") as test:
    for line in test.readlines():

        redacted_text = line
        for pattern, placeholder in REDACTION_MAP.items():
            redacted_text = re.sub(pattern, placeholder, redacted_text)

        output += redacted_text

print(output)