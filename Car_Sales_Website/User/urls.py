from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('register/',views.Register,name="Register"),
    path('login/',views.Login.as_view(),name="Login"),
    path('logout/',LogoutView.as_view(),name="Logout"),
]