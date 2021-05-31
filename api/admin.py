from django.contrib import admin
from .models import User,House,HouseCase,LocationOfHouse,Intermediary,Case

admin.site.register(User)
admin.site.register(House)
admin.site.register(HouseCase)
admin.site.register(Case)
admin.site.register(LocationOfHouse)
admin.site.register(Intermediary)

# Register your models here.
