from django.urls import path
from .views import TesView

urlpatterns = [
    path("", TesView.as_view(), name="test")
]