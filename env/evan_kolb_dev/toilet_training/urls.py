from django.urls import path, re_path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('add_trainee/', views.add_trainee_view, name='add_trainee'),
    re_path(r'^active_session/(?P<alias>\w+)/', views.active_session_view, name='active_session'),
    re_path(r'^trainee_data/(?P<alias>\w+)/', views.trainee_data_view, name='trainee_data')
]
