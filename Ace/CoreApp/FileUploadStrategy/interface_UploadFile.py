from abc import ABC , abstractmethod
from . import MapColumn
class UploadFile(ABC):

    @abstractmethod
    def dopreProcessing(self, map_column_obj:MapColumn.SetColumnName):
        pass
    
    @abstractmethod
    def uploadFile(self):
        pass