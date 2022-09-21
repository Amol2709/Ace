class SetColumnName:
    def __init__(self):
        self.first_name_col = None 
        self.last_name_col = None 
        self.state_name_col  = None
        self.village_name_col = None
        self.district_name_col = None
        self.contact_number_col = None
    
    def setFirstNameCol(self, first_name):
        self.first_name_col = first_name
        return self

    def setLastNameCol(self, last_name):
        self.last_name_col = last_name
        return self 

    def setStateNameCol(self, state_name):
        self.state_name_col = state_name
        return self

    def setVillageNameCol(self, village_name):
        self.village_name_col = village_name
        return self 

    def setDistricNameCol(self, district_name):
        self.district_name_col = district_name
        return self
    
    def setContactNumberCol(self, contact_number):
        self.contact_number_col = contact_number
        return self
    
    def getFirstNameCol(self):
        return self.first_name_col
    
    def getLastNameCol(self):
        return self.last_name_col

    def getStateNameCol(self):
        return self.state_name_col
    
    def getVillageNameCol(self):
        return self.village_name_col
    
    def getDistrictNameCol(self):
        return self.district_name_col
    
    def getContactNumberCol(self):
        return self.contact_number_col