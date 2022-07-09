from django.urls import path

from .views import show_hello, Log, Out, Registr, short_link, redirect_to_orig, profile

urlpatterns = [
    path('', show_hello, name='main'),
    path('login/', Log.as_view(), name='login'),
    path('logout/', Out.as_view(), name='logout'),
    path('registration/', Registr.as_view(), name='registration'),
    path('short/', short_link, name='short'),
    path('profile/', profile, name='profile'),
    path('<slug:short_id>/', redirect_to_orig, name='redirect'),
]
