from django.urls import path
from .views import signup, user_login, home

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    
    # Add other URL patterns as needed
]
