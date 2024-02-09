from django.contrib import admin
from .models import ClassAttendance, ClassSchedule, Query, QueryComment

# Register your models here
admin.site.register(ClassSchedule)
admin.site.register(ClassAttendance)
admin.site.register(Query)
admin.site.register(QueryComment)