from .. DBConnection import  EstablishConnection

class UpdateDB:
    def __init__(self, tableName, value):
        self.tableName = tableName
        self.value = value
        self.dbconn_obj = EstablishConnection.ReturnConnection()
    def update(self):
        conn=self.dbconn_obj.newConnection()
        cursor = conn.cursor() 
        stmt= ('INSERT INTO "{}" (first_name,last_name,state_name,district_name,village_name,phone)'"VALUES (%s,%s,%s,%s,%s,%s)".format(self.tableName))
        cursor.executemany(stmt,self.value)
        conn.commit()
        conn.close()
    