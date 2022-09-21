from django.contrib import admin
from . models import FarmerInfo, FarmerInfoHindi,FarmerInfoMarathi,FarmerInfoPunjabi,FarmerInfoTelugu
# Register your models here.
admin.site.register(FarmerInfo)
admin.site.register(FarmerInfoMarathi)
admin.site.register(FarmerInfoHindi)
admin.site.register(FarmerInfoTelugu)
