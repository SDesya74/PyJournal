from django.contrib import admin
from main.models import Student, Teacher, Subject, Mark

# Register your models here.
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(Mark)