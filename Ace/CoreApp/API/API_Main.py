from . interface_TranslationAPI import TranslationAPI
class API:
    def __init__(self, api:TranslationAPI):
        self.api = api 
    def translateText(self,target, text):
        return self.api.translate_text(target, text)