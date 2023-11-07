from django.urls import path,include

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('linedance/', include('e_newline.urls')),
    path('golf/', include('d_golf.urls')),
    path('manager/', include('django.contrib.auth.urls')),
    path('manager/', include('manager.urls')),
   ]