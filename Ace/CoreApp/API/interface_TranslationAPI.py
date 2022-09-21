from abc import ABC , abstractmethod

class TranslationAPI(ABC):

    @abstractmethod
    def translate_text(target, text):
        pass