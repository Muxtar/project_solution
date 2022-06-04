from django.urls import path
from accounts.views import loginView, registerView, logoutView, profileView

urlpatterns = [
    path('login/', loginView, name = 'login'),
    path('register/', registerView, name='register'),
    path('logout/', logoutView, name='logout'),
    path('profile/', profileView, name='profile')
]