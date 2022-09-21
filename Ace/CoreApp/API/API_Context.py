from . import API_Main
from . import GoogleAPI_Adapter

class TextTranslator:
    def __init__(self):
        self.obj = API_Main.API(GoogleAPI_Adapter.GoogleAPIAdapter())
    def translate_text(self,target,text):
        return self.obj.translateText(target, text)