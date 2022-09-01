from django.db import models

class CfdiAduana(models.Model):
    aduanaclave = models.CharField(db_column='ADUANACLAVE', primary_key=True, max_length=4)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=254, blank=True, null=True)  # Field name made lowercase.
    class Meta:
        db_table = 'CFDI_Aduana'


class CfdiClaveUnidadMedida(models.Model):
    unidadmedidaclave = models.CharField(db_column='UNIDADMEDIDACLAVE', primary_key=True, max_length=5)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=120, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    nota = models.CharField(db_column='NOTA', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    simbolo = models.CharField(db_column='SIMBOLO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    class Meta:
        db_table = 'CFDI_ClaveUnidadMedida'


class CfdiDocumentosRelacionados(models.Model):
    sysid_dr = models.IntegerField(db_column='SYSID_DR', primary_key=True)  # Field name made lowercase.
    uuid = models.CharField(db_column='UUID', max_length=99, blank=True, null=True)  # Field name made lowercase.
    tipocfdi = models.CharField(db_column='TIPOCFDI', max_length=34)  # Field name made lowercase.
    consecutivo_tipocfd = models.IntegerField(db_column='CONSECUTIVO_TIPOCFD')  # Field name made lowercase.
    tiporelacion = models.CharField(db_column='TIPORELACION', max_length=2, blank=True, null=True)  # Field name made lowercase.
    class Meta:
        db_table = 'CFDI_DocumentosRelacionados'


class CfdiDocumentosRelacionadosFI(models.Model):
    sysid_dr = models.IntegerField(db_column='SYSID_DR', primary_key=True)  # Field name made lowercase.
    uuid = models.CharField(db_column='UUID', max_length=99, blank=True, null=True)  # Field name made lowercase.
    consecutivo_tipocfd = models.IntegerField(db_column='CONSECUTIVO_TIPOCFD')  # Field name made lowercase.
    class Meta:
        db_table='CFDI_DocumentosRelacionadosFI'


class CfdiFormaPago(models.Model):
    formapagoclave = models.CharField(db_column='FORMAPAGOCLAVE', primary_key=True, max_length=10)
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=80, blank=True, null=True)
    class Meta:
        db_table='CFDI_Formapago'
    

class CfdiImpuestos(models.Model):
    impuestoclave = models.CharField(db_column='IMPUESTOCLAVE', primary_key=True, max_length=4)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=20, blank=True, null=True)  # Field name made lowercase.
    retencion = models.CharField(db_column='RETENCION', max_length=2, blank=True, null=True)  # Field name made lowercase.
    traslado = models.CharField(db_column='TRASLADO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    local = models.CharField(db_column='LOCAL', max_length=10, blank=True, null=True)  # Field name made lowercase.
    entidadaplica = models.CharField(db_column='ENTIDADAPLICA', max_length=20, blank=True, null=True)  # Field name made lowercase.
    class Meta:
        db_table = 'CFDI_Impuestos'

class CfdiMetodoPago(models.Model):
    metodopagoclave = models.CharField(db_column='METODOPAGOCLAVE', primary_key=True, max_length=5)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=120, blank=True, null=True)  # Field name made lowercase.
    class Meta:
        db_table = 'CFDI_Metodopago'

class CfdiMonedas(models.Model):
    monedaclave = models.CharField(db_column='MONEDACLAVE', primary_key=True, max_length=5)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=120, blank=True, null=True)  # Field name made lowercase.
    decimales = models.IntegerField(db_column='DECIMALES', blank=True, null=True)  # Field name made lowercase.
    porcentajevariacion = models.CharField(db_column='PORCENTAJEVARIACION', max_length=10, blank=True, null=True)  # Field name made lowercase.
    class Meta:
        db_table = 'CFDI_Monedas'


class CfdiPais(models.Model):
    paisclave = models.CharField(db_column='PAISCLAVE', primary_key=True, max_length=3)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=120, blank=True, null=True)  # Field name made lowercase.
    class Meta:
        db_table ='CFDI_Pais'

class CfdiPatente(models.Model):
    patenteclave = models.CharField(db_column='PATENTECLAVE', primary_key=True, max_length=4)  # Field name made lowercase.
    class Meta:
        db_table = 'CFDI_Patente'


class CfdiProductosServicios(models.Model):
    productoclave = models.CharField(db_column='PRODUCTOCLAVE', primary_key=True, max_length=10)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=254, blank=True, null=True)  # Field name made lowercase.
    incluirivatraslado = models.CharField(db_column='INCLUIRIVATRASLADO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    incluiriepstraslado = models.CharField(db_column='INCLUIRIEPSTRASLADO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    complementoincluir = models.CharField(db_column='COMPLEMENTOINCLUIR', max_length=20, blank=True, null=True)  # Field name made lowercase.
    class Meta:
        db_table = 'CFDI_ProductosServicios'

class CfdiRegimenFiscal(models.Model):
    regimenfiscalclave = models.CharField(db_column='REGIMENFISCALCLAVE', primary_key=True, max_length=3)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=254, blank=True, null=True)  # Field name made lowercase.
    fisica = models.CharField(db_column='FISICA', max_length=2, blank=True, null=True)  # Field name made lowercase.
    moral = models.CharField(db_column='MORAL', max_length=2, blank=True, null=True)  # Field name made lowercase.
    class Meta:
        db_table = 'CFDI_RegimenFiscal'


class CfdiTasaCuota(models.Model):
    impuesto = models.CharField(db_column='IMPUESTO', primary_key=True, max_length=5)  # Field name made lowercase.
    valormaximo = models.DecimalField(db_column='VALORMAXIMO', max_digits=17, decimal_places=7)  # Field name made lowercase.
    rango = models.CharField(db_column='RANGO', max_length=10)  # Field name made lowercase.
    valorminimo = models.DecimalField(db_column='VALORMINIMO', max_digits=17, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    factor = models.CharField(db_column='FACTOR', max_length=10, blank=True, null=True)  # Field name made lowercase.
    traslado = models.CharField(db_column='TRASLADO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    retencion = models.CharField(db_column='RETENCION', max_length=2, blank=True, null=True)  # Field name made lowercase.
    class Meta:
        db_table = 'CFDI_Tasacuota'
        
        
class CfdiTipoDeComprobante(models.Model):
    tipocomprobanteclave = models.CharField(db_column='TIPOCOMPROBANTECLAVE', primary_key=True, max_length=3)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=80, blank=True, null=True)  # Field name made lowercase.
    class Meta:
        db_table = 'CFDI_TipoDeComprobante'

class CfdiTipoFactor(models.Model):
    tipofactorclave = models.CharField(db_column='TIPOFACTORCLAVE', primary_key=True, max_length=20)  # Field name made lowercase.
    class Meta:
        db_table='CFDI_TipoFactor'
        
        
class CfdiTipoRelacion(models.Model):
    tiporelacionclave = models.CharField(db_column='TIPORELACIONCLAVE', primary_key=True, max_length=5)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=120, blank=True, null=True)  # Field name made lowercase.
    class Meta:
        db_table= 'CFDI_TipoRelacion'

class CfdiUso(models.Model):
    usoclave = models.CharField(db_column='USOCLAVE', primary_key=True, max_length=5)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=120, blank=True, null=True)  # Field name made lowercase.
    fisica = models.CharField(db_column='FISICA', max_length=2, blank=True, null=True)  # Field name made lowercase.
    moral = models.CharField(db_column='MORAL', max_length=2, blank=True, null=True)  # Field name made lowercase.
    class Meta:
        db_table= 'CFDI_Uso'

class CfdiCodigoPostal(models.Model):
    codigopostal = models.CharField(db_column='CODIGOPOSTAL', primary_key=True, max_length=10)  # Field name made lowercase.
    estado = models.CharField(db_column='ESTADO', max_length=3, blank=True, null=True)  # Field name made lowercase.
    municipio = models.CharField(db_column='MUNICIPIO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    localidad = models.CharField(db_column='LOCALIDAD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    class Meta:
        db_table = 'CFDI_CodigoPostal'
    
class CfdiClaveprodSTCC(models.Model):
    clave_stcc = models.CharField(db_column='Clave_STCC', primary_key=True, max_length=9)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=155, blank=True, null=True)  # Field name made lowercase.
    class Meta:
        db_table = 'CFDI_ClaveprodSTCC'
        
class CfdiClavetipoCarga(models.Model):
    clave_tipo_carga = models.CharField(db_column='Clave_Tipo_Carga', primary_key=True, max_length=3)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=65, blank=True, null=True)  # Field name made lowercase.
    class Meta:
        db_table = 'CFDI_ClavetipoCarga'
        
class CfdiClaveUnidadPeso(models.Model):
    clave_unidad = models.CharField(db_column='Clave_Unidad', primary_key=True, max_length=4)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=155)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=999, blank=True, null=True)  # Field name made lowercase.
    class Meta:
        db_table = 'CFDI_ClaveUnidadPeso'

class CfdiCodigoTransporteAereo(models.Model):
    clave_identificacion = models.CharField(db_column='Clave_Identificacion', primary_key=True, max_length=6)  # Field name made lowercase.
    nacionalidad = models.CharField(db_column='Nacionalidad', max_length=64, blank=True, null=True)  # Field name made lowercase.
    nombre_aerolinea = models.CharField(db_column='Nombre_aerolinea', max_length=155, blank=True, null=True)  # Field name made lowercase.
    oaci = models.CharField(db_column='OACI', max_length=5, blank=True, null=True)  # Field name made lowercase.
    class Meta:
        db_table = 'CFDI_CodigoTransporteAereo'

class CfdiColonia(models.Model):
    colonia = models.CharField(db_column='COLONIA', primary_key=True, max_length=5)  # Field name made lowercase.
    cp = models.CharField(db_column='CP', max_length=8)  # Field name made lowercase.
    nombre_asentamiento = models.CharField(db_column='NOMBRE_ASENTAMIENTO', max_length=150, blank=True, null=True)  # Field name made lowercase.
    class Meta:
        db_table = 'CFDI_Colonia'
        
class CfdiConfigAutoTransporte(models.Model):
    clave_nomenclatura = models.CharField(db_column='Clave_Nomenclatura', primary_key=True, max_length=7)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    numero_ejes = models.CharField(db_column='Numero_Ejes', max_length=3, blank=True, null=True)  # Field name made lowercase.
    numero_llantas = models.CharField(db_column='Numero_llantas', max_length=25, blank=True, null=True)  # Field name made lowercase.
    class Meta:
        db_table = 'CFDI_ConfigAutoTransporte'

class CfdiConfigMaritima(models.Model):
    clave_conf_maritima = models.CharField(db_column='Clave_Conf_Maritima', primary_key=True, max_length=4)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=64, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'CFDI_ConfigMaritima'


class CfdiContenedor(models.Model):
    clave_contenedor = models.CharField(db_column='Clave_Contenedor', primary_key=True, max_length=5)  # Field name made lowercase.
    tipo_contenedor = models.CharField(db_column='Tipo_Contenedor', max_length=4, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=155, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'CFDI_Contenedor'


class CfdiContenedorMaritimo(models.Model):
    clave_contenedor_maritimo = models.CharField(db_column='Clave_Contenedor_Maritimo', primary_key=True, max_length=6)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=65, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'CFDI_ContenedorMaritimo'


class CfdiCveTransporteCP(models.Model):
    clave_transporte = models.CharField(db_column='Clave_Transporte', primary_key=True, max_length=2)  # Field name made lowercase.
    descripcion_transporte = models.CharField(db_column='Descripcion_Transporte', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'CFDI_CveTransporteCP'


class CfdiDerechosDePaso(models.Model):
    clave_derecho_peso = models.CharField(db_column='Clave_Derecho_Peso', primary_key=True, max_length=7)  # Field name made lowercase.
    derecho_peso = models.CharField(db_column='Derecho_peso', max_length=7, blank=True, null=True)  # Field name made lowercase.
    entre = models.CharField(db_column='Entre', max_length=155, blank=True, null=True)  # Field name made lowercase.
    hasta = models.CharField(db_column='Hasta', max_length=155, blank=True, null=True)  # Field name made lowercase.
    otorga_recibe = models.CharField(db_column='Otorga_Recibe', max_length=55, blank=True, null=True)  # Field name made lowercase.
    concesionario = models.CharField(db_column='Concesionario', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'CFDI_DerechosDePaso'


class CfdiEstaciones(models.Model):
    clave_transporte = models.CharField(db_column='Clave_Transporte', primary_key=True, max_length=2)  # Field name made lowercase.
    clave_identificacion = models.CharField(db_column='Clave_Identificacion', max_length=6)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=65, blank=True, null=True)  # Field name made lowercase.
    nacionalidad = models.CharField(db_column='Nacionalidad', max_length=35, blank=True, null=True)  # Field name made lowercase.
    iata = models.CharField(db_column='IATA', max_length=4, blank=True, null=True)  # Field name made lowercase.
    linea_ferrea = models.CharField(db_column='Linea_Ferrea', max_length=9, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'CFDI_Estaciones'
        unique_together = (('clave_transporte', 'clave_identificacion'),)


class CfdiEstados(models.Model):
    estado = models.CharField(db_column='ESTADO', primary_key=True, max_length=4)  # Field name made lowercase.
    nombre_estado = models.CharField(db_column='NOMBRE_ESTADO', max_length=64, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'CFDI_Estados'


class CfdiExportacion(models.Model):
    id_clave = models.CharField(db_column='ID_CLAVE', primary_key=True, max_length=2)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=19, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'CFDI_Exportacion'


class CfdiFraccion(models.Model):
    fraccionarencelaria = models.CharField(db_column='FRACCIONARENCELARIA', primary_key=True, max_length=10)  # Field name made lowercase.
    descripcion = models.TextField(db_column='DESCRIPCION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    um = models.CharField(db_column='UM', max_length=4, blank=True, null=True)  # Field name made lowercase.
    imp = models.CharField(db_column='IMP', max_length=19, blank=True, null=True)  # Field name made lowercase.
    exp = models.CharField(db_column='EXP', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'CFDI_Fraccion'


class CfdiLocalidades(models.Model):
    localidades = models.CharField(db_column='LOCALIDADES', primary_key=True, max_length=3)  # Field name made lowercase.
    estado = models.CharField(db_column='ESTADO', max_length=4)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'CFDI_Localidades'
        unique_together = (('localidades', 'estado'),)


class CfdiMotivoTraslado(models.Model):
    motivo_traslado = models.CharField(db_column='MOTIVO_TRASLADO', primary_key=True, max_length=3)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=64, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'CFDI_MOTIVO_TRASLADO'


class CfdiMaterialPeligroso(models.Model):
    clave_material_peligroso = models.CharField(db_column='Clave_Material_Peligroso', primary_key=True, max_length=10)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    clase_div = models.CharField(db_column='Clase_div', max_length=55, blank=True, null=True)  # Field name made lowercase.
    peligro_secundario = models.CharField(db_column='Peligro_Secundario', max_length=55, blank=True, null=True)  # Field name made lowercase.
    emb_env_onu = models.CharField(db_column='EMB_ENV_ONU', max_length=55, blank=True, null=True)  # Field name made lowercase.
    disp_espec = models.CharField(db_column='Disp_Espec', max_length=55, blank=True, null=True)  # Field name made lowercase.
    cant_limitadas = models.CharField(db_column='Cant_Limitadas', max_length=55, blank=True, null=True)  # Field name made lowercase.
    exceptuadas = models.CharField(db_column='Exceptuadas', max_length=55, blank=True, null=True)  # Field name made lowercase.
    inst_emb_env = models.CharField(db_column='Inst_EMB_ENV', max_length=55, blank=True, null=True)  # Field name made lowercase.
    disp_espec_emba_env = models.CharField(db_column='Disp_Espec_Emba_ENV', max_length=55, blank=True, null=True)  # Field name made lowercase.
    cisternasport_inst_transp = models.CharField(db_column='CisternasPort_Inst_transp', max_length=55, blank=True, null=True)  # Field name made lowercase.
    rig_disp_espec = models.CharField(db_column='RIG_Disp_Espec', max_length=55, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'CFDI_MaterialPeligroso'


class CfdiMeses(models.Model):
    id_clave = models.CharField(db_column='ID_CLAVE', primary_key=True, max_length=2)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=49, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'CFDI_Meses'


class CfdiMotivoCancelacion(models.Model):
    id_cancelacion = models.CharField(db_column='ID_CANCELACION', primary_key=True, max_length=2)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=249, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'CFDI_Motivo_Cancelacion'


class CfdiMunicipios(models.Model):
    municipio = models.CharField(db_column='MUNICIPIO', primary_key=True, max_length=4)  # Field name made lowercase.
    estado = models.CharField(db_column='ESTADO', max_length=4)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=149, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'CFDI_Municipios'
        unique_together = (('municipio', 'estado'),)


class CfdiNumautorizacionnaviero(models.Model):
    numero_autorizacion = models.CharField(db_column='Numero_Autorizacion', primary_key=True, max_length=20)  # Field name made lowercase.
    inicio_vigencia = models.IntegerField(db_column='Inicio_Vigencia', blank=True, null=True)  # Field name made lowercase.
    inicio_vigencia_field = models.CharField(db_column='Inicio_Vigencia_', max_length=9, blank=True, null=True)  # Field name made lowercase. Field renamed because it ended with '_'.
    fin_vigencia = models.IntegerField(db_column='Fin_Vigencia', blank=True, null=True)  # Field name made lowercase.
    fin_vigencia_field = models.CharField(db_column='Fin_Vigencia_', max_length=9, blank=True, null=True)  # Field name made lowercase. Field renamed because it ended with '_'.

    class Meta:
        db_table = 'CFDI_NumAutorizacionNaviero'


class CfdiObjetoimp(models.Model):
    id_clave = models.CharField(db_column='ID_CLAVE', primary_key=True, max_length=2)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=49, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'CFDI_ObjetoImp'




# class Cfdi33PartestransporteC(models.Model):
#     clave = models.CharField(db_column='CLAVE', primary_key=True, max_length=4)  # Field name made lowercase.
#     descripcion = models.CharField(db_column='DESCRIPCION', max_length=54, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFDI33_PartesTransporte_c'


class CfdiPeriodicidad(models.Model):
    id_clave = models.CharField(db_column='ID_CLAVE', primary_key=True, max_length=2)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=14, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'CFDI_Periodicidad'


class CfdiRemolques(models.Model):
    sysid_remolque = models.IntegerField(db_column='SYSID_REMOLQUE', primary_key=True)  # Field name made lowercase.
    rem1_subtipo = models.CharField(db_column='REM1_SUBTIPO', max_length=7, blank=True, null=True)  # Field name made lowercase.
    rem1_placa = models.CharField(db_column='REM1_PLACA', max_length=7, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'CFDI_Remolques'


class CfdiSubtiporem(models.Model):
    clave_remolque = models.CharField(db_column='Clave_Remolque', primary_key=True, max_length=7)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'CFDI_SubTipoRem'


# class Cfdi33TferrCarro(models.Model):
#     id_fac_cartaporte = models.IntegerField(db_column='ID_FAC_CARTAPORTE', blank=True, null=True)  # Field name made lowercase.
#     lineacarro = models.IntegerField(db_column='LINEACARRO', blank=True, null=True)  # Field name made lowercase.
#     tipocarro = models.CharField(db_column='TIPOCARRO', max_length=5, blank=True, null=True)  # Field name made lowercase.
#     matriculacarro = models.CharField(db_column='MATRICULACARRO', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     guiacarro = models.CharField(db_column='GUIACARRO', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     toneladasnetascarro = models.DecimalField(db_column='TONELADASNETASCARRO', max_digits=11, decimal_places=3, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFDI33_TFerr_Carro'


# class Cfdi33TferrDerechosdepeso(models.Model):
#     id_fac_cons_cp = models.IntegerField(db_column='ID_FAC_CONS_CP', primary_key=True)  # Field name made lowercase.
#     linea_derechospeso = models.IntegerField(db_column='LINEA_DERECHOSPESO', blank=True, null=True)  # Field name made lowercase.
#     tipoderechodepaso = models.CharField(db_column='TIPODERECHODEPASO', max_length=7, blank=True, null=True)  # Field name made lowercase.
#     kilometrajepagado = models.DecimalField(db_column='KILOMETRAJEPAGADO', max_digits=11, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFDI33_TFerr_DerechosDePeso'


class CfdiTipoCarro(models.Model):
    clave_tipocarro = models.CharField(db_column='Clave_TipoCarro', primary_key=True, max_length=5)  # Field name made lowercase.
    tipo_carro = models.CharField(db_column='Tipo_Carro', max_length=25, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=155, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'CFDI_TipoCarro'


class CfdiTipodeservicio(models.Model):
    clave_tiposervicio = models.CharField(db_column='Clave_TipoServicio', primary_key=True, max_length=4)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=55)  # Field name made lowercase.

    class Meta:
        db_table = 'CFDI_TipoDeServicio'


class CfdiTipoembalaje(models.Model):
    clave_designacion = models.CharField(db_column='Clave_Designacion', primary_key=True, max_length=5)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'CFDI_TipoEmbalaje'


class CfdiTipoEstacion(models.Model):
    clave_estacion = models.CharField(db_column='Clave_Estacion', primary_key=True, max_length=2)  # Field name made lowercase.
    descripcion_tipo_estacion = models.CharField(db_column='Descripcion_Tipo_Estacion', max_length=25, blank=True, null=True)  # Field name made lowercase.
    clave_transporte = models.CharField(db_column='Clave_Transporte', max_length=19, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'CFDI_TipoEstacion'


class CfdiTipopermiso(models.Model):
    clave = models.CharField(db_column='Clave', primary_key=True, max_length=6)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    clave_transporte = models.CharField(db_column='Clave_Transporte', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'CFDI_TipoPermiso'


# class CfdiTranMarContenedores(models.Model):
#     id_cartaporte = models.IntegerField(db_column='ID_CARTAPORTE', primary_key=True)  # Field name made lowercase.
#     linea_contenedor = models.IntegerField(db_column='LINEA_CONTENEDOR')  # Field name made lowercase.
#     matriculacontenedor = models.CharField(db_column='MATRICULACONTENEDOR', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     tipocontenedor = models.CharField(db_column='TIPOCONTENEDOR', max_length=6, blank=True, null=True)  # Field name made lowercase.
#     numprecinto = models.CharField(db_column='NUMPRECINTO', max_length=20, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
        
#         db_table = 'CFDI_TranMar_Contenedores'
#         unique_together = (('id_cartaporte', 'linea_contenedor'),)


class CfdiUnidadMedidaAduana(models.Model):
    unidad_medida_aduana = models.IntegerField(db_column='UNIDAD_MEDIDA_ADUANA', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=54, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'CFDI_Unidad_Medida_Aduana'
