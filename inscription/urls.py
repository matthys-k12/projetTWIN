from django.urls import path
from .views import inscription_view, confirmation_view

urlpatterns = [
    path('', inscription_view, name='inscription'),
    path('confirmation/<str:numero_inscription>/', confirmation_view, name='confirmation'),
]
