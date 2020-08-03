from django.contrib import admin
from .models import *

admin.site.site_title = "Todo App Admin Area"
admin.site.site_header ="Todo App Admin"
admin.site.index_title = "Welcome to Todo App Admin Area"

# Register your models here.
admin.site.register(Todo)
