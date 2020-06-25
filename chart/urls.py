# chart/urls.py
from django.contrib import admin
from django.urls import path
from chart import views                                     # !!!

urlpatterns = [
    path('', views.home, name='home'),

    path('ticket-class/2/',
         views.ticket_class_view_2, name='ticket_class_view_2'),


    path('covid19_korea/',
         views.covid19_korea, name='covid19_korea'),


    path('admin/', admin.site.urls),
]