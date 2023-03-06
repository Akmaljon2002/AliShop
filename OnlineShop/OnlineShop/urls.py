from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from asosiy.views import Home2View, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('asosiy/', include('asosiy.urls')),
    path('buyurtma/', include('buyurtma.urls')),
    path('user/', include('userapp.urls')),
    path('', Home2View.as_view(), name='home2'),
    path('logout/', LogoutView.as_view(), name='logout'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
