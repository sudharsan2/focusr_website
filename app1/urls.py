from django.urls import path
from .views import save_api_enquery, save_api_apply

urlpatterns =[
    path('post/enquery',save_api_enquery.as_view(),name='save_api_apply'),
    path('post/apply', save_api_apply.as_view(),name='save_api_apply')
]