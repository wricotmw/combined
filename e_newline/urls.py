from django.urls import path

from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.line, name='line'),
    path('linedances', views.linedances, name='linedances'),
    path('search_dance', views.search_dance, name='search_dance'),
    path('video_test/<id>, <name>', views.video_test, name='video_test'),
    path('add_dance', views.add_dance, name='add-dance'),
    path('ammend_dance', views.ammend_dance, name='ammend_dance'),
    path('ammendment/ <dances_id>', views.ammendment, name='ammendment'),
   

   ]

urlpatterns += staticfiles_urlpatterns()