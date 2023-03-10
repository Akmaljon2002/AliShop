from django.urls import path
from .views import *

urlpatterns = [
    path('savat/', SavatView.as_view(), name='savat'),
    path('savat_q/<int:pk>/', SavatQView.as_view(), name='savat-q'),
    path('savatga_qosh/<int:pk>/', SavatgaQoshView.as_view(), name='savatga-qosh'),
    path('ochirish/<int:pk>/', SavatdanOchirView.as_view(), name='ochirish'),
    path('tanlangan_qosh/<int:pk>/', TanlanganQoshView.as_view(), name='tanlangan-qosh'),
    path('savat_k/<int:pk>/', SavatKView.as_view(), name='savat-k'),
    path('tanlangan_ochir/<int:pk>/', TanlanganOchirView.as_view(), name='tanlangan-ochir'),
    path('tanlangan/', TanlanganView.as_view(), name='tanlangan'),
    path('', BuyurtmaView.as_view(), name='buyurtma'),

]