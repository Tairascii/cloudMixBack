from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import get_user_model

# Create your views here.


@api_view(['POST'])
def register(request):
    form = UserCreationForm(request.data)
    if form.is_valid():
        user = form.save()
        return Response({'message': 'User registered successfully', 'user_id': user.id},
                        status=status.HTTP_201_CREATED)
    return Response(form.errors, status=400)


@api_view(['POST'])
def login(request):
    form = AuthenticationForm(request, request.data)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            return Response({'message': 'User logged in', 'user_id': user.id},
                            status=status.HTTP_200_OK)
        return Response({'message': 'Wrong creds'}, status=400)
    return Response(form.errors, status=400)




