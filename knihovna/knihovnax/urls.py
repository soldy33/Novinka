from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'pridat', views.KnihovnaViewSet, basename='pridat')

urlpatterns = [
    path('', include(router.urls)),
    path('tabulka/', views.knihovna_tabulka, name='knihovna_tabulka'),
    path('prodlouzit/<int:knihovna_id>/', views.prodlouzit_vypujcku, name='prodlouzit'),
    path('smazat/', views.zobrazit_tabulku_a_smazat_knihu, name='smazat_knihu_tabulka')]

