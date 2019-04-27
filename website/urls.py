from django.urls import path
from website import views
from django.contrib import admin
from django.conf.urls import url
from django.views.generic import TemplateView


admin.autodiscover()

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('contato/', views.contato, name='contato'),
    path('artista/', views.Artista.as_view(), name='artista'),
    path('aonde/', views.Aonde.as_view(), name='aonde'),
    path('trabalhos/', views.trabalhos, name='trabalhos'),
    url(r'^(?P<slug>[-\w]+)$', views.AlbumDetail.as_view(), name='album'),
    url(r'^robots\.txt/$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    url(r'^sitemap\.xml/$', TemplateView.as_view(template_name='sitemap.xml', content_type='application/xml')),
]
