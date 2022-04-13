from django.urls import path
from . import views

urlpatterns = [
    path('',views.fundings, name="fundings"),
    path('register/',views.registerFunding, name="register"),
    path('detail/<str:pk>/',views.viewDetail, name='detail')
]


