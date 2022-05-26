from django.contrib import admin

from .models import MenuItem, Restaurant, School, Student

admin.site.register(Student)
admin.site.register(School)
admin.site.register(Restaurant)
admin.site.register(MenuItem)
