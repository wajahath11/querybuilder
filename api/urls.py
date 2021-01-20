from django.urls import path
from .views import *


urlpatterns = [
    path('qurydata/',search_result.as_view())
]

