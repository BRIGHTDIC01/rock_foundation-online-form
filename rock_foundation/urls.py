from django.contrib import admin
from django.urls import path
from admissions import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('apply/', views.apply, name='apply'),
]