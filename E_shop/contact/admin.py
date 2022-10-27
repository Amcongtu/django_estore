from django.contrib import admin
from contact.models import *
# Register your models here.
admin.site.register(Location)
admin.site.register(StatusLocation)

admin.site.register(Contact)