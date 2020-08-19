from django.urls import path
from .views import *
urlpatterns = [
    path('get_blog/<str:title>', get_blog, name="get_blog"),
    path('get_blog/', get_blog, name="get_blog"),
    path('create_blog/', create_blog, name="create_blog"),
    path('put_blog/<str:title>', put_blog, name="put_blog"),
    path('delete_blog/<str:title>', delete_blog, name="delete_blog"),
]
