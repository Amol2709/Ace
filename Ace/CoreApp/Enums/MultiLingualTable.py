from enum import Enum

class TableLanguageCode(Enum):
    TABLENAME_CODE = [('CoreApp_farmerinfohindi','hi'),('CoreApp_farmerinfomarathi','mr'),
                    ('CoreApp_farmerinfopunjabi','pa'),('CoreApp_farmerinfotelugu','te')]
    TABLENAME_CODE_MAP = {'hi':'CoreApp_farmerinfohindi',
                        'mr':'CoreApp_farmerinfomarathi',
                        'te': 'CoreApp_farmerinfotelugu',
                        'pa': 'CoreApp_farmerinfopunjabi',
                        'en':'CoreApp_farmerinfo'
                            }


# print(FileExtension.SUPPORTED_FILE_EXTENSION.value[1])