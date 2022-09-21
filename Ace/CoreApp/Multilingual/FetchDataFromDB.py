from .. DBConnection import  EstablishConnection
import pandas as pd
class FetchData:
    def __init__(self):
        self.dbconn_obj = EstablishConnection.ReturnConnection()
        self.conn  = self.dbconn_obj.newConnection()
    def fetchData(self):
        
        df = pd.read_sql_query('SELECT id, first_name, last_name, state_name, village_name, district_name, phone from "CoreApp_farmerinfo" where status={}'.format(False),con= self.conn)
        print(df.head())
        farmer_id = list(df['id'])
        f_name  = list(df['first_name'])
        l_name = list(df['last_name'])
        state_name = list(df['state_name'])
        village_name  = list(df['village_name'])
        district_name = list(df['district_name'])
        phone = list(df['phone'])
        context = {
            'first_name':f_name,
            'last_name':l_name,
            'state_name':state_name,
            'village_name':village_name,
            'district_name':district_name,
            'phone':phone,
            'farmer_id':farmer_id
        }
        return context
    def upDateDB(self,tableName,value):
        self.cursor = self.conn.cursor() 
        stmt= ('INSERT INTO "{}" (first_name,last_name,state_name,district_name,village_name,phone,farmer_id)'"VALUES (%s,%s,%s,%s,%s,%s,%s)".format(tableName))
        #value=tuple(zip(first_name_list, last_name_list,state_name_list, district_name_list,village_name_list, contact_number_list  ))
        self.cursor.executemany(stmt,value)
        self.conn.commit()
    def updateMainTable(self):
        stmt= 'UPDATE "CoreApp_farmerinfo"  SET status={} '.format(True)
        self.cursor.execute(stmt)
        self.conn.commit()
        

        