from . import interface_UploadFile
import pandas as pd
from .. DBConnection import  EstablishConnection


class UploadExcel(interface_UploadFile.UploadFile):
    def __init__(self,file_name):
        self.file_name  =  file_name
        self.dbconn_obj = EstablishConnection.ReturnConnection()
    def dopreProcessing(self, map_col_obj):
        self.map_col_obj = map_col_obj
        nan_value = float("NaN")
        
        self.df = pd.read_excel('CoreApp/UploadedFiles/'+self.file_name)
        self.df.replace("", nan_value, inplace=True)
        print(map_col_obj.getFirstNameCol())
        print(self.df.head())
        print(list(self.df.columns))
        print(map_col_obj.getFirstNameCol() in list(self.df.columns))
        self.df=self.df.dropna(subset=[self.map_col_obj.getFirstNameCol()])
       
    def uploadFile(self):
        first_name_list = list(self.df[self.map_col_obj.getFirstNameCol()])
        last_name_list = list(self.df[self.map_col_obj.getLastNameCol()])
        state_name_list = list(self.df[self.map_col_obj.getStateNameCol()])
        district_name_list = list(self.df[self.map_col_obj.getDistrictNameCol()])
        village_name_list = list(self.df[self.map_col_obj.getVillageNameCol()])
        contact_number_list = list(self.df[self.map_col_obj.getContactNumberCol()])
        status = [False]*len(contact_number_list)
        #print(first_name_list, last_name_list,state_name_list, district_name_list,village_name_list, contact_number_list)

        conn=self.dbconn_obj.newConnection()
        cursor = conn.cursor() 
        stmt= ('INSERT INTO "CoreApp_farmerinfo" (first_name,last_name,state_name,district_name,village_name,phone,status)'"VALUES (%s,%s,%s,%s,%s,%s,%s)")
        value=tuple(zip(first_name_list, last_name_list,state_name_list, district_name_list,village_name_list, contact_number_list,status  ))
        cursor.executemany(stmt,value)
        conn.commit()
        conn.close()

        