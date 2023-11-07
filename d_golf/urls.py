from django.urls import path

from . import views


urlpatterns = [
    path('', views.golf, name='golf'),
     path('add_golfer/', views.add_golfer, name= "add_golfer"),
     path('add_scores/', views.add_scores, name= "add_scores"),
   ]