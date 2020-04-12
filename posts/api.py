from .models import Post, Like
from .serializers import PostSerializer, LikeSerializer, AuthorSerializer, AnalyticSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.db.models import Count, Q


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class LikeList(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


class AuthorList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = AuthorSerializer


class AnalyticList(APIView):

    def get(self, request):
        analytic = Like.objects.extra({'date': 'date(created)'}).values('date').annotate(
            liked=Count('id', filter=Q(like=True)),
            disliked=Count('id', filter=Q(like=False)),
        ).order_by('-date')
        serializer = AnalyticSerializer(analytic, many=True)

        return Response(serializer.data)
