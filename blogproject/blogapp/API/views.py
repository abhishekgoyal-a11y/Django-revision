
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter

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
    if request.user.is_superuser:
        if request.method == "POST":
            serialize = BlogSerializer(data=request.data)
            if serialize.is_valid():
                serialize.save()
                return Response(serialize.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serialize.errors, status=status.HTTP_404_BAD_REQUEST)
    else:
        return Response({
            "Response": "not have permission to create"
        })


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
    search_fields = ('title', 'message', 'description')
