from ..models import Blog
from rest_framework import serializers
from django.contrib.auth.models import User

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username","email","password"]

# {
# "username":"alert",
# "email":"alert@gmail.com",
# "password":"abhi@1234"
# }