
from Cats.models import CfdiFormaPago
from .models import *
from .serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import generics 
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class ExamplePagination(PageNumberPagination):       
       page_size = 20

class FormaPagoList(generics.ListAPIView):
    pagination_class = PageNumberPagination
    queryset = CfdiFormaPago.objects.all().order_by('formapagoclave')
    serializer_class = CfdiFormaPago_Serializer
    def get_queryset(self, *args, **kwargs):        
        if len(self.kwargs) != 0 :            
            return self.queryset.filter(formapagoclave__icontains=self.kwargs['formapagoclave'])            
        else:
            return super().get_queryset()
class MonedasList(generics.ListAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]    
    pagination_class = ExamplePagination 
    queryset = CfdiMonedas.objects.all().order_by('monedaclave')
    serializer_class = cfdiMonedas_Serializer
    
    def get_queryset(self, *args, **kwargs):        
        if len(self.kwargs) != 0 :            
            return self.queryset.filter(monedaclave__icontains=self.kwargs['monedaclave'])            
        else:
            return super().get_queryset()


class PaisList(generics.ListAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    
    pagination_class = PageNumberPagination
    queryset = CfdiPais.objects.all().order_by('paisclave')
    serializer_class = cfdiPais_Serializer
    
    def get_queryset(self, *args, **kwargs):        
        if len(self.kwargs) != 0 :            
            return self.queryset.filter(paisclave__icontains=self.kwargs['paisclave'])            
        else:
            return super().get_queryset()


class ProductosServiciosList(generics.ListAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    pagination_class = ExamplePagination
    queryset = CfdiProductosServicios.objects.all().order_by('productoclave')
    serializer_class = cfdiProductoServicio_Serializer

    def get_queryset(self, *args, **kwargs):        
        if len(self.kwargs) != 0 :            
            return self.queryset.filter(productoclave__icontains=self.kwargs['productoclave'])            
        else:
            return super().get_queryset()
    

class RegimenFiscalList(generics.ListAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    
    pagination_class = PageNumberPagination
    queryset = CfdiRegimenFiscal.objects.all().order_by('regimenfiscalclave')
    serializer_class = CfdiRegimenFiscal_Serializer
    
    def get_queryset(self, *args, **kwargs):        
        if len(self.kwargs) != 0 :            
            return self.queryset.filter(regimenfiscalclave__icontains=self.kwargs['regimenfiscalclave'])            
        else:
            return super().get_queryset()
    

class TipoRelacionList(generics.ListAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    
    pagination_class = PageNumberPagination
    queryset = CfdiTipoRelacion.objects.all().order_by('tiporelacionclave')
    serializer_class = CfdiTipoRelacion_Serializer
    
    def get_queryset(self, *args, **kwargs):        
        if len(self.kwargs) != 0 :            
            return self.queryset.filter(tiporelacionclave__icontains=self.kwargs['tiporelacionclave'])            
        else:
            return super().get_queryset()


class UsoList(generics.ListAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    
    pagination_class = PageNumberPagination
    queryset = CfdiUso.objects.all().order_by('usoclave')
    serializer_class = CfdiUso_Serializer
    
    def get_queryset(self, *args, **kwargs):        
        if len(self.kwargs) != 0 :            
            return self.queryset.filter(usoclave__icontains=self.kwargs['usoclave'])            
        else:
            return super().get_queryset()
        

class CodigoPostalList(generics.ListAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    
    pagination_class = PageNumberPagination
    queryset = CfdiCodigoPostal.objects.all().order_by('codigopostal')
    serializer_class = CfdiCodigoPostal_Serializer
    
    def get_queryset(self, *args, **kwargs):        
        if len(self.kwargs) != 0 :            
            return self.queryset.filter(codigopostal__icontains=self.kwargs['codigopostal'])            
        else:
            return super().get_queryset()


class ColoniasList(generics.ListAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    
    pagination_class = PageNumberPagination
    queryset = CfdiColonia.objects.all().order_by('colonia')
    serializer_class = CfdiColonia_Serializer
    
    def get_queryset(self, *args, **kwargs):        
        if len(self.kwargs) != 0 :            
            return self.queryset.filter(colonia__icontains=self.kwargs['colonia'])            
        else:
            return super().get_queryset()


class EstadosList(generics.ListAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    
    pagination_class = PageNumberPagination
    queryset = CfdiEstados.objects.all().order_by('estado')
    serializer_class = CfdiEstados_Serializer
    
    def get_queryset(self, *args, **kwargs):        
        if len(self.kwargs) != 0 :            
            return self.queryset.filter(estado__icontains=self.kwargs['estado'])            
        else:
            return super().get_queryset()
       
class ClaveUnidadMedidaList(generics.ListAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination
    queryset = CfdiClaveUnidadMedida.objects.all().order_by('unidadmedidaclave')
    serializer_class = CfdiClaveUnidadMedida_Serializer
    
    
    def dispatch(self, request, *args, **kwargs):
        #print('-------------------dispatch', kwargs, request.method)
        if request.method == 'POST':
            kwargs.pop('unidadmedidaclave', None)
        """
        `.dispatch()` is pretty much the same as Django's regular dispatch,
        but with extra hooks for startup, finalize, and exception handling.
        """
        self.args = args
        self.kwargs = kwargs
        request = self.initialize_request(request, *args, **kwargs)
        self.request = request
        self.headers = self.default_response_headers  # deprecate?
        
        try:
            self.initial(request, *args, **kwargs)

            # Get the appropriate handler method
            if request.method.lower() in self.http_method_names:
                handler = getattr(self, request.method.lower(),
                                  self.http_method_not_allowed)
            else:
                handler = self.http_method_not_allowed

            response = handler(request, *args, **kwargs)

        except Exception as exc:
            response = self.handle_exception(exc)

        self.response = self.finalize_response(request, response, *args, **kwargs)
        return self.response
    
    
    def post(self, request, format=None):
        #print('--------------------------',self.kwargs)
        serializer = CfdiClaveUnidadMedida_Serializer(data=request.data)                    
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, *args, **kwargs):
        #print('--------------get------------')
        return self.list(request, *args, **kwargs)
    def get_queryset(self, *args, **kwargs): 
        #print('-----------query------------')
        if len(self.kwargs) != 0 :            
            return self.queryset.filter(unidadmedidaclave__icontains=self.kwargs['unidadmedidaclave'])            
        else:
            return super().get_queryset()
