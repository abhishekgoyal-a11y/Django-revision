from django.urls import path
from .views import *
urlpatterns = [
    path('get_blog/<str:title>/', get_blog, name="get_blog"),
    path('get_blog/', get_blog, name="get_blog"),
    path('create_blog/', create_blog, name="create_blog"),
    path('put_blog/<str:title>/', put_blog, name="put_blog"),
    path('delete_blog/<str:title>/', delete_blog, name="delete_blog"),
    path('pagination/', pagination.as_view(), name="pagination"),

    ###########################################USE API KEY################################################3

    path('get_blog_api/<str:api_key>/', get_blog_api, name="get_blog_api"),
    path('get_blog_api/<str:api_key>/<int:p_key>/', get_blog_api, name="get_blog_api"),
    path('update_blog_api/<str:api_key>/<int:p_key>/', update_blog_api, name="update_blog_api"),
    path('delete_blog_api/<str:api_key>/<int:p_key>/', delete_blog_api, name="delete_blog_api"),
    path('create_blog_api/<str:api_key>/', create_blog_api, name="create_blog_api"),
    path('get_api/', get_api, name="get_api"),
    path('registration_api/', registration_api, name="registration_api")

]
