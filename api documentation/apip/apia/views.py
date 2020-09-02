# from django.shortcuts import render, get_object_or_404
# from django.http import JsonResponse
# from .models import Poll


# def polls_list(request):
#     MAX_OBJECTS = 20
#     polls = Poll.objects.all()[:MAX_OBJECTS]
#     data = {"results": list(polls.values(
#         "question", "created_by__username", "pub_date"))}
#     return JsonResponse(data)


# def polls_detail(request, pk):
#     poll = get_object_or_404(Poll, pk=pk)
#     data = {"results": {
#         "question": poll.question,
#         "created_by": poll.created_by.username,
#         "pub_date": poll.pub_date
#     }}
#     return JsonResponse(data)

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from django.shortcuts import get_object_or_404
# from .models import Poll, Choice
# from .serializers import PollSerializer


# class PollList(APIView):
#     def get(self, request):
#         polls = Poll.objects.all()[:20]
#         data = PollSerializer(polls, many=True).data
#         return Response(data)


# class PollDetail(APIView):
#     def get(self, request, pk):
#         poll = get_object_or_404(Poll, pk=pk)
#         data = PollSerializer(poll).data
#         return Response(data)


# from rest_framework import generics
# from .models import Poll, Choice
# from .serializers import PollSerializer, ChoiceSerializer, VoteSerializer


# class PollList(generics.ListCreateAPIView):
#     queryset = Poll.objects.all()
#     serializer_class = PollSerializer


# class PollDetail(generics.RetrieveDestroyAPIView):
#     queryset = Poll.objects.all()
#     serializer_class = PollSerializer


# class ChoiceList(generics.ListCreateAPIView):
#     queryset = Choice.objects.all()
#     serializer_class = ChoiceSerializer


# class CreateVote(generics.CreateAPIView):
#     serializer_class = VoteSerializer


# from rest_framework import generics
# from rest_framework.views import APIView
# from rest_framework import status
# from rest_framework.response import Response
# from .models import Poll, Choice
# from .serializers import PollSerializer, ChoiceSerializer, VoteSerializer


# class ChoiceList(generics.ListCreateAPIView):
#     serializer_class = ChoiceSerializer
#     def get_queryset(self):
#         queryset = Choice.objects.filter(poll_id=self.kwargs["pk"])
#         return queryset


# class CreateVote(APIView):
#     serializer_class = VoteSerializer

#     def post(self, request, pk, choice_pk):
#         voted_by = request.data.get("voted_by")
#         data = {'choice': choice_pk, 'poll': pk, 'voted_by': voted_by}
#         serializer = VoteSerializer(data=data)
#         if serializer.is_valid():
#             vote = serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from django.contrib import auth
# from rest_framework import generics
# from .serializers import PollSerializer, ChoiceSerializer, VoteSerializer, UserSerializer


# class UserCreate(generics.CreateAPIView):
#     authentication_classes = ()
#     permission_classes = ()
#     serializer_class = UserSerializer


# class LoginView(APIView):
#     permission_classes = ()

#     def post(self, request,):
#         username = request.data.get("username")
#         password = request.data.get("password")
#         user = auth.authenticate(username=username, password=password)
#         if user:
#             print(user.id)
#             return Response({"token": user.auth_token.key})
#         else:
#             return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)


from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib import auth
from .models import Poll
from .serializers import PollSerializer


class LoginView(APIView):
    permission_classes = ()

    def post(self, request,):
        username = request.data.get("username")
        password = request.data.get("password")
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return Response({"success": "Credentials are correct"})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)


class polllist(APIView):
    def get(self, request):
        data = Poll.objects.all()
        serialize = PollSerializer(data, many=True).data
        return Response({"data": serialize}, status=status.HTTP_200_OK)


# {
# "username":"bala5",
# "password":"bala5"
# }
