from . import views
from django.urls import path

urlpatterns = [
  path("",views.home,name="home"),
  path('overview/', views.overview, name='overview'),
  path('learning/', views.learning, name='learning'),
]