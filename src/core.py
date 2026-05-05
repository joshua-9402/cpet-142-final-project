import abc


class Redactor(abc.ABC):
    def __init__(self, text_line: str):
        self.text_line = text_line

    @abc.abstractmethod
    def readline(self):
        pass

    @abc.abstractmethod
    def writeline(self):
        pass

    @abc.abstractmethod
    def redact(self) -> str:
        return self.text_line