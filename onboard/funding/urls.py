from django.urls import path
from . import views

urlpatterns = [
    path('',views.fundings, name="fundings")
]


