from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_jwt.views import refresh_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/',
         include([
             re_path(r'^rest-auth/', include('rest_auth.urls')),
             re_path(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
             re_path(r'^refresh-token/', refresh_jwt_token),
             path('', include('posts.urls')),
         ])),
]
