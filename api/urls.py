from django.urls import path
from . import views

urlpatterns = [
    path('', views.simple_request, name='send_comment'),
    path('image/', views.image_request, name='send_image')
]
