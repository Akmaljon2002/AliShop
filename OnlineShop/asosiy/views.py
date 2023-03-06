from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from .models import *

# 1
class LoginView(View):
    def get(self, request):
        return render(request, 'page-user-login.html')

    def post(self, request):
        user = authenticate(username = request.POST.get('l'),
                            password = request.POST.get('p'))
        if user is None:
            return redirect("/")
        login(request, user)
        return redirect("/asosiy/home/")

# 2
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("/")

# 3
class RegisterView(View):
    def get(self, request):
        return render(request, 'page-user-register.html')

class Home2View(View):
    def get(self, request):
        return render(request, 'page-index-2.html')

class HomeView(View):
    def get(self, request):
        data = {
            'bolimlar':Bolim.objects.all()[:7],
            'chegirmalilar':Mahsulot.objects.filter(chegirma__gt=0).order_by('-chegirma')[:5]
        }
        return render(request, 'page-index.html', data)

class BolimlarView(View):
    def get(self, request):
        data = {
            'bolimlar':Bolim.objects.all()
        }
        return render(request, 'page-category.html', data)

class BolimView(View):
    def get(self, request, pk):
        data = {
            'mahsulotlar':Mahsulot.objects.filter(bolim__id=pk)
        }
        return render(request, 'page-listing-grid.html', data)