from django.urls import path
from . import views
urlpatterns = [
    path('',views.Home,name='HomePage'),
    path('product/<int:pid>',views.Product_view,name='productpage')
]