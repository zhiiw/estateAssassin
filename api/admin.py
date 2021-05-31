from django.contrib import admin
from .models import User,House,HouseOfCase,LocationOfHouse,Intermediary

admin.site.register(User)
admin.site.register(House)
admin.site.register(HouseOfCase)
admin.site.register(LocationOfHouse)
admin.site.register(Intermediary)

# Register your models here.
