from django.urls import path
from .views import *
urlpatterns = [

    path('FormaPago/', FormaPagoList.as_view()),
    path('FormaPago/<str:formapagoclave>/', FormaPagoList.as_view()),
    
    path('UniMed/', ClaveUnidadMedidaList.as_view()),
    path('UniMed/<str:unidadmedidaclave>/', ClaveUnidadMedidaList.as_view()),
    
    path('Monedas/', MonedasList.as_view()),
    path('Monedas/<str:monedaclave>/', MonedasList.as_view()),
    
    path('Pais/', PaisList.as_view()),
    path('Pais/<str:paisclave>/', PaisList.as_view()),
    
    path('ProdServ/', ProductosServiciosList.as_view()),
    path('ProdServ/<str:productoclave>/', ProductosServiciosList.as_view()),
    
    path('RegimenFiscal/', RegimenFiscalList.as_view()),
    path('RegimenFiscal/<str:regimenfiscalclave>/', RegimenFiscalList.as_view()),
    
    path('TipoRelacion/', TipoRelacionList.as_view()),
    path('TipoRelacion/<str:tiporelacionclave>/', TipoRelacionList.as_view()),
    
    path('Uso/', UsoList.as_view()),
    path('Uso/<str:usoclave>/', UsoList.as_view()),
    
    path('CP/', CodigoPostalList.as_view()),
    path('CP/<str:codigopostal>/', CodigoPostalList.as_view()),
    
    path('Estados/', EstadosList.as_view()),
    path('Estados/<str:estado>/', EstadosList.as_view()),
]