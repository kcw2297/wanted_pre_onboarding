from django.urls import path
from . import views


urlpatterns = [
    path('login/',views.loginUser,name='login'),
    path('userregister/',views.registerUser,name='userRegister'),
    path('logout/',views.logoutUser, name='logout')
]