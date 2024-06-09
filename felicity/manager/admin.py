from django.contrib import admin
from .models import SelfInfo, Buyer, Invoice, Challan, Entry, User, ChallanEntry
# Register your models here.

admin.site.register(SelfInfo)
admin.site.register(Buyer)
admin.site.register(Invoice)
admin.site.register(Challan)
admin.site.register(Entry)
admin.site.register(ChallanEntry)