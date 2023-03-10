from django.db.models import Sum
from django.shortcuts import render, redirect
from django.views import View
from .models import *
from asosiy.models import Mahsulot
from userapp.models import Profil



class SavatView(View):
    def get(self, request):
        savatlar = Savat.objects.filter(profil__user=request.user)
        summa = savatlar.aggregate(Sum('umumiy')).get('umumiy__sum')
        chegirmalar = 0
        for savat in savatlar:
            chegirmalar += savat.miqdor*(savat.mahsulot.chegirma*savat.mahsulot.narx)/100
        content = {
            'savatlar': Savat.objects.filter(profil__user=request.user),
            'summa':summa,
            'chg':round(chegirmalar, 2),
            'yakuniy':summa - round(chegirmalar, 2)
        }
        return render(request, 'page-shopping-cart.html', content)

class SavatQView(View):
    def get(self, request, pk):
        savat = Savat.objects.get(id=pk)
        if savat.profil.user == request.user:
            savat.miqdor += 1
            savat.umumiy = savat.miqdor*savat.mahsulot.narx
            savat.save()
        return redirect("savat")

# 2
class SavatgaQoshView(View):
    def get(self, request, pk):
        mahsulot = Mahsulot.objects.get(id=pk)
        if Savat.objects.filter(profil__user=request.user , mahsulot=mahsulot).first() is None:
            Savat.objects.create(
                mahsulot = mahsulot,
                umumiy = mahsulot.narx,
                profil = Profil.objects.get(user=request.user)
            )
            return redirect(f"/asosiy/mahsulot/{pk}/")
        savat = Savat.objects.get(profil__user=request.user , mahsulot=mahsulot)
        savat.miqdor += 1
        savat.umumiy = savat.miqdor * savat.mahsulot.narx
        savat.save()
        return redirect(f"/asosiy/mahsulot/{pk}/")

# 3
class SavatdanOchirView(View):
    def get(self, request, pk):
        savat = Savat.objects.get(id=pk)
        if savat.profil.user == request.user:
            savat.delete()
        return redirect("savat")


# 1
class TanlanganQoshView(View):
    def get(self, request, pk):
        tanlangan = Tanlangan.objects.filter(profil__user=request.user, mahsulot__id=pk)
        if tanlangan.first() is None:
            Tanlangan.objects.create(
                profil = Profil.objects.get(user=request.user),
                mahsulot = Mahsulot.objects.get(id=pk)
            )
        else:
            tanlangan.delete()
        return redirect("savat")


class SavatKView(View):
    def get(self, request, pk):
        savat = Savat.objects.get(id=pk)
        if savat.profil.user == request.user and savat.miqdor != 1:
            savat.miqdor -= 1
            savat.umumiy = savat.miqdor*savat.mahsulot.narx
            savat.save()
        return redirect("savat")

class TanlanganOchirView(View):
    def get(self, request, pk):
        tanlangan = Tanlangan.objects.get(id=pk)
        if tanlangan.profil.user == request.user:
            tanlangan.delete()
        return redirect("tanlangan")


class TanlanganView(View):
    def get(self, request):
        content = {
            'tanlanganlar':Tanlangan.objects.filter(profil__user=request.user)
        }
        return render(request, 'page-profile-wishlist.html', content)

class BuyurtmaView(View):
    def get(self, request):
        return render(request, 'page-profile-orders.html')
