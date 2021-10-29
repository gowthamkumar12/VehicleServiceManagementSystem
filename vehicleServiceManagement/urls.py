"""vehicleServiceManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from vehicle.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name='index'),
    path('user_login',user_login, name='user_login'),
    path('admin_login',admin_login, name='admin_login'),
    path('user_home',user_home, name='user_home'),
    path('admin_home',admin_home, name='admin_home'),
    path('logout',Logout, name='logout'),
    path('add_mechanic',add_mechanic,name='add_mechanic'),
    path('manage_mechanic',manage_mechanic, name='manage_mechanic'),
    path('edit_mechanic/<int:pid>',edit_mechanic,name='edit_mechanic'),
    path('add_category',add_category, name='add_category'),
    path('manage_category',manage_category, name='manage_category'),
    path('edit_category/<int:pid>',edit_category,name='edit_category'),
    path('register',register,name='register'),
    path('termsandcondition',termsandcondition,name='termsandcondition'),
    path('enquiry_form',enquiry_form,name='enquiry_form'),
    path('enquiry_history',enquiry_history,name='enquiry_history'),
    path('add_enquirytype',add_enquirytype, name='add_enquirytype'),
    path('view_enquirytype',view_enquirytype, name='view_enquirytype'),
    path('delete_enquirytype/<int:pid>',delete_enquirytype,name='delete_enquirytype'),
    path('delete_mechanic/<int:pid>',delete_mechanic,name='delete_mechanic'),
    path('delete_category/<int:pid>',delete_category,name='delete_category'),
    path('changepasswordadmin',changepasswordadmin, name='changepasswordadmin'),
    path('changepassworduser',changepassworduser, name='changepassworduser'),
    path('user_profile',user_profile, name='user_profile'),
    path('service_request',service_request,name='service_request'),
    path('service_history',service_history,name='service_history'),
    path('reg_users',reg_users,name='reg_users'),
    path('pending_service',pending_service,name='pending_service'),
    path('rejected_services',rejected_services,name='rejected_services'),
    path('view_service_request/<int:pid>',view_service_request,name='view_service_request'),
    path('pending_servicing',pending_servicing,name='pending_servicing'),
    path('view_service/<int:pid>',view_service,name='view_service'),
    path('completed_service',completed_service,name='completed_service'),
    path('notrespond_enquiry',notrespond_enquiry,name='notrespond_enquiry'),
    path('respond_enquiry',respond_enquiry,name='respond_enquiry'),
    path('view_enquiry/<int:pid>',view_enquiry,name='view_enquiry'),
    path('search_enquiry',search_enquiry,name='search_enquiry'),
    path('search_service',search_service,name='search_service'),
    path('service_view/<int:pid>',service_view, name='service_view'),
    path('enquiry_view/<int:pid>',enquiry_view, name='enquiry_view'),
]
