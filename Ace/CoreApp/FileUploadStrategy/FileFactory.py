from ..Enums import SupportedFile
from . import UploadCSVFile
from . import  UploadExcelFile


class FileFactory:
    def __init__(self, file_name):
        self.file_name = file_name
    def returnFileObject(self, extension): 
        if extension == SupportedFile.FileExtension.SUPPORTED_FILE_EXTENSION.value[0]:
            return UploadExcelFile.UploadExcel(self.file_name)
        elif extension == SupportedFile.FileExtension.SUPPORTED_FILE_EXTENSION.value[1]:
            return UploadCSVFile.UploadCSV(self.file_name)
