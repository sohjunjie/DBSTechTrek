from django.contrib import messages
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.shortcuts import render, redirect
from django.urls import reverse



def IndexPage(request):
    return render(request, 'index.html')
