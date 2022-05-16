from django.urls import path
from accounts import views

urlpatterns = [
    #path('customer_register/',views.customer_register.as_view(), name='customer_register'),
    #path('manager_login',views.ManagerLoginView.as_view(),name='manager_login'),
    #path('manager_signup',views.manager_signup,name='manager_signup')
    path('manager_signup',views.manager_signup.as_view(),name='manager_signup'),
    path('manager_login/',views.manager_login, name='manager_login'),
]