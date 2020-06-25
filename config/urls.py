# chart/urls.py
from django.contrib import admin
from django.urls import path, include
from chart import views                                     # !!!

urlpatterns = [
    path('', include('chart.urls')),
    path('covid19_korea/',
         views.covid19_korea, name='covid19_korea'),  # !!!
    path('admin/', admin.site.urls),
]