
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.authtoken.models import Token



from django.contrib.auth.models import User,auth
from ..models import Blog
from .serializers import BlogSerializer


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_blog(request, title=None):
    if request.method == "GET":
        if title is not None:
            blog = Blog.objects.get(title=title)
            serialize = BlogSerializer(blog, many=False)
            return Response(serialize.data)
        else:
            blog = request.user.blog_set.all()
            serialize = BlogSerializer(blog, many=True)
            return Response(serialize.data)


@api_view(['POST'])
def create_blog(request):
    if request.method == "POST":
        serialize = BlogSerializer(data=request.data)
        if serialize.is_valid():
            blog=serialize.save()
            blog.author=request.user
            blog.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialize.errors, status=status.HTTP_404_BAD_REQUEST)



@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
def put_blog(request, title):
    if request.method == "PUT":
        blog = Blog.objects.get(title=title)
        user = request.user
        if blog.author != user:
            return Response({
                "Response": "not have permission to update"
            })

        serialize = BlogSerializer(blog, data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialize.errors, status=status.HTTP_404_BAD_REQUEST)


@api_view(['DELETE'])
def delete_blog(request, title):
    if request.method == "DELETE":
        blog = Blog.objects.get(title=title)

        user = request.user
        if blog.author != user:
            return Response({
                "Response": "not have permission to update"
            })

        blog.delete()
        return Response(status=status.HTTP_201_CREATED)


class pagination(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('title', 'description')



@api_view(['GET'])
def get_blog_api(request, api_key):
    if request.method == "GET":
        try:
            username=Token.objects.get(key=api_key).user
            username_id=User.objects.get(username=username).id
            blogs=Blog.objects.filter(author=username_id)
            serialize = BlogSerializer(blogs, many=True)
            return Response(serialize.data)
        except:
            return Response({"error":"no api found"})


@api_view(['POST'])
def create_blog_api(request,api_key):
    if request.method == "POST":
        serialize = BlogSerializer(data=request.data)
        if serialize.is_valid():
            blog=serialize.save()
            blog.author=Token.objects.get(key=api_key).user
            blog.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialize.errors, status=status.HTTP_404_BAD_REQUEST)



@api_view(['POST'])
def get_api(request):
    if request.method=="POST":
        username = request.data.get("username")
        password = request.data.get("password")
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            return Response({"Api Key":Token.objects.get(user=user).key})
        else:
            return Response({"error":"user is not found"})