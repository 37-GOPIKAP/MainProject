from django.contrib import admin
from accounts.models import *
#from django.contrib.auth.admin import UserAdmin
# Register your models here.
admin.site.register(User)
admin.site.register(Institution)
admin.site.register(SchoolManager)
admin.site.register(Principal)
admin.site.register(AdmStaff)
admin.site.register(Teacher)
admin.site.register(Students)
admin.site.register(Parent)

