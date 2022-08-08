from django.urls import path
from . import views

urlpatterns = [
    path('', views.CatalogListView.as_view(), name='catalog'),
    path('dlya_tela/', views.dlya_tela, name='dlya_tela'),
    path('face/', views.face, name='face'),
    path('dlya_volos/', views.dlya_volos, name='dlya_volos'),
    path('skin_type/', views.skin_type, name='skin_type'),
    path('dry_skin/', views.dry_skin, name='dry_skin'),
    path('normal_skin/', views.normal_skin, name='normal_skin'),
    path('oil_skin/', views.oil_skin, name='oil_skin'),
    path('<int:pk>/', views.catalog_detail, name='catalog_detail'),

]