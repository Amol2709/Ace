import psycopg2
from django.conf import settings
class ReturnConnection:
	def __init__(self):
		self.user_name = settings.DATABASES['default']['USER']
		self.password = settings.DATABASES['default']['PASSWORD']
		self.host = settings.DATABASES['default']['HOST']
		self.database_name = settings.DATABASES['default']['NAME']
		self.port_number= settings.DATABASES['default']['PORT']
	def newConnection(self):
		try:
			#Establishing connection
			self.conn = psycopg2.connect(user=self.user_name, password=self.password, host=self.host, database=self.database_name,port=self.port_number)
		except (Exception, psycopg2.Error) as error :
			print("Failed to Established Connection".format(error))
		else:
			return self.conn