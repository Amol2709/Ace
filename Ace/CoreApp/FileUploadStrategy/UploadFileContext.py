from .interface_UploadFile import  UploadFile
from . import FileFactory
class SaveFileToDB:
    def __init__(self, file_extension, file_name):
        self.file_name = file_name
        self.file_extension = file_extension
        obj = FileFactory.FileFactory(self.file_name)
        self.obj = obj.returnFileObject(self.file_extension)
        

    def dopreProcessing(self, map_column_object):
        self.obj.dopreProcessing(map_column_object)
    def saveFile(self):
        self.obj.uploadFile()

