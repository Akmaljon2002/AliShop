from django.urls import path
from .views import *

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('bolimlar/', BolimlarView.as_view(), name='bolimlar'),
    path('bolim/<int:pk>/', BolimView.as_view(), name='bolim'),
]