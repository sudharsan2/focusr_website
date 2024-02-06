from django.urls import path
from .views import save_api

urlpatterns =[
    path('post',save_api.as_view(),name='save_api')
]