from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/<int:id>', views.post_detail, name='post_detail'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
