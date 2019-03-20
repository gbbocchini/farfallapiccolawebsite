from django.urls import path
from website import views
from website import forms
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import url

admin.autodiscover()

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('contato/', views.contato, name='contato'),
    path('artista/', views.Artista.as_view(), name='artista'),
    path('aonde/', views.Aonde.as_view(), name='aonde'),
    path('trabalhos/', views.trabalhos, name='trabalhos'),
    url(r'^(?P<slug>[-\w]+)$', views.AlbumDetail.as_view(), name='album'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
