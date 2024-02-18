from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update/<str:pk>', views.update, name='update'),
    path('delete/<str:pk>', views.delete, name='delete'),
    path('findex', views.findex, name='findex'),
    path('register', views.register, name='index'),
    path('login', views.login, name='login'),
]