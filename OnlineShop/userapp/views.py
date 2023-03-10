from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.shortcuts import render, redirect
from django.views import View


class RegisterView(View):
    def get(self, request):
        return render(request, 'page-user-register.html')
    def post(self, request):
        if request.POST.get('p') == request.POST.get('cp'):
            user = User.objects.create_user(
                username = request.POST.get('email'),
                password = request.POST.get('p')
            )
            Profil.objects.create(
                ism = f"{request.POST.get('f_n')} {request.POST.get('l_n')}",
                jins = request.POST.get('gender'),
                user = user
            )
        return redirect("/user/login/")

class ProfilView(View):
    def get(self, request):
        return render(request, 'page-profile-main.html')