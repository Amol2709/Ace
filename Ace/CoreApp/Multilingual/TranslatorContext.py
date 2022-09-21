from . MultilingualTranslator import Translator
from .. Enums import MultiLingualTable
from . import FetchDataFromDB
import pandas as pd 
class TranslatorContext:
    def __init__(self):
        
        self.db_transaction = FetchDataFromDB.FetchData()
        map = self.db_transaction.fetchData()
        self.id = map['farmer_id']
        self.translator_obj = Translator(map)
     
    def translate(self):
        
        for tableName, code in MultiLingualTable.TableLanguageCode.TABLENAME_CODE.value:
            print(str(code))
            self.result = self.translator_obj.translate(str(code))
            self.result.append(self.id)
            print(self.result)
            self.result  = tuple(zip(*self.result))
            print(self.result)
            self.db_transaction.upDateDB(str(tableName),self.result)
        self.db_transaction.updateMainTable()
            
        

    