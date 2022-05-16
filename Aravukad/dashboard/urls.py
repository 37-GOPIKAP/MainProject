from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('Manager/',views.Manager,name='Manager'),
    path('AdmnStaff/',views.AdmnStaff,name='AdmnStaff'),
    path('Principal/',views.Principal,name='Principal'),
    path('Teacher/',views.Teacher,name='Teacher'),
    path('Students/',views.Students,name='Students'),
    path('Parent/',views.Parent,name='Parent'),
]