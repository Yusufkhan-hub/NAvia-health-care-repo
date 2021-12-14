from django.urls import path
from .views import search_api,search_api_view


urlpatterns = [
    path('search_api/',search_api,name='search_api'),
    path('search_api_view/',search_api_view.as_view()),
]
