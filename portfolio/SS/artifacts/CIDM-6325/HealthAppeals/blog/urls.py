from django.urls import path
from django.contrib.auth import views as auth_views
from . import views  
from .views import PostListView, RegisterView

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='blog_home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
