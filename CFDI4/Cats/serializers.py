from rest_framework import serializers
from . models import *

class CfdiFormaPago_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CfdiFormaPago
        fields = '__all__'
        ordering = 'formapagoclave'
        
class CfdiClaveUnidadMedida_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CfdiClaveUnidadMedida
        fields = '__all__'
        
        
class cfdiMonedas_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CfdiMonedas
        fields = '__all__'
        

class cfdiPais_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CfdiPais
        fields = '__all__'
        
class cfdiProductoServicio_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CfdiProductosServicios
        fields = '__all__'
        
class CfdiRegimenFiscal_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CfdiRegimenFiscal
        fields ='__all__'
        
class CfdiTipoRelacion_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CfdiTipoRelacion
        fields = '__all__'


class CfdiUso_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CfdiUso
        fields = '__all__'
        
class CfdiCodigoPostal_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CfdiCodigoPostal
        fields = '__all__'
        
class CfdiColonia_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CfdiColonia
        fields = '__all__'


class CfdiEstados_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CfdiEstados
        fields = '__all__'


class CfdiExportacion_Serailizer(serializers.ModelSerializer):
    class Meta:
        model = CfdiExportacion
        fields = '__all__'
        
        
class CfdiLocalidades_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CfdiLocalidades
        fields = '__all__'
        

class CfdiMotivoCancelacion_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CfdiMotivoCancelacion
        fields = '__all__'
        

class CfdiMunicipios_Serializer(serializers.ModelSerializer):
    class Meta:
        model =CfdiMunicipios
        fields = '__all__'
        

class CfdiObjetoimp_Serializer(serializers.ModelSerializer):
    class Meta:
        fields = CfdiObjetoimp
        fields = '__all__'


