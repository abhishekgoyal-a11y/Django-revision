
from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class BlogForm(ModelForm):
	class Meta:
		model = Blog
		fields=["title","image","description"]
		exclude=("author",)


class RegistrationForm(UserCreationForm):
	class Meta:
		model = User
		fields = ["username","email","password1","password2"]


class CustomerProfileForm(ModelForm): 
    class Meta: 
        model = CustomerProfile 
        fields = ['profile_image']




