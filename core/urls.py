from django.urls import path
from .views import dashboard
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
