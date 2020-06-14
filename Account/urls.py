
from django.urls import path 
from . import views
urlpatterns = [
    path('',views.Register,name='SiginUp'),
    path('siginup/',views.SiginUp_Handle,name='SiginUp'),
]

