from django.urls import path
from . import views


urlpatterns = [
    path('',views.getRoutes),
    path('fundings/', views.getFundings),
    path('funding/<str:pk>', views.getFunding),
]