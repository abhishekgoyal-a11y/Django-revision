from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name="home"),
    path('login_page', login_page, name='login_page'),
    path('logout', logout, name='logout'),
    path('registration', registration, name='registration'),
    path('createblogpage', createblogpage, name='createblogpage'),
    path('viewblog', viewblog, name='viewblog'),
    path('deleteblog/<int:pk>/', deleteblog, name='deleteblog'),
    path('updateblog/<int:pk>/', updateblog, name='updateblog'),
    path('customer_profile/', customer_profile, name='customer_profile'),
    # path('hotel_image_view/', hotel_image_view, name='hotel_image_view'),
    # path('success/', success, name='success')
]
