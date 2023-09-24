from django.contrib import admin
from django.urls import path
from campaign import views as campaign_views

urlpatterns = [
    path('', campaign_views.home, name='home'),
    path('admin/', admin.site.urls),
    path('register/', campaign_views.register, name='register'),
    path('about_us/register/', campaign_views.register, name='about_us_register'),
    path('contact_us/register/', campaign_views.register, name='contact_us_register'),
    path('med_info/', campaign_views.med_info_view, name='med_info'),
    path('volunteer/', campaign_views.volunteer_view, name='volunteer'),
    path('login/', campaign_views.loginView, name='login'),
    path('about_us/login/', campaign_views.loginView, name='about_us_login'),
    path('contact_us/login/', campaign_views.loginView, name='contact_us_login'),
    path('logout/', campaign_views.logoutUser, name='logout'),
    path('about_us/logout/', campaign_views.logoutUser, name='about_us_logout'),
    path('contact_us/logout/', campaign_views.logoutUser, name='contact_us_logout'),
    path('contact_us/', campaign_views.contact_us, name='Contact Us'),
    path('about_us/', campaign_views.about_us, name='About Us')
]
