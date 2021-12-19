from django.contrib import admin

# Register your models here.
from .models import Students, User

admin.site.register(Students)
admin.site.register(User)
