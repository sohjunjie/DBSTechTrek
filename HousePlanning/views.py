from django.contrib import messages
from django.contrib.auth import REDIRECT_FIELD_NAME, logout
from django.shortcuts import render, redirect
from django.urls import reverse

from django.contrib import messages
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.shortcuts import render, redirect
from django.urls import reverse


def IndexPage(request):

    code = request.GET.get('code', None)
    state = request.GET.get('state', None)
    if code and state:
        return redirect(HomePage, code)

    return render(request, 'index.html')


def HomePage(request, code):

    basicParam = 'OTkyNGI3NGYtMzZhNy00NThhLWFmZTYtYzNhOWY5ZjI3MGI3OmRlNWU1MzdkLWEzYmMtNDhhMS1hNDU1LTkyOWRkYjQ4MmE2ZA=='
    headers = {'Authorization': 'Basic ' + basicParam,
               'grant_type': 'token',
               'code': code
              }

    # ret = requests.post(url, headers = headers, data = json.dumps({"homeLoanApplicants":{"dateOfBirth":"1988-01-01", "fixedMonthlyIncome": {"amount": income}}}))

    # print(headers)

    return render(request, 'postlogin.html')


def LogoutPage(request):
    logout(request)
    return redirect(IndexPage)
