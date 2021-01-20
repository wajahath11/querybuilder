from django.urls import path
from django.urls.conf import re_path
from .views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('qurydata/',search_result.as_view())
]
urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='upwork/build/index.html'))]