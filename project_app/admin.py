from django.contrib import admin
from project_app.models import User, Course, Section,TA

# Register your models here.
admin.site.register(User)
admin.site.register(TA)
admin.site.register(Course)
admin.site.register(Section)





