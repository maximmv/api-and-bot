from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/',
         include([
             # path(r'auth/', include('djoser.urls')),
             # path('api-auth/', include('rest_framework.urls')),
             re_path(r'^rest-auth/', include('rest_auth.urls')),
             re_path(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
         ])),
]
