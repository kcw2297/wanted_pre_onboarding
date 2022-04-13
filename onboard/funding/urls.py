from django.urls import path
from . import views

urlpatterns = [
    path('',views.Fundings, name="fundings"),
    path('funding/<str:pk>/',views.FundingObj, name='funding'),
    path('create-funding/',views.CreateFunding, name="create-funding"),
    path('update-funding/<str:pk>',views.UpdateFunding,name='update-funding'),
    path('delete-funding/<str:pk>',views.DeleteFunding,name='delete-funding'),
]


