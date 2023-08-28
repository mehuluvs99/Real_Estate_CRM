from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('users/', views.user_list, name='users'),
    path('add_inquiry/', views.add_inquiry, name='add_inquiry'),
    path('account/', views.accounts, name='account'),
    path('upload_inquiry/', views.upload_file, name='upload_inquiry'),
    path('payment/', views.payment, name='payment'),
    path('agent/', views.agent, name='agent'),
]