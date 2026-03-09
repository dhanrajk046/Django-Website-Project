from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.service, name='services'),
    # path('contact/', views.contact, name='contact'),
    path('contact/', views.contact, name='contact'),
    # path('', views.home, name='home'),
]
