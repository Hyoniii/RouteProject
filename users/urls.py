from django.urls import path, include
from .views import TestView

urlpatterns = [
    path('kakao/login', TestView.as_view())
]
