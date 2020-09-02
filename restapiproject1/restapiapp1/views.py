from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
# TUTORIAL
# parwiz forogh


# # generic view set
# class articleviewset(viewsets.GenericViewSet):
#     same as generic_api_view


# # Viewset


class articleviewset(viewsets.ViewSet):
    def list(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Article.objects.all()
        article = get_object_or_404(queryset, pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def delete(self, request, pk=None):
        queryset = Article.objects.all()
        article = get_object_or_404(queryset, pk=pk)
        article.delete()

    def update(self, request, pk=None):
        article = Article.objects.get(id=pk)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

# generic based view
# class generic_api_view(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
#                        mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
#     serializer_class = ArticleSerializer
#     queryset = Article.objects.all()
#     lookup_field = 'id'
#     # authentication_classes = [SessionAuthentication, BasicAuthentication]
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]

#     def get(self, request, id=None):
#         if id:
#             return self.retrieve(request)
#         else:
#             return self.list(request)

#     def post(self, request):
#         return self.create(request)

#     def put(self, request, id=None):
#         return self.update(request, id)

#     def delete(self, request, id):
#         return self.destroy(request, id)


# # class based views
# class Article_class_list(APIView):
#     def get(self, request):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#         return Response(serializer.data)


# class Article_class_onebyone(APIView):
#     def get_object(self, pk):
#         try:
#             return Article.objects.get(id=pk)
#         except Article.DoesNotExist:
#             return HttpResponse(status=status.HTTP_404_NOT_FOUND)

#     def get(self, request, pk):
#         article = self.get_object(pk)
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         article = self.get_object(pk)
#         serializer = ArticleSerializer(instance=article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#         return Response(serializer.data)

#     def delete(self, request, pk):
#         article = self.get_object(pk)
#         article.delete()


# function based views
# using Response

@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == "GET":
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    if request.method == "POST":
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def article_onebyone(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == "GET":
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_201_CREATED)
    elif request.method == "DELETE":
        article.delete()
        return Response(status=status.HTTP_201_CREATED)

# #  using rest JsonResponse

# @csrf_exempt
# def article_list(request):
#     if request.method == "GET":
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return JsonResponse(serializer.data, safe=False)
#     if request.method == "POST":
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         else:
#             return JsonResponse(serializer.errors, status=400)


# @csrf_exempt
# def article_onebyone(request, pk):
#     article = Article.objects.get(pk=pk)
#     if request.method == "GET":
#         serializer = ArticleSerializer(article)
#         return JsonResponse(serializer.data)
#     elif request.method == "PUT":
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(article, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         else:
#             return JsonResponse(serializer.errors, status=400)
#     elif request.method == "DELETE":
#         article.delete()
#         return HttpResponse(status=204)
