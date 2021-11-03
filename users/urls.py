
from django.urls import path

from users.views import login, logout, profile
from users.views import UserRegistrationView

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('profile/', profile, name='profile'),
    path('logout/', logout, name='logout'),

]