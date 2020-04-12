from django.urls import path
from posts import api

urlpatterns = [
    path('posts/', api.PostList.as_view()),
    path('posts/<int:pk>/', api.PostDetail.as_view()),
    path('likes/', api.LikeList.as_view()),
    path('authors/', api.AuthorList.as_view()),
    path('authors/<int:pk>/', api.AuthorDetail.as_view()),
    path('analytic/', api.AnalyticList.as_view()),
]
