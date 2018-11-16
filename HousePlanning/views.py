from django.contrib import messages
from django.contrib.auth import REDIRECT_FIELD_NAME, logout
from django.shortcuts import render, redirect
from django.urls import reverse

from django.contrib import messages
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.shortcuts import render, redirect
from django.urls import reverse


# from sf_frontend.exceptions import AuthenticationError
# from sf_frontend.views.auth_views import try_login_user


# def go_to_login(request, redirect_field_name=REDIRECT_FIELD_NAME):
#     redirect_to = request.POST.get(redirect_field_name,
#                                    request.GET.get(redirect_field_name, reverse('home')))

#     if request.user.is_authenticated:
#         return redirect(redirect_to)

#     if not request.POST:
#         return render(request, 'login.html', {'redirect_to': redirect_to})

#     username = request.POST.get('username', '')
#     password = request.POST.get('password', '')

#     try:
#         if try_login_user(request, username, password):
#             return redirect(redirect_to)
#     except AuthenticationError as e:
#         messages.error(request, e.error)
#         return redirect(go_to_login)


# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login
# from sf_frontend.exceptions import AuthenticationError

# def try_login_user(request, username, password):

#     if not (username and password):
#         raise AuthenticationError(error='Sign-in credentials not entered.')

#     user = authenticate(username=username, password=password)
#     if user is None:
#         raise AuthenticationError(error='Incorrect login credentials provided.')

#     if not user.is_active:
#         raise AuthenticationError(error='The account is currently disabled.')

#     login(request, user)
#     return True



def IndexPage(request):

    code = request.GET.get('code', None)
    state = request.GET.get('state', None)
    if code and state:
        return redirect(HomePage, code=code)

    return render(request, 'index.html', {'code': code})


def HomePage(request, code):
    basicParam = 'OTkyNGI3NGYtMzZhNy00NThhLWFmZTYtYzNhOWY5ZjI3MGI3OmRlNWU1MzdkLWEzYmMtNDhhMS1hNDU1LTkyOWRkYjQ4MmE2ZA=='
    headers = {'Authorization': 'Basic ' + basicParam,
               'grant_type': 'token',
               'code': code
              }

    print(headers)

    return render(request, 'house.html')


def LogoutPage(request):
    logout(request)
    return redirect(IndexPage)
