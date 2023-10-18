"""
URL configuration for tripplanner project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'), #not working
    path('trip/', views.trip_detail, name='trip_detail'), #not working
    path('register/', views.register, name='register'), 
    path('login/', views.user_login, name='login'), #{'template_name': 'login.html'} #not working
    path('logout/', views.user_logout, name='logout'),#not working
    path('profile/', views.profile, name='profile'), #not working
    path('create_booking/', views.create_booking, name='create_booking'),
    path('booking_success/', views.booking_success, name='booking_success'),
    path('manage_bookings/', views.manage_bookings, name='manage_bookings'), #not working
    path('submit_review/', views.submit_review, name='submit_review'),
    path('review_success/', views.review_success, name='review_success'),
    path('trip_reviews/', views.trip_reviews, name='trip_reviews'), #not working
]

#urlpatterns = [
#    