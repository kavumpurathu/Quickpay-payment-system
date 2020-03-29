from django.contrib import admin
# from .models import mobrecharge
# from .models import drecharge
from.models import wallet
from.models import complaints,recharge
from.models import spweb,serviceprovider,userregistration,offer
# Register your models here.
# admin.site.register(mobrecharge)
# admin.site.register(drecharge)
admin.site.register(wallet)
admin.site.register(complaints)
admin.site.register(spweb)
admin.site.register(serviceprovider)
admin.site.register(userregistration)
admin.site.register(offer)
admin.site.register(recharge)




