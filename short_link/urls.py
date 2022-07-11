from django.urls import path

from .views import LoginUser, LogoutUser, RegistrUser, short_link, redirect_to_orig, profile, index, short_succes

urlpatterns = [
    path('', index, name='index'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutUser.as_view(), name='logout'),
    path('registration/', RegistrUser.as_view(), name='registration'),
    path('short/', short_link, name='short'),
    path('short_succes/', short_succes, name='short_succes'),
    path('profile/', profile, name='profile'),
    path('<slug:short_id>/', redirect_to_orig, name='redirect'),
]
