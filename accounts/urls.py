from django.urls import path
from . import views
from .views import UserProfileView

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('profile/<username>/', UserProfileView.as_view(), name='user-profile'),
]
