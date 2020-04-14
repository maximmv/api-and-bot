from django.urls import path
from posts import api

urlpatterns = [
    path('post/', api.PostList.as_view()),
    path('post/<int:pk>/', api.PostDetail.as_view()),
    path('like/', api.LikeList.as_view()),
    path('author/', api.AuthorList.as_view()),
    path('author/<int:pk>/', api.AuthorDetail.as_view()),
    path('analytic/', api.AnalyticList.as_view()),
]
