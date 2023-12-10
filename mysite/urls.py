from django.contrib.auth import views 
from django.urls import include, path


urlpatterns = [
    path('cloud/', include('cloud.urls')),
]
