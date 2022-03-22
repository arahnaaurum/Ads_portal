from django.shortcuts import render, redirect, reverse
# from django.views.generic.edit import CreateView
from django.views.generic import View
from random import randint

from django.contrib.auth.models import User
from .models import OneTimeCode


class RegisterView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'sign/register.html', {})

    def post(self, request, *args, **kwargs):
        user = str(request.user)
        username = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        code = randint(100, 1000)

        otc = OneTimeCode(user=user, username=username, code=code, email=email, password=password)  # создаём объект OneTimeCode
        otc.save()
        return redirect('../finish')


class RegisterFinView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'sign/registerfin.html', {})

    def post(self, request, *args, **kwargs):
        code = int(request.POST['code'])
        user = str(request.user)
        search = OneTimeCode.objects.get(user=user)
        if search.code == code:
            newuser = User(username=search.username, email=search.email)
            newuser.set_password(str(search.password))
            newuser.save()
            search.delete()
        else:
            raise ValueError('Wrong code')
        return redirect('../')