from ..API import  API_Context

class Translator:
    def __init__(self, map):
        self.api_obj = API_Context.TextTranslator()
        self.first_name = map['first_name']
        self.last_name = map['last_name']
        self.state_name = map['state_name']
        self.village_name = map['village_name']
        self.district_name = map['district_name']
        self.phone = map['phone']
        self.farmer_id = map['farmer_id']
        self.input_data = [self.first_name, self.last_name, self.state_name, self.district_name, self.village_name, self.phone]
        
        
    def translate(self,language_code):
        self.output_data=[]
        for i in range(len(self.input_data)):
            tmp=[]
            result = self.api_obj.translate_text(language_code,self.input_data[i])
            #print(result)
            for j in range(len(result)):
                tmp.append(result[j]['translatedText'])
            self.output_data.append(tmp)
        return self.output_data
