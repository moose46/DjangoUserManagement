# Author: Robert W. Curtiss
# urls.py was created on August 13 2021 @ 10:13 AM
# Project: DjangoUserManagement
from django.conf.urls import url
from django.urls import path, include

from users import views

urlpatterns = [
    url(r'^accounts/', include("django.contrib.auth.urls")),
    url(r'^register/', views.register, name="register"),
    path('', views.dashboard, name='dashboard'),
]
