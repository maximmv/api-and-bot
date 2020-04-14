import datetime
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
        analytic_qs = Like.objects.all()
        date_from = self.request.query_params.get('date_from', None)
        date_to = self.request.query_params.get('date_to', None)

        if date_from:
            try:
                date_from = datetime.datetime.strptime(date_from, '%Y-%m-%d')
                analytic_qs = analytic_qs.filter(created__gte=date_from)
            except ValueError:
                pass
        if date_to:
            try:
                date_to = datetime.datetime.strptime(date_to, '%Y-%m-%d')
                date_to = date_to + datetime.timedelta(days=1)
                analytic_qs = analytic_qs.filter(created__lt=date_to)
            except ValueError:
                pass

        analytic_qs = analytic_qs.extra({'date': 'date(created)'}).values('date').annotate(
            liked=Count('id', filter=Q(like=True)),
            disliked=Count('id', filter=Q(like=False)),
        ).order_by('-date')
        serializer = AnalyticSerializer(analytic_qs, many=True)

        return Response(serializer.data)
