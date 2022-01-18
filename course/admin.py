from django.contrib import admin

from course.models import *

# Register your models here.
admin.site.register(subject)
admin.site.register(course)
admin.site.register(teacher)
admin.site.register(teacher_app)
admin.site.register(userDetail)
admin.site.register(userCourse)
admin.site.register(certificate)