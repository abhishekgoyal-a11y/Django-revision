from .views import *
from django.urls import path, include
from rest_framework.routers import DefaultRouter

##router = DefaultRouter()
##router.register('article', articleviewset, basename='anythingyoucangive')


urlpatterns = [
    path('article_list/', articleviewset, name='article_list'),
    path('article_list/<int:id>/',
         articleviewset, name='article_list'),
    # path('article_onebyone/<int:pk>/',
    #      Article_class_onebyone.as_view(), name='article_onebyone')
]
