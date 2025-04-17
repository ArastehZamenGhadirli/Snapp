from .views import RequestTaxi
from django.urls import path


urlpatterns = [
    path('reqruestTaxi/',RequestTaxi.as_view())
]
