from django.urls import path
from .views import *


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('profil/', ProfilView.as_view(), name='profil'),

]