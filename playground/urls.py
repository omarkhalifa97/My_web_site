from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile),
    path('submit/', views.submit),

]