# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


# class Anticipodetalles(models.Model):
#     anticiposysid = models.IntegerField(db_column='ANTICIPOSYSID', blank=True, null=True, primary_key=True)  # Field name made lowercase.
#     claveprodserv = models.CharField(db_column='CLAVEPRODSERV', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     cantidad = models.DecimalField(db_column='CANTIDAD', max_digits=13, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     claveunidad = models.CharField(db_column='CLAVEUNIDAD', max_length=5, blank=True, null=True)  # Field name made lowercase.
#     descripcion = models.CharField(db_column='DESCRIPCION', max_length=254, blank=True, null=True)  # Field name made lowercase.
#     valorunitario = models.DecimalField(db_column='VALORUNITARIO', max_digits=13, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     importe = models.DecimalField(db_column='IMPORTE', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     partidaiva = models.DecimalField(db_column='PARTIDAIVA', max_digits=17, decimal_places=5, blank=True, null=True)  # Field name made lowercase.
#     partidaivaporcentaje = models.DecimalField(db_column='PARTIDAIVAPORCENTAJE', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     partidaivaretenido = models.DecimalField(db_column='PARTIDAIVARETENIDO', max_digits=17, decimal_places=5, blank=True, null=True)  # Field name made lowercase.
#     partidaivaretenidoporcentaje = models.DecimalField(db_column='PARTIDAIVARETENIDOPORCENTAJE', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     partidaisr = models.DecimalField(db_column='PARTIDAISR', max_digits=17, decimal_places=5, blank=True, null=True)  # Field name made lowercase.
#     partidaisrporcentaje = models.DecimalField(db_column='PARTIDAISRPORCENTAJE', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'AnticipoDetalles'

# class Anticipos(models.Model):
#     sysid = models.IntegerField(db_column='SYSID', primary_key=True)  # Field name made lowercase.
#     numero = models.IntegerField(db_column='NUMERO', blank=True, null=True)  # Field name made lowercase.
#     procesado = models.SmallIntegerField(db_column='PROCESADO', blank=True, null=True)  # Field name made lowercase.
#     fecha = models.IntegerField(db_column='FECHA', blank=True, null=True)  # Field name made lowercase.
#     cliente = models.CharField(db_column='CLIENTE', max_length=19, blank=True, null=True)  # Field name made lowercase.
#     importe_pesos = models.DecimalField(db_column='IMPORTE_PESOS', max_digits=17, decimal_places=5, blank=True, null=True)  # Field name made lowercase.
#     importe_dolares = models.DecimalField(db_column='IMPORTE_DOLARES', max_digits=17, decimal_places=5, blank=True, null=True)  # Field name made lowercase.
#     estatus = models.CharField(db_column='ESTATUS', max_length=24, blank=True, null=True)  # Field name made lowercase.
#     valor_aplicado_timbrado_pesos = models.DecimalField(db_column='VALOR_APLICADO_TIMBRADO_PESOS', max_digits=17, decimal_places=5, blank=True, null=True)  # Field name made lowercase.
#     valor_aplicado_timbrado_dolares = models.DecimalField(db_column='VALOR_APLICADO_TIMBRADO_DOLARES', max_digits=17, decimal_places=5, blank=True, null=True)  # Field name made lowercase.
#     depositotimbrado_pesos = models.DecimalField(db_column='DEPOSITOTIMBRADO_PESOS', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     depositotimbrado_dolares = models.DecimalField(db_column='DEPOSITOTIMBRADO_DOLARES', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     valor_aplicado_no_timbrado_pesos = models.DecimalField(db_column='VALOR_APLICADO_NO_TIMBRADO_PESOS', max_digits=17, decimal_places=5, blank=True, null=True)  # Field name made lowercase.
#     valor_aplicado_no_timbrado_dolares = models.DecimalField(db_column='VALOR_APLICADO_NO_TIMBRADO_DOLARES', max_digits=17, decimal_places=5, blank=True, null=True)  # Field name made lowercase.
#     depositonotimbrado_pesos = models.DecimalField(db_column='DEPOSITONOTIMBRADO_PESOS', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     depositonotimbrado_dolares = models.DecimalField(db_column='DEPOSITONOTIMBRADO_DOLARES', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     saldo_pesos = models.DecimalField(db_column='SALDO_PESOS', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     saldo_dolares = models.DecimalField(db_column='SALDO_DOLARES', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     receptor_nombre = models.CharField(db_column='RECEPTOR_NOMBRE', max_length=120, blank=True, null=True)  # Field name made lowercase.
#     receptor_rfc = models.CharField(db_column='RECEPTOR_RFC', max_length=13, blank=True, null=True)  # Field name made lowercase.
#     receptor_residenciafiscal = models.CharField(db_column='RECEPTOR_RESIDENCIAFISCAL', max_length=4, blank=True, null=True)  # Field name made lowercase.
#     receptor_numregidtrib = models.CharField(db_column='RECEPTOR_NUMREGIDTRIB', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     receptor_usocfdi = models.CharField(db_column='RECEPTOR_USOCFDI', max_length=5, blank=True, null=True)  # Field name made lowercase.
#     emisor_regimenfiscal = models.CharField(db_column='EMISOR_REGIMENFISCAL', max_length=5, blank=True, null=True)  # Field name made lowercase.
#     emisor_nombre = models.CharField(db_column='EMISOR_NOMBRE', max_length=120, blank=True, null=True)  # Field name made lowercase.
#     emisor_rfc = models.CharField(db_column='EMISOR_RFC', max_length=13, blank=True, null=True)  # Field name made lowercase.
#     comprobante_lugarexpedicion = models.CharField(db_column='COMPROBANTE_LUGAREXPEDICION', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     comprobante_tipodecomprobante = models.CharField(db_column='COMPROBANTE_TIPODECOMPROBANTE', max_length=3, blank=True, null=True)  # Field name made lowercase.
#     comprobante_formapago = models.CharField(db_column='COMPROBANTE_FORMAPAGO', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     comprobante_metodopago = models.CharField(db_column='COMPROBANTE_METODOPAGO', max_length=5, blank=True, null=True)  # Field name made lowercase.
#     comprobante_serie = models.CharField(db_column='COMPROBANTE_SERIE', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     comprobante_folio = models.IntegerField(db_column='COMPROBANTE_FOLIO', blank=True, null=True)  # Field name made lowercase.
#     comprobante_total = models.DecimalField(db_column='COMPROBANTE_TOTAL', max_digits=17, decimal_places=5, blank=True, null=True)  # Field name made lowercase.
#     comprobante_total_dolares = models.DecimalField(db_column='COMPROBANTE_TOTAL_DOLARES', max_digits=17, decimal_places=5, blank=True, null=True)  # Field name made lowercase.
#     comprobante_tipocambio = models.DecimalField(db_column='COMPROBANTE_TIPOCAMBIO', max_digits=9, decimal_places=5, blank=True, null=True)  # Field name made lowercase.
#     comprobante_subtotal = models.DecimalField(db_column='COMPROBANTE_SUBTOTAL', max_digits=17, decimal_places=5, blank=True, null=True)  # Field name made lowercase.
#     comprobante_subtotal_dolares = models.DecimalField(db_column='COMPROBANTE_SUBTOTAL_DOLARES', max_digits=17, decimal_places=5, blank=True, null=True)  # Field name made lowercase.
#     comprobante_moneda = models.CharField(db_column='COMPROBANTE_MONEDA', max_length=9, blank=True, null=True)  # Field name made lowercase.
#     comprobante_fecha = models.CharField(db_column='COMPROBANTE_FECHA', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     comprobante_estatus = models.CharField(db_column='COMPROBANTE_ESTATUS', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     comprobante_importeiva = models.DecimalField(db_column='COMPROBANTE_IMPORTEIVA', max_digits=15, decimal_places=5, blank=True, null=True)  # Field name made lowercase.
#     comprobante_importeiva_dolares = models.DecimalField(db_column='COMPROBANTE_IMPORTEIVA_DOLARES', max_digits=15, decimal_places=5, blank=True, null=True)  # Field name made lowercase.
#     comprobante_importeivaporcentaje = models.DecimalField(db_column='COMPROBANTE_IMPORTEIVAPORCENTAJE', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     comprobante_importeivaretenido = models.DecimalField(db_column='COMPROBANTE_IMPORTEIVARETENIDO', max_digits=17, decimal_places=5, blank=True, null=True)  # Field name made lowercase.
#     comprobante_importeivaretenido_dolares = models.DecimalField(db_column='COMPROBANTE_IMPORTEIVARETENIDO_DOLARES', max_digits=15, decimal_places=5, blank=True, null=True)  # Field name made lowercase.
#     comprobante_importeivaretenidoporcentaje = models.DecimalField(db_column='COMPROBANTE_IMPORTEIVARETENIDOPORCENTAJE', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     comprobante_importeisr = models.DecimalField(db_column='COMPROBANTE_IMPORTEISR', max_digits=15, decimal_places=5, blank=True, null=True)  # Field name made lowercase.
#     comprobante_importeisr_dolares = models.DecimalField(db_column='COMPROBANTE_IMPORTEISR_DOLARES', max_digits=15, decimal_places=5, blank=True, null=True)  # Field name made lowercase.
#     comprobante_importeisrporcentaje = models.DecimalField(db_column='COMPROBANTE_IMPORTEISRPORCENTAJE', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     cadenaoriginal = models.TextField(db_column='CADENAORIGINAL', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sellodigital = models.CharField(db_column='SELLODIGITAL', max_length=999, blank=True, null=True)  # Field name made lowercase.
#     nocertificado = models.CharField(db_column='NOCERTIFICADO', max_length=59, blank=True, null=True)  # Field name made lowercase.
#     foliopac = models.CharField(db_column='FOLIOPAC', max_length=99, blank=True, null=True)  # Field name made lowercase.
#     fechacertificacion = models.CharField(db_column='FECHACERTIFICACION', max_length=24, blank=True, null=True)  # Field name made lowercase.
#     cfdi33_rfcprovcertificacion = models.CharField(db_column='CFDI33_RFCPROVCERTIFICACION', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     cfdi33_versiontimbrado = models.CharField(db_column='CFDI33_VERSIONTIMBRADO', max_length=9, blank=True, null=True)  # Field name made lowercase.
#     cadenaoriginalsat = models.TextField(db_column='CADENAORIGINALSAT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sellodigitalsat = models.CharField(db_column='SELLODIGITALSAT', max_length=999, blank=True, null=True)  # Field name made lowercase.
#     nocertificadosat = models.CharField(db_column='NOCERTIFICADOSAT', max_length=79, blank=True, null=True)  # Field name made lowercase.
#     cancelstatus_cfdi33 = models.CharField(db_column='CANCELSTATUS_CFDI33', max_length=99, blank=True, null=True)  # Field name made lowercase.
#     iscancelable_cfdi33 = models.CharField(db_column='ISCANCELABLE_CFDI33', max_length=99, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'Anticipos'
#         unique_together = (('cliente', 'numero'),)


# class AnticiposEgresosDetalles(models.Model):
#     anticiposysid = models.IntegerField(db_column='ANTICIPOSYSID', primary_key=True)  # Field name made lowercase.
#     linea = models.IntegerField(db_column='LINEA')  # Field name made lowercase.
#     nocertificadodigital = models.CharField(db_column='NOCERTIFICADODIGITAL', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     versiontimbrado = models.CharField(db_column='VERSIONTIMBRADO', max_length=19, blank=True, null=True)  # Field name made lowercase.
#     uuidtimbrado = models.CharField(db_column='UUIDTIMBRADO', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     rfcprovcertificacion = models.CharField(db_column='RFCPROVCERTIFICACION', max_length=13, blank=True, null=True)  # Field name made lowercase.
#     cadenaoriginalsattimbrado = models.CharField(db_column='CADENAORIGINALSATTIMBRADO', max_length=4999, blank=True, null=True)  # Field name made lowercase.
#     sellocfdtimbrado = models.CharField(db_column='SELLOCFDTIMBRADO', max_length=4999, blank=True, null=True)  # Field name made lowercase.
#     nocertificadosattimbrado = models.CharField(db_column='NOCERTIFICADOSATTIMBRADO', max_length=4999, blank=True, null=True)  # Field name made lowercase.
#     formapago = models.CharField(db_column='FORMAPAGO', max_length=4, blank=True, null=True)  # Field name made lowercase.
#     tipocomprobante = models.CharField(db_column='TIPOCOMPROBANTE', max_length=4, blank=True, null=True)  # Field name made lowercase.
#     sellodigitalemisor = models.CharField(db_column='SELLODIGITALEMISOR', max_length=4999, blank=True, null=True)  # Field name made lowercase.
#     fechayhoratimbrado = models.CharField(db_column='FECHAYHORATIMBRADO', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     importe = models.DecimalField(db_column='IMPORTE', max_digits=17, decimal_places=5, blank=True, null=True)  # Field name made lowercase.
#     saldo = models.DecimalField(db_column='SALDO', max_digits=17, decimal_places=5, blank=True, null=True)  # Field name made lowercase.
#     estatus = models.CharField(db_column='ESTATUS', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     consecutivo = models.IntegerField(db_column='CONSECUTIVO', blank=True, null=True)  # Field name made lowercase.
#     iva = models.DecimalField(db_column='IVA', max_digits=17, decimal_places=5, blank=True, null=True)  # Field name made lowercase.
#     ivaretenido = models.DecimalField(db_column='IVARETENIDO', max_digits=17, decimal_places=5, blank=True, null=True)  # Field name made lowercase.
#     isr = models.DecimalField(db_column='ISR', max_digits=17, decimal_places=5, blank=True, null=True)  # Field name made lowercase.
#     ivaporcentaje = models.DecimalField(db_column='IVAPORCENTAJE', max_digits=17, decimal_places=5, blank=True, null=True)  # Field name made lowercase.
#     ivaretenidoporcentaje = models.DecimalField(db_column='IVARETENIDOPORCENTAJE', max_digits=17, decimal_places=5, blank=True, null=True)  # Field name made lowercase.
#     isrporcentaje = models.DecimalField(db_column='ISRPORCENTAJE', max_digits=17, decimal_places=5, blank=True, null=True)  # Field name made lowercase.
#     tipofactor = models.CharField(db_column='TIPOFACTOR', max_length=19, blank=True, null=True)  # Field name made lowercase.
#     impuesto = models.CharField(db_column='IMPUESTO', max_length=19, blank=True, null=True)  # Field name made lowercase.
#     unidadmedidaclave = models.CharField(db_column='UNIDADMEDIDACLAVE', max_length=4, blank=True, null=True)  # Field name made lowercase.
#     productoclave = models.CharField(db_column='PRODUCTOCLAVE', max_length=9, blank=True, null=True)  # Field name made lowercase.
#     cantidad = models.DecimalField(db_column='CANTIDAD', max_digits=7, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     descripcion = models.CharField(db_column='DESCRIPCION', max_length=199, blank=True, null=True)  # Field name made lowercase.
#     valorunitario = models.DecimalField(db_column='VALORUNITARIO', max_digits=17, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     cadenaoriginalemisor = models.CharField(db_column='CADENAORIGINALEMISOR', max_length=4999, blank=True, null=True)  # Field name made lowercase.
#     subtotal = models.DecimalField(db_column='SUBTOTAL', max_digits=17, decimal_places=5, blank=True, null=True)  # Field name made lowercase.
#     total = models.DecimalField(db_column='TOTAL', max_digits=17, decimal_places=5, blank=True, null=True)  # Field name made lowercase.
#     sellosat = models.CharField(db_column='SELLOSAT', max_length=4999, blank=True, null=True)  # Field name made lowercase.
#     fechayhoraemision = models.CharField(db_column='FECHAYHORAEMISION', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     fechaclarion = models.IntegerField(db_column='FECHACLARION', blank=True, null=True)  # Field name made lowercase.
#     cancelstatus_cfdi33 = models.CharField(db_column='CANCELSTATUS_CFDI33', max_length=99, blank=True, null=True)  # Field name made lowercase.
#     iscancelable_cfdi33 = models.CharField(db_column='ISCANCELABLE_CFDI33', max_length=99, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'Anticipos_Egresos_Detalles'
#         unique_together = (('anticiposysid', 'linea'),)

# class Cfd33Aduana(models.Model):
#     aduanaclave = models.CharField(db_column='ADUANACLAVE', primary_key=True, max_length=4)  # Field name made lowercase.
#     descripcion = models.CharField(db_column='DESCRIPCION', max_length=254, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFD33Aduana'


# class Cfd33Claveunidadmedida(models.Model):
#     unidadmedidaclave = models.CharField(db_column='UNIDADMEDIDACLAVE', primary_key=True, max_length=5)  # Field name made lowercase.
#     nombre = models.CharField(db_column='NOMBRE', max_length=120, blank=True, null=True)  # Field name made lowercase.
#     descripcion = models.CharField(db_column='DESCRIPCION', max_length=1000, blank=True, null=True)  # Field name made lowercase.
#     nota = models.CharField(db_column='NOTA', max_length=2000, blank=True, null=True)  # Field name made lowercase.
#     simbolo = models.CharField(db_column='SIMBOLO', max_length=20, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFD33ClaveUnidadMedida'


# class Cfd33Documentosrelacionados(models.Model):
#     sysid_dr = models.IntegerField(db_column='SYSID_DR', primary_key=True)  # Field name made lowercase.
#     uuid = models.CharField(db_column='UUID', max_length=99, blank=True, null=True)  # Field name made lowercase.
#     tipocfdi = models.CharField(db_column='TIPOCFDI', max_length=34)  # Field name made lowercase.
#     consecutivo_tipocfd = models.IntegerField(db_column='CONSECUTIVO_TIPOCFD')  # Field name made lowercase.
#     tiporelacion = models.CharField(db_column='TIPORELACION', max_length=2, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFD33DocumentosRelacionados'
#         unique_together = (('sysid_dr', 'tipocfdi', 'consecutivo_tipocfd'),)


# class Cfd33Documentosrelacionadosfi(models.Model):
#     sysid_dr = models.IntegerField(db_column='SYSID_DR', primary_key=True)  # Field name made lowercase.
#     uuid = models.CharField(db_column='UUID', max_length=99, blank=True, null=True)  # Field name made lowercase.
#     consecutivo_tipocfd = models.IntegerField(db_column='CONSECUTIVO_TIPOCFD')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFD33DocumentosRelacionadosFI'
#         unique_together = (('sysid_dr', 'consecutivo_tipocfd'),)


class Cfd33Formapago(models.Model):
    formapagoclave = models.CharField(db_column='FORMAPAGOCLAVE', primary_key=True, max_length=10)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=80, blank=True, null=True)  # Field name made lowercase.



# class Cfd33Impuestos(models.Model):
#     impuestoclave = models.CharField(db_column='IMPUESTOCLAVE', primary_key=True, max_length=4)  # Field name made lowercase.
#     descripcion = models.CharField(db_column='DESCRIPCION', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     retencion = models.CharField(db_column='RETENCION', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     traslado = models.CharField(db_column='TRASLADO', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     local = models.CharField(db_column='LOCAL', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     entidadaplica = models.CharField(db_column='ENTIDADAPLICA', max_length=20, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFD33Impuestos'

# class Cfd33Metodopago(models.Model):
#     metodopagoclave = models.CharField(db_column='METODOPAGOCLAVE', primary_key=True, max_length=5)  # Field name made lowercase.
#     descripcion = models.CharField(db_column='DESCRIPCION', max_length=120, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFD33MetodoPago'


# class Cfd33Monedas(models.Model):
#     monedaclave = models.CharField(db_column='MONEDACLAVE', primary_key=True, max_length=5)  # Field name made lowercase.
#     descripcion = models.CharField(db_column='DESCRIPCION', max_length=120, blank=True, null=True)  # Field name made lowercase.
#     decimales = models.IntegerField(db_column='DECIMALES', blank=True, null=True)  # Field name made lowercase.
#     porcentajevariacion = models.CharField(db_column='PORCENTAJEVARIACION', max_length=10, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFD33Monedas'


# class Cfd33Pais(models.Model):
#     paisclave = models.CharField(db_column='PAISCLAVE', primary_key=True, max_length=3)  # Field name made lowercase.
#     descripcion = models.CharField(db_column='DESCRIPCION', max_length=120, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFD33Pais'


# class Cfd33Patente(models.Model):
#     patenteclave = models.CharField(db_column='PATENTECLAVE', primary_key=True, max_length=4)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFD33Patente'


# class Cfd33Productosservicios(models.Model):
#     productoclave = models.CharField(db_column='PRODUCTOCLAVE', primary_key=True, max_length=10)  # Field name made lowercase.
#     descripcion = models.CharField(db_column='DESCRIPCION', max_length=254, blank=True, null=True)  # Field name made lowercase.
#     incluirivatraslado = models.CharField(db_column='INCLUIRIVATRASLADO', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     incluiriepstraslado = models.CharField(db_column='INCLUIRIEPSTRASLADO', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     complementoincluir = models.CharField(db_column='COMPLEMENTOINCLUIR', max_length=20, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFD33ProductosServicios'


# class Cfd33Regimenfiscal(models.Model):
#     regimenfiscalclave = models.CharField(db_column='REGIMENFISCALCLAVE', primary_key=True, max_length=3)  # Field name made lowercase.
#     descripcion = models.CharField(db_column='DESCRIPCION', max_length=254, blank=True, null=True)  # Field name made lowercase.
#     fisica = models.CharField(db_column='FISICA', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     moral = models.CharField(db_column='MORAL', max_length=2, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFD33RegimenFiscal'


# class Cfd33Tasacuota(models.Model):
#     impuesto = models.CharField(db_column='IMPUESTO', primary_key=True, max_length=5)  # Field name made lowercase.
#     valormaximo = models.DecimalField(db_column='VALORMAXIMO', max_digits=17, decimal_places=7)  # Field name made lowercase.
#     rango = models.CharField(db_column='RANGO', max_length=10)  # Field name made lowercase.
#     valorminimo = models.DecimalField(db_column='VALORMINIMO', max_digits=17, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     factor = models.CharField(db_column='FACTOR', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     traslado = models.CharField(db_column='TRASLADO', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     retencion = models.CharField(db_column='RETENCION', max_length=2, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFD33TasaCuota'
#         unique_together = (('impuesto', 'valormaximo', 'rango'),)

# class Cfd33Tipodecomprobante(models.Model):
#     tipocomprobanteclave = models.CharField(db_column='TIPOCOMPROBANTECLAVE', primary_key=True, max_length=3)  # Field name made lowercase.
#     descripcion = models.CharField(db_column='DESCRIPCION', max_length=80, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFD33TipoDeComprobante'

# class Cfd33Tipofactor(models.Model):
#     tipofactorclave = models.CharField(db_column='TIPOFACTORCLAVE', primary_key=True, max_length=20)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFD33TipoFactor'

# class Cfd33Tiporelacion(models.Model):
#     tiporelacionclave = models.CharField(db_column='TIPORELACIONCLAVE', primary_key=True, max_length=5)  # Field name made lowercase.
#     descripcion = models.CharField(db_column='DESCRIPCION', max_length=120, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFD33TipoRelacion'


# class Cfd33Uso(models.Model):
#     usoclave = models.CharField(db_column='USOCLAVE', primary_key=True, max_length=5)  # Field name made lowercase.
#     descripcion = models.CharField(db_column='DESCRIPCION', max_length=120, blank=True, null=True)  # Field name made lowercase.
#     fisica = models.CharField(db_column='FISICA', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     moral = models.CharField(db_column='MORAL', max_length=2, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFD33Uso'


# class Cfdi33Codigopostal(models.Model):
#     codigopostal = models.CharField(db_column='CODIGOPOSTAL', primary_key=True, max_length=10)  # Field name made lowercase.
#     estado = models.CharField(db_column='ESTADO', max_length=3, blank=True, null=True)  # Field name made lowercase.
#     municipio = models.CharField(db_column='MUNICIPIO', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     localidad = models.CharField(db_column='LOCALIDAD', max_length=5, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFDI33CodigoPostal'


# class Cfdi33Cartaporte(models.Model):
#     id_factura_consecutivo = models.IntegerField(db_column='ID_FACTURA_CONSECUTIVO', primary_key=True)  # Field name made lowercase.
#     cartaporte_transpinternac = models.CharField(db_column='CARTAPORTE_TRANSPINTERNAC', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     cartaporte_entradasalidamerc = models.CharField(db_column='CARTAPORTE_ENTRADASALIDAMERC', max_length=7, blank=True, null=True)  # Field name made lowercase.
#     cartaporte_viaentradasalida = models.CharField(db_column='CARTAPORTE_VIAENTRADASALIDA', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     cartaporte_totaldistrec = models.DecimalField(db_column='CARTAPORTE_TOTALDISTREC', max_digits=7, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     cp_mcias_pesobrutototal = models.DecimalField(db_column='CP_MCIAS_PESOBRUTOTOTAL', max_digits=13, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
#     cp_mcias_unidadpeso = models.CharField(db_column='CP_MCIAS_UNIDADPESO', max_length=4, blank=True, null=True)  # Field name made lowercase.
#     cp_mcias_pesonetototal = models.DecimalField(db_column='CP_MCIAS_PESONETOTOTAL', max_digits=7, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
#     cp_mcias_numtotalmercancias = models.IntegerField(db_column='CP_MCIAS_NUMTOTALMERCANCIAS', blank=True, null=True)  # Field name made lowercase.
#     cp_mcias_cargoportasacion = models.DecimalField(db_column='CP_MCIAS_CARGOPORTASACION', max_digits=13, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
#     cp_mcias_autofed = models.SmallIntegerField(db_column='CP_MCIAS_AUTOFED', blank=True, null=True)  # Field name made lowercase.
#     cp_mcias_autofed_permsct = models.CharField(db_column='CP_MCIAS_AUTOFED_PERMSCT', max_length=6, blank=True, null=True)  # Field name made lowercase.
#     cp_mcias_autofed_numpermisosct = models.CharField(db_column='CP_MCIAS_AUTOFED_NUMPERMISOSCT', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     cp_mcias_autofed_nombreaseg = models.CharField(db_column='CP_MCIAS_AUTOFED_NOMBREASEG', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     cp_mcias_autofed_numpolizaseguro = models.CharField(db_column='CP_MCIAS_AUTOFED_NUMPOLIZASEGURO', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     cp_mcias_autofed_idv_configvehicular = models.CharField(db_column='CP_MCIAS_AUTOFED_IDV_CONFIGVEHICULAR', max_length=7, blank=True, null=True)  # Field name made lowercase.
#     cp_mcias_autofed_idv_placavm = models.CharField(db_column='CP_MCIAS_AUTOFED_IDV_PLACAVM', max_length=7, blank=True, null=True)  # Field name made lowercase.
#     cp_mcias_autofed_idv_aniomodelovm = models.CharField(db_column='CP_MCIAS_AUTOFED_IDV_ANIOMODELOVM', max_length=4, blank=True, null=True)  # Field name made lowercase.
#     cp_mcias_autofed_rem1_subtiporem = models.CharField(db_column='CP_MCIAS_AUTOFED_REM1_SUBTIPOREM', max_length=7, blank=True, null=True)  # Field name made lowercase.
#     cp_mcias_autofed_rem1_placa = models.CharField(db_column='CP_MCIAS_AUTOFED_REM1_PLACA', max_length=7, blank=True, null=True)  # Field name made lowercase.
#     cp_mcias_autofed_rem2_subtiporem = models.CharField(db_column='CP_MCIAS_AUTOFED_REM2_SUBTIPOREM', max_length=7, blank=True, null=True)  # Field name made lowercase.
#     cp_mcias_autofed_rem2_placa = models.CharField(db_column='CP_MCIAS_AUTOFED_REM2_PLACA', max_length=7, blank=True, null=True)  # Field name made lowercase.
#     cp_mcias_tranmar = models.SmallIntegerField(db_column='CP_MCIAS_TRANMAR', blank=True, null=True)  # Field name made lowercase.
#     cp_mcias_tranmar_permsct = models.CharField(db_column='CP_MCIAS_TRANMAR_PERMSCT', max_length=6, blank=True, null=True)  # Field name made lowercase.
#     cp_mcias_tranmar_numpermisosct = models.CharField(db_column='CP_MCIAS_TRANMAR_NUMPERMISOSCT', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     cp_mcias_tranmar_numpolizaseguro = models.CharField(db_column='CP_MCIAS_TRANMAR_NUMPOLIZASEGURO', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     cp_mcias_tranmar_tipoembarcacion = models.CharField(db_column='CP_MCIAS_TRANMAR_TIPOEMBARCACION', max_length=4, blank=True, null=True)  # Field name made lowercase.
#     cp_mcias_tranmar_matricula = models.CharField(db_column='CP_MCIAS_TRANMAR_MATRICULA', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     cp_mcias_tranmar_numeroomi = models.CharField(db_column='CP_MCIAS_TRANMAR_NUMEROOMI', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     cp_mcias_tranmar_anioembarcacion = models.CharField(db_column='CP_MCIAS_TRANMAR_ANIOEMBARCACION', max_length=4, blank=True, null=True)  # Field name made lowercase.
#     cp_mcias_tranmar_nombreembarc = models.CharField(db_column='CP_MCIAS_TRANMAR_NOMBREEMBARC', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     cp_mcias_tranmar_nacionalidadembarc = models.CharField(db_column='CP_MCIAS_TRANMAR_NACIONALIDADEMBARC', max_length=19, blank=True, null=True)  # Field name made lowercase.
#     cp_mcias_tranmar_unidadesdearqbruto = models.DecimalField(db_column='CP_MCIAS_TRANMAR_UNIDADESDEARQBRUTO', max_digits=7, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
#     cp_mcias_tranmar_tipocarga = models.CharField(db_column='CP_MCIAS_TRANMAR_TIPOCARGA', max_length=5, blank=True, null=True)  # Field name made lowercase.
#     cp_mcias_tranmar_numcertitc = models.CharField(db_column='CP_MCIAS_TRANMAR_NUMCERTITC', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     cp_mcias_tranmar_eslora = models.DecimalField(db_column='CP_MCIAS_TRANMAR_ESLORA', max_digits=7, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     cp_mcias_tranmar_manga = models.DecimalField(db_column='CP_MCIAS_TRANMAR_MANGA', max_digits=7, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     cp_mcias_tranmar_calado = models.DecimalField(db_column='CP_MCIAS_TRANMAR_CALADO', max_digits=7, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     cp_mcias_tranmar_lineanaviera = models.CharField(db_column='CP_MCIAS_TRANMAR_LINEANAVIERA', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     cp_mcias_tranmar_nombreagentenaviero = models.CharField(db_column='CP_MCIAS_TRANMAR_NOMBREAGENTENAVIERO', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     cp_mcias_tranmar_numautorizacionnaviero = models.CharField(db_column='CP_MCIAS_TRANMAR_NUMAUTORIZACIONNAVIERO', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     cp_mcias_tranmar_numviaje = models.CharField(db_column='CP_MCIAS_TRANMAR_NUMVIAJE', max_length=31, blank=True, null=True)  # Field name made lowercase.
#     cp_mcias_tranmar_numconocembarc = models.CharField(db_column='CP_MCIAS_TRANMAR_NUMCONOCEMBARC', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     cp_mcias_taereo = models.SmallIntegerField(db_column='CP_MCIAS_TAEREO', blank=True, null=True)  # Field name made lowercase.
#     cp_mcias_taereo_permsct = models.CharField(db_column='CP_MCIAS_TAEREO_PERMSCT', max_length=6, blank=True, null=True)  # Field name made lowercase.
#     cp_mcias_taereo_numpermisosct = models.CharField(db_column='CP_MCIAS_TAEREO_NUMPERMISOSCT', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     cp_mcias_taereo_matriculaaeronave = models.CharField(db_column='CP_MCIAS_TAEREO_MATRICULAAERONAVE', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     cp_mcias_taereo_nombreaseg = models.CharField(db_column='CP_MCIAS_TAEREO_NOMBREASEG', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     cp_mcias_taereo_numpolizaseguro = models.CharField(db_column='CP_MCIAS_TAEREO_NUMPOLIZASEGURO', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     cp_mcias_taereo_numeroguia = models.CharField(db_column='CP_MCIAS_TAEREO_NUMEROGUIA', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     cp_mcias_taereo_lugarcontrato = models.CharField(db_column='CP_MCIAS_TAEREO_LUGARCONTRATO', max_length=120, blank=True, null=True)  # Field name made lowercase.
#     cp_mcias_taereo_rfctransportista = models.CharField(db_column='CP_MCIAS_TAEREO_RFCTRANSPORTISTA', max_length=18, blank=True, null=True)  # Field name made lowercase.
#     cp_mcias_taereo_codigotransportista = models.CharField(db_column='CP_MCIAS_TAEREO_CODIGOTRANSPORTISTA', max_length=6, blank=True, null=True)  # Field name made lowercase.
#     cp_mcias_taereo_numregidtribtranspor = models.CharField(db_column='CP_MCIAS_TAEREO_NUMREGIDTRIBTRANSPOR', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     cp_mcias_taereo_residenciafiscaltranspor = models.CharField(db_column='CP_MCIAS_TAEREO_RESIDENCIAFISCALTRANSPOR', max_length=3, blank=True, null=True)  # Field name made lowercase.
#     cp_mcias_taereo_nombretransportista = models.CharField(db_column='CP_MCIAS_TAEREO_NOMBRETRANSPORTISTA', max_length=254, blank=True, null=True)  # Field name made lowercase.
#     cp_mcias_taereo_rfcembarcador = models.CharField(db_column='CP_MCIAS_TAEREO_RFCEMBARCADOR', max_length=18, blank=True, null=True)  # Field name made lowercase.
#     cp_mcias_taereo_numregidtribembarc = models.CharField(db_column='CP_MCIAS_TAEREO_NUMREGIDTRIBEMBARC', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     cp_mcias_taereo_residenciafiscalembarc = models.CharField(db_column='CP_MCIAS_TAEREO_RESIDENCIAFISCALEMBARC', max_length=3, blank=True, null=True)  # Field name made lowercase.
#     cp_mcias_taereo_nombreembarcador = models.CharField(db_column='CP_MCIAS_TAEREO_NOMBREEMBARCADOR', max_length=254, blank=True, null=True)  # Field name made lowercase.
#     cp_mcias_tferr = models.SmallIntegerField(db_column='CP_MCIAS_TFERR', blank=True, null=True)  # Field name made lowercase.
#     cp_mcias_tferr_tipodeservicio = models.CharField(db_column='CP_MCIAS_TFERR_TIPODESERVICIO', max_length=4, blank=True, null=True)  # Field name made lowercase.
#     cp_mcias_tferr_nombreaseg = models.CharField(db_column='CP_MCIAS_TFERR_NOMBREASEG', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     cp_mcias_tferr_numpolizaseguro = models.CharField(db_column='CP_MCIAS_TFERR_NUMPOLIZASEGURO', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     cp_mcias_tferr_concesionario = models.CharField(db_column='CP_MCIAS_TFERR_CONCESIONARIO', max_length=18, blank=True, null=True)  # Field name made lowercase.
#     figura_tran_clavetransporte = models.CharField(db_column='FIGURA_TRAN_CLAVETRANSPORTE', max_length=19, blank=True, null=True)  # Field name made lowercase.
#     cartaporte_paisorigendestino = models.CharField(db_column='CARTAPORTE_PAISORIGENDESTINO', max_length=3, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFDI33_CartaPorte'


# class Cfdi33CartaporteCantidadtransporta(models.Model):
#     id_cartaporte_mercancia = models.IntegerField(db_column='ID_CARTAPORTE_MERCANCIA', primary_key=True)  # Field name made lowercase.
#     lineamercancia = models.IntegerField(db_column='LINEAMERCANCIA')  # Field name made lowercase.
#     id_cantidadtransporta = models.IntegerField(db_column='ID_CANTIDADTRANSPORTA')  # Field name made lowercase.
#     mcia_cantidad = models.DecimalField(db_column='MCIA_CANTIDAD', max_digits=11, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     mcia_idorigen = models.CharField(db_column='MCIA_IDORIGEN', max_length=8, blank=True, null=True)  # Field name made lowercase.
#     mcia_iddestino = models.CharField(db_column='MCIA_IDDESTINO', max_length=8, blank=True, null=True)  # Field name made lowercase.
#     mcia_cvestransporte = models.CharField(db_column='MCIA_CVESTRANSPORTE', max_length=2, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFDI33_CartaPorte_CantidadTransporta'
#         unique_together = (('id_cartaporte_mercancia', 'lineamercancia', 'id_cantidadtransporta'),)

# class Cfdi33CartaporteGuiasidentificacion(models.Model):
#     id_cartaporte_mercancia = models.IntegerField(db_column='ID_CARTAPORTE_MERCANCIA', primary_key=True)  # Field name made lowercase.
#     lineamercancia = models.IntegerField(db_column='LINEAMERCANCIA')  # Field name made lowercase.
#     lineaguiaidentificacion = models.IntegerField(db_column='LINEAGUIAIDENTIFICACION')  # Field name made lowercase.
#     numeroguiaidentificacion = models.CharField(db_column='NUMEROGUIAIDENTIFICACION', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     descripguiaidentificacion = models.CharField(db_column='DESCRIPGUIAIDENTIFICACION', max_length=1000, blank=True, null=True)  # Field name made lowercase.
#     pesoguiaidentificacion = models.DecimalField(db_column='PESOGUIAIDENTIFICACION', max_digits=7, decimal_places=3, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFDI33_CartaPorte_GuiasIdentificacion'
#         unique_together = (('id_cartaporte_mercancia', 'lineamercancia', 'lineaguiaidentificacion'),)

# class Cfdi33CartaporteMercancias(models.Model):
#     id_cartaporte_mercancia = models.IntegerField(db_column='ID_CARTAPORTE_MERCANCIA', primary_key=True)  # Field name made lowercase.
#     lineamercancia = models.IntegerField(db_column='LINEAMERCANCIA')  # Field name made lowercase.
#     bienestransp = models.CharField(db_column='BIENESTRANSP', max_length=8, blank=True, null=True)  # Field name made lowercase.
#     clavestcc = models.CharField(db_column='CLAVESTCC', max_length=9, blank=True, null=True)  # Field name made lowercase.
#     descripcion = models.CharField(db_column='DESCRIPCION', max_length=1000, blank=True, null=True)  # Field name made lowercase.
#     cantidad = models.DecimalField(db_column='CANTIDAD', max_digits=23, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     claveunidad = models.CharField(db_column='CLAVEUNIDAD', max_length=19, blank=True, null=True)  # Field name made lowercase.
#     unidad = models.CharField(db_column='UNIDAD', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     dimensiones = models.CharField(db_column='DIMENSIONES', max_length=11, blank=True, null=True)  # Field name made lowercase.
#     materialpeligroso = models.CharField(db_column='MATERIALPELIGROSO', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     cvematerialpeligroso = models.CharField(db_column='CVEMATERIALPELIGROSO', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     embalaje = models.CharField(db_column='EMBALAJE', max_length=5, blank=True, null=True)  # Field name made lowercase.
#     descripembalaje = models.CharField(db_column='DESCRIPEMBALAJE', max_length=1000, blank=True, null=True)  # Field name made lowercase.
#     pesoenkg = models.DecimalField(db_column='PESOENKG', max_digits=11, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
#     valormercancia = models.DecimalField(db_column='VALORMERCANCIA', max_digits=11, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
#     moneda = models.CharField(db_column='MONEDA', max_length=3, blank=True, null=True)  # Field name made lowercase.
#     fraccionarancelaria = models.CharField(db_column='FRACCIONARANCELARIA', max_length=19, blank=True, null=True)  # Field name made lowercase.
#     uuidcomercioext = models.CharField(db_column='UUIDCOMERCIOEXT', max_length=49, blank=True, null=True)  # Field name made lowercase.
#     detallemercancia = models.SmallIntegerField(db_column='DETALLEMERCANCIA', blank=True, null=True)  # Field name made lowercase.
#     detallemercancia_unidadpeso = models.CharField(db_column='DETALLEMERCANCIA_UNIDADPESO', max_length=4, blank=True, null=True)  # Field name made lowercase.
#     detallemercancia_pesobruto = models.DecimalField(db_column='DETALLEMERCANCIA_PESOBRUTO', max_digits=11, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
#     detallemercancia_pesoneto = models.DecimalField(db_column='DETALLEMERCANCIA_PESONETO', max_digits=11, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
#     detallemercancia_pesotara = models.DecimalField(db_column='DETALLEMERCANCIA_PESOTARA', max_digits=11, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
#     detallemercancia_numpiezas = models.IntegerField(db_column='DETALLEMERCANCIA_NUMPIEZAS', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFDI33_CartaPorte_Mercancias'
#         unique_together = (('id_cartaporte_mercancia', 'lineamercancia'),)

# class Cfdi33CartaportePedimentos(models.Model):
#     id_cp_merancia_pedimento = models.IntegerField(db_column='ID_CP_MERANCIA_PEDIMENTO', primary_key=True)  # Field name made lowercase.
#     lineamercancia = models.IntegerField(db_column='LINEAMERCANCIA')  # Field name made lowercase.
#     lineapedimentomerca = models.IntegerField(db_column='LINEAPEDIMENTOMERCA')  # Field name made lowercase.
#     pedimento = models.CharField(db_column='PEDIMENTO', max_length=21, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFDI33_CartaPorte_Pedimentos'
#         unique_together = (('id_cp_merancia_pedimento', 'lineamercancia', 'lineapedimentomerca'),)

# class Cfdi33CartaporteSeguros(models.Model):
#     id_cp_seguros = models.IntegerField(db_column='ID_CP_SEGUROS', primary_key=True)  # Field name made lowercase.
#     asegurarespcivil = models.CharField(db_column='ASEGURARESPCIVIL', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     polizarespcivil = models.CharField(db_column='POLIZARESPCIVIL', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     aseguramedambiente = models.CharField(db_column='ASEGURAMEDAMBIENTE', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     polizamedambiente = models.CharField(db_column='POLIZAMEDAMBIENTE', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     aseguracarga = models.CharField(db_column='ASEGURACARGA', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     polizacarga = models.CharField(db_column='POLIZACARGA', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     primaseguro = models.DecimalField(db_column='PRIMASEGURO', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFDI33_CartaPorte_Seguros'

# class Cfdi33CartaporteUbicaciones(models.Model):
#     id_cartaporte_field = models.IntegerField(db_column='ID_CARTAPORTE_', primary_key=True)  # Field name made lowercase. Field renamed because it ended with '_'.
#     linea = models.IntegerField(db_column='LINEA')  # Field name made lowercase.
#     ubicacion_tipoestacion = models.CharField(db_column='UBICACION_TIPOESTACION', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     ubicacion_distanciarecorrida = models.DecimalField(db_column='UBICACION_DISTANCIARECORRIDA', max_digits=7, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     ubicacion_origen = models.SmallIntegerField(db_column='UBICACION_ORIGEN', blank=True, null=True)  # Field name made lowercase.
#     ubicacion_origen_idorigen = models.CharField(db_column='UBICACION_ORIGEN_IDORIGEN', max_length=8, blank=True, null=True)  # Field name made lowercase.
#     ubicacion_origen_rfcremitente = models.CharField(db_column='UBICACION_ORIGEN_RFCREMITENTE', max_length=19, blank=True, null=True)  # Field name made lowercase.
#     ubicacion_origen_nombreremitente = models.CharField(db_column='UBICACION_ORIGEN_NOMBREREMITENTE', max_length=254, blank=True, null=True)  # Field name made lowercase.
#     ubicacion_origen_numregidtrib = models.CharField(db_column='UBICACION_ORIGEN_NUMREGIDTRIB', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     ubicacion_origen_residenciafiscal = models.CharField(db_column='UBICACION_ORIGEN_RESIDENCIAFISCAL', max_length=3, blank=True, null=True)  # Field name made lowercase.
#     ubicacion_origen_nombreestacion = models.CharField(db_column='UBICACION_ORIGEN_NOMBREESTACION', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     ubicacion_origen_navegaciontrafico = models.CharField(db_column='UBICACION_ORIGEN_NAVEGACIONTRAFICO', max_length=9, blank=True, null=True)  # Field name made lowercase.
#     ubicacion_origen_fechahorasalida = models.CharField(db_column='UBICACION_ORIGEN_FECHAHORASALIDA', max_length=21, blank=True, null=True)  # Field name made lowercase.
#     ubicacion_destino = models.SmallIntegerField(db_column='UBICACION_DESTINO', blank=True, null=True)  # Field name made lowercase.
#     ubicacion_destino_iddestino = models.CharField(db_column='UBICACION_DESTINO_IDDESTINO', max_length=8, blank=True, null=True)  # Field name made lowercase.
#     ubicacion_destino_rfcdestinatario = models.CharField(db_column='UBICACION_DESTINO_RFCDESTINATARIO', max_length=19, blank=True, null=True)  # Field name made lowercase.
#     ubicacion_destino_numregidtrib = models.CharField(db_column='UBICACION_DESTINO_NUMREGIDTRIB', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     ubicacion_destino_residenciafiscal = models.CharField(db_column='UBICACION_DESTINO_RESIDENCIAFISCAL', max_length=3, blank=True, null=True)  # Field name made lowercase.
#     ubicacion_destino_numestacion = models.CharField(db_column='UBICACION_DESTINO_NUMESTACION', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     ubicacion_destino_nombreestacion = models.CharField(db_column='UBICACION_DESTINO_NOMBREESTACION', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     ubicacion_destino_navegaciontrafico = models.CharField(db_column='UBICACION_DESTINO_NAVEGACIONTRAFICO', max_length=8, blank=True, null=True)  # Field name made lowercase.
#     ubicacion_destino_fechahoraprogllegada = models.CharField(db_column='UBICACION_DESTINO_FECHAHORAPROGLLEGADA', max_length=19, blank=True, null=True)  # Field name made lowercase.
#     ubicacion_domicilio = models.SmallIntegerField(db_column='UBICACION_DOMICILIO', blank=True, null=True)  # Field name made lowercase.
#     ubicacion_domicilio_calle = models.CharField(db_column='UBICACION_DOMICILIO_CALLE', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     ubicacion_domicilio_numeroexterior = models.CharField(db_column='UBICACION_DOMICILIO_NUMEROEXTERIOR', max_length=19, blank=True, null=True)  # Field name made lowercase.
#     ubicacion_domicilio_numerointerior = models.CharField(db_column='UBICACION_DOMICILIO_NUMEROINTERIOR', max_length=9, blank=True, null=True)  # Field name made lowercase.
#     ubicacion_domicilio_colonia = models.CharField(db_column='UBICACION_DOMICILIO_COLONIA', max_length=120, blank=True, null=True)  # Field name made lowercase.
#     ubicacion_domicilio_localidad = models.CharField(db_column='UBICACION_DOMICILIO_LOCALIDAD', max_length=120, blank=True, null=True)  # Field name made lowercase.
#     ubicacion_domicilio_referencia = models.CharField(db_column='UBICACION_DOMICILIO_REFERENCIA', max_length=120, blank=True, null=True)  # Field name made lowercase.
#     ubicacion_domicilio_municipio = models.CharField(db_column='UBICACION_DOMICILIO_MUNICIPIO', max_length=120, blank=True, null=True)  # Field name made lowercase.
#     ubicacion_domicilio_estado = models.CharField(db_column='UBICACION_DOMICILIO_ESTADO', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     ubicacion_domicilio_pais = models.CharField(db_column='UBICACION_DOMICILIO_PAIS', max_length=3, blank=True, null=True)  # Field name made lowercase.
#     ubicacion_domicilio_codigopostal = models.CharField(db_column='UBICACION_DOMICILIO_CODIGOPOSTAL', max_length=12, blank=True, null=True)  # Field name made lowercase.
#     ubicacion_origen_numestacion = models.CharField(db_column='UBICACION_ORIGEN_NUMESTACION', max_length=9, blank=True, null=True)  # Field name made lowercase.
#     ubi_origen_fecha_clarion = models.IntegerField(db_column='UBI_ORIGEN_FECHA_CLARION', blank=True, null=True)  # Field name made lowercase.
#     ubi_destino_fecha_clarion = models.IntegerField(db_column='UBI_DESTINO_FECHA_CLARION', blank=True, null=True)  # Field name made lowercase.
#     ubicacion_destino_nombre = models.CharField(db_column='UBICACION_DESTINO_NOMBRE', max_length=254, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFDI33_CartaPorte_Ubicaciones'
#         unique_together = (('id_cartaporte_field', 'linea'),)

# class Cfdi33CatConfigtransporte(models.Model):
#     sysid = models.IntegerField(db_column='SYSID', primary_key=True)  # Field name made lowercase.
#     permisosct = models.CharField(db_column='PERMISOSCT', max_length=6, blank=True, null=True)  # Field name made lowercase.
#     numeropermisosct = models.CharField(db_column='NUMEROPERMISOSCT', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     nombre_aseguranza = models.CharField(db_column='NOMBRE_ASEGURANZA', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     num_poliza_seguro = models.CharField(db_column='NUM_POLIZA_SEGURO', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     id_configvehicular = models.CharField(db_column='ID_CONFIGVEHICULAR', max_length=7, blank=True, null=True)  # Field name made lowercase.
#     placa = models.CharField(db_column='PLACA', max_length=7, blank=True, null=True)  # Field name made lowercase.
#     aniomodelo = models.CharField(db_column='ANIOMODELO', max_length=4, blank=True, null=True)  # Field name made lowercase.
#     rem1_subtipo = models.CharField(db_column='REM1_SUBTIPO', max_length=7, blank=True, null=True)  # Field name made lowercase.
#     rem1_placa = models.CharField(db_column='REM1_PLACA', max_length=7, blank=True, null=True)  # Field name made lowercase.
#     rem2_subtipo = models.CharField(db_column='REM2_SUBTIPO', max_length=7, blank=True, null=True)  # Field name made lowercase.
#     rem2_placa = models.CharField(db_column='REM2_PLACA', max_length=7, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFDI33_Cat_ConfigTransporte'

# class Cfdi33CatFigurastransporte(models.Model):
#     sysid_figtransp = models.IntegerField(db_column='SYSID_FIGTRANSP', primary_key=True)  # Field name made lowercase.
#     tipofigura = models.CharField(db_column='TIPOFIGURA', max_length=19, blank=True, null=True)  # Field name made lowercase.
#     rfc = models.CharField(db_column='RFC', max_length=19, blank=True, null=True)  # Field name made lowercase.
#     nombre = models.CharField(db_column='NOMBRE', max_length=254, blank=True, null=True)  # Field name made lowercase.
#     numregid = models.CharField(db_column='NUMREGID', max_length=39, blank=True, null=True)  # Field name made lowercase.
#     recidenciafiscal = models.CharField(db_column='RECIDENCIAFISCAL', max_length=19, blank=True, null=True)  # Field name made lowercase.
#     calle = models.CharField(db_column='CALLE', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     numext = models.CharField(db_column='NUMEXT', max_length=9, blank=True, null=True)  # Field name made lowercase.
#     numint = models.CharField(db_column='NUMINT', max_length=9, blank=True, null=True)  # Field name made lowercase.
#     colonia = models.CharField(db_column='COLONIA', max_length=118, blank=True, null=True)  # Field name made lowercase.
#     referencia = models.CharField(db_column='REFERENCIA', max_length=23, blank=True, null=True)  # Field name made lowercase.
#     municipo = models.CharField(db_column='MUNICIPO', max_length=120, blank=True, null=True)  # Field name made lowercase.
#     estado = models.CharField(db_column='ESTADO', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     codigopostal = models.CharField(db_column='CODIGOPOSTAL', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     localidad = models.CharField(db_column='LOCALIDAD', max_length=120, blank=True, null=True)  # Field name made lowercase.
#     pais = models.CharField(db_column='PAIS', max_length=3, blank=True, null=True)  # Field name made lowercase.
#     numlicencia = models.CharField(db_column='NUMLICENCIA', max_length=16, blank=True, null=True)  # Field name made lowercase.
#     nombrefigura = models.CharField(db_column='NOMBREFIGURA', max_length=254, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFDI33_Cat_FigurasTransporte'

# class Cfdi33CatTransportes(models.Model):
#     sysid_transporte = models.IntegerField(db_column='SYSID_TRANSPORTE', primary_key=True)  # Field name made lowercase.
#     id_configvehicular = models.CharField(db_column='ID_CONFIGVEHICULAR', max_length=7, blank=True, null=True)  # Field name made lowercase.
#     placa = models.CharField(db_column='PLACA', max_length=7, blank=True, null=True)  # Field name made lowercase.
#     aniomodelo = models.CharField(db_column='ANIOMODELO', max_length=4, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFDI33_Cat_Transportes'

# class Cfdi33CatUbicaciones(models.Model):
#     sysid_ubica = models.IntegerField(db_column='SYSID_UBICA', primary_key=True)  # Field name made lowercase.
#     tipo_ubicacion = models.CharField(db_column='TIPO_UBICACION', max_length=9, blank=True, null=True)  # Field name made lowercase.
#     id_ori_des = models.CharField(db_column='ID_ORI_DES', max_length=8, blank=True, null=True)  # Field name made lowercase.
#     rfc = models.CharField(db_column='RFC', max_length=19, blank=True, null=True)  # Field name made lowercase.
#     nombre = models.CharField(db_column='NOMBRE', max_length=254, blank=True, null=True)  # Field name made lowercase.
#     numregid = models.CharField(db_column='NUMREGID', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     residecniafiscal = models.CharField(db_column='RESIDECNIAFISCAL', max_length=3, blank=True, null=True)  # Field name made lowercase.
#     numext = models.CharField(db_column='NUMEXT', max_length=19, blank=True, null=True)  # Field name made lowercase.
#     numint = models.CharField(db_column='NUMINT', max_length=9, blank=True, null=True)  # Field name made lowercase.
#     colonia = models.CharField(db_column='COLONIA', max_length=120, blank=True, null=True)  # Field name made lowercase.
#     localidad = models.CharField(db_column='LOCALIDAD', max_length=120, blank=True, null=True)  # Field name made lowercase.
#     referencia = models.CharField(db_column='REFERENCIA', max_length=120, blank=True, null=True)  # Field name made lowercase.
#     municipio = models.CharField(db_column='MUNICIPIO', max_length=120, blank=True, null=True)  # Field name made lowercase.
#     estado = models.CharField(db_column='ESTADO', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     pais = models.CharField(db_column='PAIS', max_length=3, blank=True, null=True)  # Field name made lowercase.
#     codigopostal = models.CharField(db_column='CODIGOPOSTAL', max_length=12, blank=True, null=True)  # Field name made lowercase.
#     calle = models.CharField(db_column='CALLE', max_length=100, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFDI33_Cat_Ubicaciones'

# class Cfdi33Claveprodstcc(models.Model):
#     clave_stcc = models.CharField(db_column='Clave_STCC', primary_key=True, max_length=9)  # Field name made lowercase.
#     descripcion = models.CharField(db_column='Descripcion', max_length=155, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFDI33_ClaveProdSTCC'

# class Cfdi33Clavetipocarga(models.Model):
#     clave_tipo_carga = models.CharField(db_column='Clave_Tipo_Carga', primary_key=True, max_length=3)  # Field name made lowercase.
#     descripcion = models.CharField(db_column='Descripcion', max_length=65, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFDI33_ClaveTipoCarga'

# class Cfdi33Claveunidadpeso(models.Model):
#     clave_unidad = models.CharField(db_column='Clave_Unidad', primary_key=True, max_length=4)  # Field name made lowercase.
#     nombre = models.CharField(db_column='Nombre', max_length=155)  # Field name made lowercase.
#     descripcion = models.CharField(db_column='Descripcion', max_length=999, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFDI33_ClaveUnidadPeso'


# class Cfdi33Codigotransporteaereo(models.Model):
#     clave_identificacion = models.CharField(db_column='Clave_Identificacion', primary_key=True, max_length=6)  # Field name made lowercase.
#     nacionalidad = models.CharField(db_column='Nacionalidad', max_length=64, blank=True, null=True)  # Field name made lowercase.
#     nombre_aerolinea = models.CharField(db_column='Nombre_aerolinea', max_length=155, blank=True, null=True)  # Field name made lowercase.
#     oaci = models.CharField(db_column='OACI', max_length=5, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFDI33_CodigoTransporteAereo'


# class Cfdi33Colonia(models.Model):
#     colonia = models.CharField(db_column='COLONIA', primary_key=True, max_length=5)  # Field name made lowercase.
#     cp = models.CharField(db_column='CP', max_length=8)  # Field name made lowercase.
#     nombre_asentamiento = models.CharField(db_column='NOMBRE_ASENTAMIENTO', max_length=150, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFDI33_Colonia'
#         unique_together = (('colonia', 'cp'),)


# class Cfdi33Configautotransporte(models.Model):
#     clave_nomenclatura = models.CharField(db_column='Clave_Nomenclatura', primary_key=True, max_length=7)  # Field name made lowercase.
#     descripcion = models.CharField(db_column='Descripcion', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     numero_ejes = models.CharField(db_column='Numero_Ejes', max_length=3, blank=True, null=True)  # Field name made lowercase.
#     numero_llantas = models.CharField(db_column='Numero_llantas', max_length=25, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFDI33_ConfigAutotransporte'


# class Cfdi33Configmaritima(models.Model):
#     clave_conf_maritima = models.CharField(db_column='Clave_Conf_Maritima', primary_key=True, max_length=4)  # Field name made lowercase.
#     descripcion = models.CharField(db_column='Descripcion', max_length=64, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFDI33_ConfigMaritima'


# class Cfdi33Contenedor(models.Model):
#     clave_contenedor = models.CharField(db_column='Clave_Contenedor', primary_key=True, max_length=5)  # Field name made lowercase.
#     tipo_contenedor = models.CharField(db_column='Tipo_Contenedor', max_length=4, blank=True, null=True)  # Field name made lowercase.
#     descripcion = models.CharField(db_column='Descripcion', max_length=155, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFDI33_Contenedor'


# class Cfdi33Contenedormaritimo(models.Model):
#     clave_contenedor_maritimo = models.CharField(db_column='Clave_Contenedor_Maritimo', primary_key=True, max_length=6)  # Field name made lowercase.
#     descripcion = models.CharField(db_column='Descripcion', max_length=65, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFDI33_ContenedorMaritimo'


# class Cfdi33CvetransporteCp(models.Model):
#     clave_transporte = models.CharField(db_column='Clave_Transporte', primary_key=True, max_length=2)  # Field name made lowercase.
#     descripcion_transporte = models.CharField(db_column='Descripcion_Transporte', max_length=25, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFDI33_CveTransporte_CP'


# class Cfdi33Derechosdepaso(models.Model):
#     clave_derecho_peso = models.CharField(db_column='Clave_Derecho_Peso', primary_key=True, max_length=7)  # Field name made lowercase.
#     derecho_peso = models.CharField(db_column='Derecho_peso', max_length=7, blank=True, null=True)  # Field name made lowercase.
#     entre = models.CharField(db_column='Entre', max_length=155, blank=True, null=True)  # Field name made lowercase.
#     hasta = models.CharField(db_column='Hasta', max_length=155, blank=True, null=True)  # Field name made lowercase.
#     otorga_recibe = models.CharField(db_column='Otorga_Recibe', max_length=55, blank=True, null=True)  # Field name made lowercase.
#     concesionario = models.CharField(db_column='Concesionario', max_length=255, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFDI33_DerechosDePaso'


# class Cfdi33Estaciones(models.Model):
#     clave_transporte = models.CharField(db_column='Clave_Transporte', primary_key=True, max_length=2)  # Field name made lowercase.
#     clave_identificacion = models.CharField(db_column='Clave_Identificacion', max_length=6)  # Field name made lowercase.
#     descripcion = models.CharField(db_column='Descripcion', max_length=65, blank=True, null=True)  # Field name made lowercase.
#     nacionalidad = models.CharField(db_column='Nacionalidad', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     iata = models.CharField(db_column='IATA', max_length=4, blank=True, null=True)  # Field name made lowercase.
#     linea_ferrea = models.CharField(db_column='Linea_Ferrea', max_length=9, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFDI33_Estaciones'
#         unique_together = (('clave_transporte', 'clave_identificacion'),)


# class Cfdi33Estados(models.Model):
#     estado = models.CharField(db_column='ESTADO', primary_key=True, max_length=4)  # Field name made lowercase.
#     nombre_estado = models.CharField(db_column='NOMBRE_ESTADO', max_length=64, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFDI33_Estados'


# class Cfdi33Exportacion(models.Model):
#     id_clave = models.CharField(db_column='ID_CLAVE', primary_key=True, max_length=2)  # Field name made lowercase.
#     descripcion = models.CharField(db_column='DESCRIPCION', max_length=19, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFDI33_Exportacion'


# class Cfdi33Figuratransporte(models.Model):
#     id_fac_cartaporte_figuratrans = models.IntegerField(db_column='ID_FAC_CARTAPORTE_FIGURATRANS', primary_key=True)  # Field name made lowercase.
#     linea_figuratrans = models.IntegerField(db_column='LINEA_FIGURATRANS')  # Field name made lowercase.
#     tipofigura = models.CharField(db_column='TIPOFIGURA', max_length=19, blank=True, null=True)  # Field name made lowercase.
#     ope_rfcoperador = models.CharField(db_column='OPE_RFCOPERADOR', max_length=18, blank=True, null=True)  # Field name made lowercase.
#     ope_numlicencia = models.CharField(db_column='OPE_NUMLICENCIA', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     ope_nombreoperador = models.CharField(db_column='OPE_NOMBREOPERADOR', max_length=254, blank=True, null=True)  # Field name made lowercase.
#     ope_numregidtriboperador = models.CharField(db_column='OPE_NUMREGIDTRIBOPERADOR', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     ope_residenciafiscaloperador = models.CharField(db_column='OPE_RESIDENCIAFISCALOPERADOR', max_length=3, blank=True, null=True)  # Field name made lowercase.
#     prop_rfcpropietario = models.CharField(db_column='PROP_RFCPROPIETARIO', max_length=18, blank=True, null=True)  # Field name made lowercase.
#     prop_nombrepropietario = models.CharField(db_column='PROP_NOMBREPROPIETARIO', max_length=254, blank=True, null=True)  # Field name made lowercase.
#     prop_numregidtribpropietario = models.CharField(db_column='PROP_NUMREGIDTRIBPROPIETARIO', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     prop_residenciafiscalpropietario = models.CharField(db_column='PROP_RESIDENCIAFISCALPROPIETARIO', max_length=3, blank=True, null=True)  # Field name made lowercase.
#     arre_rfcarrendatario = models.CharField(db_column='ARRE_RFCARRENDATARIO', max_length=18, blank=True, null=True)  # Field name made lowercase.
#     arre_nombrearrendatario = models.CharField(db_column='ARRE_NOMBREARRENDATARIO', max_length=24, blank=True, null=True)  # Field name made lowercase.
#     arre_numregidtribarrendatario = models.CharField(db_column='ARRE_NUMREGIDTRIBARRENDATARIO', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     arre_residenciafiscalarrendatario = models.CharField(db_column='ARRE_RESIDENCIAFISCALARRENDATARIO', max_length=3, blank=True, null=True)  # Field name made lowercase.
#     noti_rfcnotificado = models.CharField(db_column='NOTI_RFCNOTIFICADO', max_length=18, blank=True, null=True)  # Field name made lowercase.
#     noti_nombrenotificado = models.CharField(db_column='NOTI_NOMBRENOTIFICADO', max_length=254, blank=True, null=True)  # Field name made lowercase.
#     noti_numregidtribnotificado = models.CharField(db_column='NOTI_NUMREGIDTRIBNOTIFICADO', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     noti_residenciafiscalnotificado = models.CharField(db_column='NOTI_RESIDENCIAFISCALNOTIFICADO', max_length=3, blank=True, null=True)  # Field name made lowercase.
#     calle = models.CharField(db_column='CALLE', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     numeroexterior = models.CharField(db_column='NUMEROEXTERIOR', max_length=9, blank=True, null=True)  # Field name made lowercase.
#     numerointerior = models.CharField(db_column='NUMEROINTERIOR', max_length=9, blank=True, null=True)  # Field name made lowercase.
#     colonia = models.CharField(db_column='COLONIA', max_length=119, blank=True, null=True)  # Field name made lowercase.
#     referencia = models.CharField(db_column='REFERENCIA', max_length=24, blank=True, null=True)  # Field name made lowercase.
#     municipio = models.CharField(db_column='MUNICIPIO', max_length=120, blank=True, null=True)  # Field name made lowercase.
#     estado = models.CharField(db_column='ESTADO', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     codigopostal = models.CharField(db_column='CODIGOPOSTAL', max_length=12, blank=True, null=True)  # Field name made lowercase.
#     localidad = models.CharField(db_column='LOCALIDAD', max_length=120, blank=True, null=True)  # Field name made lowercase.
#     pais = models.CharField(db_column='PAIS', max_length=3, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFDI33_FiguraTransporte'
#         unique_together = (('id_fac_cartaporte_figuratrans', 'linea_figuratrans'),)


# class Cfdi33Fraccion(models.Model):
#     fraccionarencelaria = models.CharField(db_column='FRACCIONARENCELARIA', primary_key=True, max_length=10)  # Field name made lowercase.
#     descripcion = models.TextField(db_column='DESCRIPCION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     um = models.CharField(db_column='UM', max_length=4, blank=True, null=True)  # Field name made lowercase.
#     imp = models.CharField(db_column='IMP', max_length=19, blank=True, null=True)  # Field name made lowercase.
#     exp = models.CharField(db_column='EXP', max_length=4, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFDI33_Fraccion'


# class Cfdi33Historicouuids(models.Model):
#     consecutivo = models.IntegerField(db_column='CONSECUTIVO', blank=True, null=True,primary_key=True)  # Field name made lowercase.
#     linea = models.IntegerField(db_column='LINEA', blank=True, null=True)  # Field name made lowercase.
#     tipocomprobante = models.CharField(db_column='TIPOCOMPROBANTE', max_length=19, blank=True, null=True)  # Field name made lowercase.
#     cadenaoriginal = models.TextField(db_column='CADENAORIGINAL', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     cadenaoriginalsat = models.TextField(db_column='CADENAORIGINALSAT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sellodigital = models.TextField(db_column='SELLODIGITAL', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sellodigitalsat = models.TextField(db_column='SELLODIGITALSAT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     nocertificado = models.CharField(db_column='NOCERTIFICADO', max_length=999, blank=True, null=True)  # Field name made lowercase.
#     nocertificadosat = models.CharField(db_column='NOCERTIFICADOSAT', max_length=999, blank=True, null=True)  # Field name made lowercase.
#     fechacertificacion = models.CharField(db_column='FECHACERTIFICACION', max_length=254, blank=True, null=True)  # Field name made lowercase.
#     foliopac = models.CharField(db_column='FOLIOPAC', max_length=999, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFDI33_HistoricoUUIDs'
#         unique_together = (('consecutivo', 'linea'),)


# class Cfdi33Incoterm(models.Model):
#     incoterm = models.CharField(db_column='INCOTERM', primary_key=True, max_length=5)  # Field name made lowercase.
#     descripcion = models.CharField(db_column='DESCRIPCION', max_length=150, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFDI33_INCOTERM'


# class Cfdi33Localidades(models.Model):
#     localidades = models.CharField(db_column='LOCALIDADES', primary_key=True, max_length=3)  # Field name made lowercase.
#     estado = models.CharField(db_column='ESTADO', max_length=4)  # Field name made lowercase.
#     descripcion = models.CharField(db_column='DESCRIPCION', max_length=150, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFDI33_Localidades'
#         unique_together = (('localidades', 'estado'),)


# class Cfdi33MotivoTraslado(models.Model):
#     motivo_traslado = models.CharField(db_column='MOTIVO_TRASLADO', primary_key=True, max_length=3)  # Field name made lowercase.
#     descripcion = models.CharField(db_column='DESCRIPCION', max_length=64, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFDI33_MOTIVO_TRASLADO'


# class Cfdi33Materialpeligroso(models.Model):
#     clave_material_peligroso = models.CharField(db_column='Clave_Material_Peligroso', primary_key=True, max_length=10)  # Field name made lowercase.
#     descripcion = models.CharField(db_column='Descripcion', max_length=1000, blank=True, null=True)  # Field name made lowercase.
#     clase_div = models.CharField(db_column='Clase_div', max_length=55, blank=True, null=True)  # Field name made lowercase.
#     peligro_secundario = models.CharField(db_column='Peligro_Secundario', max_length=55, blank=True, null=True)  # Field name made lowercase.
#     emb_env_onu = models.CharField(db_column='EMB_ENV_ONU', max_length=55, blank=True, null=True)  # Field name made lowercase.
#     disp_espec = models.CharField(db_column='Disp_Espec', max_length=55, blank=True, null=True)  # Field name made lowercase.
#     cant_limitadas = models.CharField(db_column='Cant_Limitadas', max_length=55, blank=True, null=True)  # Field name made lowercase.
#     exceptuadas = models.CharField(db_column='Exceptuadas', max_length=55, blank=True, null=True)  # Field name made lowercase.
#     inst_emb_env = models.CharField(db_column='Inst_EMB_ENV', max_length=55, blank=True, null=True)  # Field name made lowercase.
#     disp_espec_emba_env = models.CharField(db_column='Disp_Espec_Emba_ENV', max_length=55, blank=True, null=True)  # Field name made lowercase.
#     cisternasport_inst_transp = models.CharField(db_column='CisternasPort_Inst_transp', max_length=55, blank=True, null=True)  # Field name made lowercase.
#     rig_disp_espec = models.CharField(db_column='RIG_Disp_Espec', max_length=55, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFDI33_MaterialPeligroso'


# class Cfdi33Meses(models.Model):
#     id_clave = models.CharField(db_column='ID_CLAVE', primary_key=True, max_length=2)  # Field name made lowercase.
#     descripcion = models.CharField(db_column='DESCRIPCION', max_length=49, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFDI33_Meses'


# class Cfdi33MotivoCancelacion(models.Model):
#     id_cancelacion = models.CharField(db_column='ID_CANCELACION', primary_key=True, max_length=2)  # Field name made lowercase.
#     descripcion = models.CharField(db_column='DESCRIPCION', max_length=249, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFDI33_Motivo_Cancelacion'


# class Cfdi33Municipios(models.Model):
#     municipio = models.CharField(db_column='MUNICIPIO', primary_key=True, max_length=4)  # Field name made lowercase.
#     estado = models.CharField(db_column='ESTADO', max_length=4)  # Field name made lowercase.
#     descripcion = models.CharField(db_column='DESCRIPCION', max_length=149, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFDI33_Municipios'
#         unique_together = (('municipio', 'estado'),)


# class Cfdi33Numautorizacionnaviero(models.Model):
#     numero_autorizacion = models.CharField(db_column='Numero_Autorizacion', primary_key=True, max_length=20)  # Field name made lowercase.
#     inicio_vigencia = models.IntegerField(db_column='Inicio_Vigencia', blank=True, null=True)  # Field name made lowercase.
#     inicio_vigencia_field = models.CharField(db_column='Inicio_Vigencia_', max_length=9, blank=True, null=True)  # Field name made lowercase. Field renamed because it ended with '_'.
#     fin_vigencia = models.IntegerField(db_column='Fin_Vigencia', blank=True, null=True)  # Field name made lowercase.
#     fin_vigencia_field = models.CharField(db_column='Fin_Vigencia_', max_length=9, blank=True, null=True)  # Field name made lowercase. Field renamed because it ended with '_'.

#     class Meta:
#         managed = False
#         db_table = 'CFDI33_NumAutorizacionNaviero'


# class Cfdi33Objetoimp(models.Model):
#     id_clave = models.CharField(db_column='ID_CLAVE', primary_key=True, max_length=2)  # Field name made lowercase.
#     descripcion = models.CharField(db_column='DESCRIPCION', max_length=49, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFDI33_ObjetoImp'


# class Cfdi33Partestransporte(models.Model):
#     id_parte_transporte = models.IntegerField(db_column='ID_PARTE_TRANSPORTE', primary_key=True)  # Field name made lowercase.
#     id_linea_figura = models.IntegerField(db_column='ID_LINEA_FIGURA')  # Field name made lowercase.
#     linea_parte_transporte = models.IntegerField(db_column='LINEA_PARTE_TRANSPORTE')  # Field name made lowercase.
#     partetransporte = models.CharField(db_column='PARTETRANSPORTE', max_length=9, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFDI33_PartesTransporte'
#         unique_together = (('id_parte_transporte', 'id_linea_figura', 'linea_parte_transporte'),)


# class Cfdi33PartestransporteC(models.Model):
#     clave = models.CharField(db_column='CLAVE', primary_key=True, max_length=4)  # Field name made lowercase.
#     descripcion = models.CharField(db_column='DESCRIPCION', max_length=54, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFDI33_PartesTransporte_c'


# class Cfdi33Periodicidad(models.Model):
#     id_clave = models.CharField(db_column='ID_CLAVE', primary_key=True, max_length=2)  # Field name made lowercase.
#     descripcion = models.CharField(db_column='DESCRIPCION', max_length=14, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFDI33_Periodicidad'


# class Cfdi33Remolques(models.Model):
#     sysid_remolque = models.IntegerField(db_column='SYSID_REMOLQUE', primary_key=True)  # Field name made lowercase.
#     rem1_subtipo = models.CharField(db_column='REM1_SUBTIPO', max_length=7, blank=True, null=True)  # Field name made lowercase.
#     rem1_placa = models.CharField(db_column='REM1_PLACA', max_length=7, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFDI33_Remolques'


# class Cfdi33Subtiporem(models.Model):
#     clave_remolque = models.CharField(db_column='Clave_Remolque', primary_key=True, max_length=7)  # Field name made lowercase.
#     descripcion = models.CharField(db_column='Descripcion', max_length=255, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFDI33_SubTipoRem'


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


# class Cfdi33Tipocarro(models.Model):
#     clave_tipocarro = models.CharField(db_column='Clave_TipoCarro', primary_key=True, max_length=5)  # Field name made lowercase.
#     tipo_carro = models.CharField(db_column='Tipo_Carro', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     descripcion = models.CharField(db_column='Descripcion', max_length=155, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFDI33_TipoCarro'


# class Cfdi33Tipodeservicio(models.Model):
#     clave_tiposervicio = models.CharField(db_column='Clave_TipoServicio', primary_key=True, max_length=4)  # Field name made lowercase.
#     descripcion = models.CharField(db_column='Descripcion', max_length=55)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFDI33_TipoDeServicio'


# class Cfdi33Tipoembalaje(models.Model):
#     clave_designacion = models.CharField(db_column='Clave_Designacion', primary_key=True, max_length=5)  # Field name made lowercase.
#     descripcion = models.CharField(db_column='Descripcion', max_length=255, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFDI33_TipoEmbalaje'


# class Cfdi33Tipoestacion(models.Model):
#     clave_estacion = models.CharField(db_column='Clave_Estacion', primary_key=True, max_length=2)  # Field name made lowercase.
#     descripcion_tipo_estacion = models.CharField(db_column='Descripcion_Tipo_Estacion', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     clave_transporte = models.CharField(db_column='Clave_Transporte', max_length=19, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFDI33_TipoEstacion'


# class Cfdi33Tipopermiso(models.Model):
#     clave = models.CharField(db_column='Clave', primary_key=True, max_length=6)  # Field name made lowercase.
#     descripcion = models.CharField(db_column='Descripcion', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     clave_transporte = models.CharField(db_column='Clave_Transporte', max_length=2, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFDI33_TipoPermiso'


# class Cfdi33TranmarContenedores(models.Model):
#     id_cartaporte = models.IntegerField(db_column='ID_CARTAPORTE', primary_key=True)  # Field name made lowercase.
#     linea_contenedor = models.IntegerField(db_column='LINEA_CONTENEDOR')  # Field name made lowercase.
#     matriculacontenedor = models.CharField(db_column='MATRICULACONTENEDOR', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     tipocontenedor = models.CharField(db_column='TIPOCONTENEDOR', max_length=6, blank=True, null=True)  # Field name made lowercase.
#     numprecinto = models.CharField(db_column='NUMPRECINTO', max_length=20, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFDI33_TranMar_Contenedores'
#         unique_together = (('id_cartaporte', 'linea_contenedor'),)


# class Cfdi33UnidadMedidaAduana(models.Model):
#     unidad_medida_aduana = models.IntegerField(db_column='UNIDAD_MEDIDA_ADUANA', primary_key=True)  # Field name made lowercase.
#     descripcion = models.CharField(db_column='DESCRIPCION', max_length=54, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFDI33_Unidad_Medida_Aduana'


# class CfdiAddendasDatos(models.Model):
#     id_addenda = models.IntegerField(db_column='ID_ADDENDA', primary_key=True)  # Field name made lowercase.
#     es_padre = models.SmallIntegerField(db_column='ES_PADRE', blank=True, null=True)  # Field name made lowercase.
#     p_nombre = models.CharField(db_column='P_NOMBRE', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     ip_p = models.IntegerField(db_column='IP_P', blank=True, null=True)  # Field name made lowercase.
#     dato = models.TextField(db_column='DATO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     factura = models.IntegerField(db_column='FACTURA')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CFDI_Addendas_Datos'
#         unique_together = (('id_addenda', 'factura'),)

# class CfdiAddendas(models.Model):
#     id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
#     es_padre = models.SmallIntegerField(db_column='ES_PADRE', blank=True, null=True)  # Field name made lowercase.
#     p_nombre = models.CharField(db_column='P_NOMBRE', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     id_p = models.IntegerField(db_column='ID_P', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'Cfdi_Addendas'
#         unique_together = (('id', 'id_p'),)


# class CfdiIne(models.Model):
#     id_factura = models.IntegerField(db_column='ID_FACTURA', primary_key=True)  # Field name made lowercase.
#     linea = models.IntegerField(db_column='LINEA')  # Field name made lowercase.
#     idcontabilidad = models.CharField(db_column='IDCONTABILIDAD', max_length=24, blank=True, null=True)  # Field name made lowercase.
#     claveentidad = models.CharField(db_column='CLAVEENTIDAD', max_length=24, blank=True, null=True)  # Field name made lowercase.
#     ambito = models.CharField(db_column='AMBITO', max_length=24, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'Cfdi_INE'
#         unique_together = (('id_factura', 'linea'),)

# class Facexpoa1(models.Model):
#     sysid = models.IntegerField(db_column='SYSID', primary_key=True)  # Field name made lowercase.
#     factura = models.IntegerField(db_column='FACTURA', blank=True, null=True)  # Field name made lowercase.
#     version = models.DecimalField(db_column='VERSION', max_digits=7, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     tipooperacion = models.CharField(db_column='TIPOOPERACION', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     clavedepedimento = models.CharField(db_column='CLAVEDEPEDIMENTO', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     certificadoorigen = models.IntegerField(db_column='CERTIFICADOORIGEN', blank=True, null=True)  # Field name made lowercase.
#     numcertificadoorigen = models.CharField(db_column='NUMCERTIFICADOORIGEN', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     numexpconfiable = models.CharField(db_column='NUMEXPCONFIABLE', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     incoterm = models.CharField(db_column='INCOTERM', max_length=3, blank=True, null=True)  # Field name made lowercase.
#     subdivision = models.IntegerField(db_column='SUBDIVISION', blank=True, null=True)  # Field name made lowercase.
#     observaciones = models.CharField(db_column='OBSERVACIONES', max_length=300, blank=True, null=True)  # Field name made lowercase.
#     tipocambiousd = models.DecimalField(db_column='TIPOCAMBIOUSD', max_digits=9, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     totalusd = models.DecimalField(db_column='TOTALUSD', max_digits=11, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     emisorcurp = models.CharField(db_column='EMISORCURP', max_length=18, blank=True, null=True)  # Field name made lowercase.
#     receptorcurp = models.CharField(db_column='RECEPTORCURP', max_length=18, blank=True, null=True)  # Field name made lowercase.
#     receptornumregidtrib = models.CharField(db_column='RECEPTORNUMREGIDTRIB', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     destnumregidtrib = models.CharField(db_column='DESTNUMREGIDTRIB', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     destrfc = models.CharField(db_column='DESTRFC', max_length=13, blank=True, null=True)  # Field name made lowercase.
#     destcurp = models.CharField(db_column='DESTCURP', max_length=18, blank=True, null=True)  # Field name made lowercase.
#     destnombre = models.CharField(db_column='DESTNOMBRE', max_length=300, blank=True, null=True)  # Field name made lowercase.
#     destcalle = models.CharField(db_column='DESTCALLE', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     destnumexterior = models.CharField(db_column='DESTNUMEXTERIOR', max_length=55, blank=True, null=True)  # Field name made lowercase.
#     destnuminterior = models.CharField(db_column='DESTNUMINTERIOR', max_length=55, blank=True, null=True)  # Field name made lowercase.
#     destcolonia = models.CharField(db_column='DESTCOLONIA', max_length=120, blank=True, null=True)  # Field name made lowercase.
#     destlocalidad = models.CharField(db_column='DESTLOCALIDAD', max_length=120, blank=True, null=True)  # Field name made lowercase.
#     destreferencia = models.CharField(db_column='DESTREFERENCIA', max_length=120, blank=True, null=True)  # Field name made lowercase.
#     destmunicipio = models.CharField(db_column='DESTMUNICIPIO', max_length=120, blank=True, null=True)  # Field name made lowercase.
#     destestado = models.CharField(db_column='DESTESTADO', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     destpais = models.CharField(db_column='DESTPAIS', max_length=3, blank=True, null=True)  # Field name made lowercase.
#     destcodigopostal = models.CharField(db_column='DESTCODIGOPOSTAL', max_length=12, blank=True, null=True)  # Field name made lowercase.
#     uuid = models.CharField(db_column='UUID', max_length=38, blank=True, null=True)  # Field name made lowercase.
#     pathpdfcfdi = models.CharField(db_column='PATHPDFCFDI', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     pathxmlcfdi = models.CharField(db_column='PATHXMLCFDI', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     aduanadespacho = models.CharField(db_column='ADUANADESPACHO', max_length=4, blank=True, null=True)  # Field name made lowercase.
#     patente = models.CharField(db_column='PATENTE', max_length=4, blank=True, null=True)  # Field name made lowercase.
#     pedmiento = models.CharField(db_column='PEDMIENTO', max_length=7, blank=True, null=True)  # Field name made lowercase.
#     numerofactura = models.CharField(db_column='NUMEROFACTURA', max_length=14, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'FacExpoA1'


# class Facexpoa1Mercancias(models.Model):
#     facexpoa1_id = models.IntegerField(db_column='FACEXPOA1_ID', primary_key=True)  # Field name made lowercase.
#     linea = models.IntegerField(db_column='LINEA')  # Field name made lowercase.
#     noidentificacion = models.CharField(db_column='NOIDENTIFICACION', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     fraccionarancelaria = models.CharField(db_column='FRACCIONARANCELARIA', max_length=8, blank=True, null=True)  # Field name made lowercase.
#     cantidadaduana = models.DecimalField(db_column='CANTIDADADUANA', max_digits=15, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
#     unidadaduana = models.IntegerField(db_column='UNIDADADUANA', blank=True, null=True)  # Field name made lowercase.
#     valorunitarioaduana = models.DecimalField(db_column='VALORUNITARIOADUANA', max_digits=13, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     valordolares = models.DecimalField(db_column='VALORDOLARES', max_digits=13, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     factura = models.CharField(db_column='FACTURA', max_length=14, blank=True, null=True)  # Field name made lowercase.
#     descripcion = models.TextField(db_column='DESCRIPCION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

#     class Meta:
#         managed = False
#         db_table = 'FacExpoA1Mercancias'
#         unique_together = (('facexpoa1_id', 'linea'),)


# class Facexpoa1Mercanciasde(models.Model):
#     facexpoa1_id = models.IntegerField(db_column='FACEXPOA1_ID', primary_key=True)  # Field name made lowercase.
#     facexpoa1_merlinea = models.IntegerField(db_column='FACEXPOA1_MERLINEA')  # Field name made lowercase.
#     linea = models.IntegerField(db_column='LINEA')  # Field name made lowercase.
#     marca = models.CharField(db_column='MARCA', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     modelo = models.CharField(db_column='MODELO', max_length=80, blank=True, null=True)  # Field name made lowercase.
#     submodelo = models.CharField(db_column='SUBMODELO', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     numeroserie = models.CharField(db_column='NUMEROSERIE', max_length=40, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'FacExpoA1MercanciasDE'
#         unique_together = (('facexpoa1_id', 'facexpoa1_merlinea', 'linea'),)


# class Facnotarioadquiriente(models.Model):
#     consecutivo = models.IntegerField(db_column='CONSECUTIVO', primary_key=True)  # Field name made lowercase.
#     nopersona = models.IntegerField(db_column='NOPERSONA')  # Field name made lowercase.
#     nombre = models.CharField(db_column='NOMBRE', max_length=254, blank=True, null=True)  # Field name made lowercase.
#     apellidopaterno = models.CharField(db_column='APELLIDOPATERNO', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     apellidomaterno = models.CharField(db_column='APELLIDOMATERNO', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     rfc = models.CharField(db_column='RFC', max_length=14, blank=True, null=True)  # Field name made lowercase.
#     curp = models.CharField(db_column='CURP', max_length=18, blank=True, null=True)  # Field name made lowercase.
#     porcentaje = models.DecimalField(db_column='PORCENTAJE', max_digits=7, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     persona = models.CharField(db_column='PERSONA', max_length=7, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'FacNotarioAdquiriente'
#         unique_together = (('consecutivo', 'nopersona'),)


# class Facnotarioenajenante(models.Model):
#     consecutivo = models.IntegerField(db_column='CONSECUTIVO', primary_key=True)  # Field name made lowercase.
#     nopersona = models.IntegerField(db_column='NOPERSONA')  # Field name made lowercase.
#     nombre = models.CharField(db_column='NOMBRE', max_length=254, blank=True, null=True)  # Field name made lowercase.
#     apellidopaterno = models.CharField(db_column='APELLIDOPATERNO', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     apellidomaterno = models.CharField(db_column='APELLIDOMATERNO', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     rfc = models.CharField(db_column='RFC', max_length=14, blank=True, null=True)  # Field name made lowercase.
#     curp = models.CharField(db_column='CURP', max_length=18, blank=True, null=True)  # Field name made lowercase.
#     porcentaje = models.DecimalField(db_column='PORCENTAJE', max_digits=7, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     persona = models.CharField(db_column='PERSONA', max_length=7, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'FacNotarioEnajenante'
#         unique_together = (('consecutivo', 'nopersona'),)


# class Factdettiporetenciones(models.Model):
#     consecutivofactura = models.IntegerField(db_column='CONSECUTIVOFACTURA', primary_key=True)  # Field name made lowercase.
#     linea = models.IntegerField(db_column='LINEA')  # Field name made lowercase.
#     claveretsat = models.IntegerField(db_column='CLAVERETSAT', blank=True, null=True)  # Field name made lowercase.
#     baseret = models.DecimalField(db_column='BASERET', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     retencion_impretenidos_impuesto = models.CharField(db_column='RETENCION_IMPRETENIDOS_IMPUESTO', max_length=19, blank=True, null=True)  # Field name made lowercase.
#     montoret_otros = models.DecimalField(db_column='MONTORET_OTROS', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     retencion_impretenidos_montoret = models.DecimalField(db_column='RETENCION_IMPRETENIDOS_MONTORET', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     tipopagoret = models.CharField(db_column='TIPOPAGORET', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     monttotpago = models.DecimalField(db_column='MONTTOTPAGO', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     monttotpagograv = models.DecimalField(db_column='MONTTOTPAGOGRAV', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     monttotpagoexent = models.DecimalField(db_column='MONTTOTPAGOEXENT', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     retencion_montototret = models.DecimalField(db_column='RETENCION_MONTOTOTRET', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'FactDetTipoRetenciones'
#         unique_together = (('consecutivofactura', 'linea'),)


# class Facturacomercioexterior(models.Model):
#     sysid = models.IntegerField(db_column='SYSID', primary_key=True)  # Field name made lowercase.
#     consecutivo = models.IntegerField(db_column='CONSECUTIVO', unique=True, blank=True, null=True)  # Field name made lowercase.
#     comercioexterior_version = models.CharField(db_column='COMERCIOEXTERIOR_VERSION', max_length=4, blank=True, null=True)  # Field name made lowercase.
#     comercioexterior_motivotraslado = models.CharField(db_column='COMERCIOEXTERIOR_MOTIVOTRASLADO', max_length=4, blank=True, null=True)  # Field name made lowercase.
#     comercioexterior_tipooperacion = models.CharField(db_column='COMERCIOEXTERIOR_TIPOOPERACION', max_length=4, blank=True, null=True)  # Field name made lowercase.
#     comercioexterior_clavedepedimento = models.CharField(db_column='COMERCIOEXTERIOR_CLAVEDEPEDIMENTO', max_length=4, blank=True, null=True)  # Field name made lowercase.
#     comercioexterior_certificadoorigen = models.IntegerField(db_column='COMERCIOEXTERIOR_CERTIFICADOORIGEN', blank=True, null=True)  # Field name made lowercase.
#     comercioexterior_numcertificadoorigen = models.CharField(db_column='COMERCIOEXTERIOR_NUMCERTIFICADOORIGEN', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     comercioexterior_numeroexportadorconfiable = models.CharField(db_column='COMERCIOEXTERIOR_NUMEROEXPORTADORCONFIABLE', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     comercioexterior_incoterm = models.CharField(db_column='COMERCIOEXTERIOR_INCOTERM', max_length=4, blank=True, null=True)  # Field name made lowercase.
#     comercioexterior_subdivision = models.IntegerField(db_column='COMERCIOEXTERIOR_SUBDIVISION', blank=True, null=True)  # Field name made lowercase.
#     comercioexterior_observaciones = models.CharField(db_column='COMERCIOEXTERIOR_OBSERVACIONES', max_length=300, blank=True, null=True)  # Field name made lowercase.
#     comercioexterior_tipocambiousd = models.DecimalField(db_column='COMERCIOEXTERIOR_TIPOCAMBIOUSD', max_digits=9, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     comercioexterior_totalusd = models.DecimalField(db_column='COMERCIOEXTERIOR_TOTALUSD', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     comercioexterior_emisor_curp = models.CharField(db_column='COMERCIOEXTERIOR_EMISOR_CURP', max_length=19, blank=True, null=True)  # Field name made lowercase.
#     comercioexterior_emisor_domicilio_calle = models.CharField(db_column='COMERCIOEXTERIOR_EMISOR_DOMICILIO_CALLE', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     comercioexterior_emisor_domicilio_numeroexterior = models.CharField(db_column='COMERCIOEXTERIOR_EMISOR_DOMICILIO_NUMEROEXTERIOR', max_length=55, blank=True, null=True)  # Field name made lowercase.
#     comercioexterior_emisor_domicilio_numerointerior = models.CharField(db_column='COMERCIOEXTERIOR_EMISOR_DOMICILIO_NUMEROINTERIOR', max_length=55, blank=True, null=True)  # Field name made lowercase.
#     comercioexterior_emisor_domicilio_colonia = models.CharField(db_column='COMERCIOEXTERIOR_EMISOR_DOMICILIO_COLONIA', max_length=4, blank=True, null=True)  # Field name made lowercase.
#     comercioexterior_emisor_domicilio_localidad = models.CharField(db_column='COMERCIOEXTERIOR_EMISOR_DOMICILIO_LOCALIDAD', max_length=4, blank=True, null=True)  # Field name made lowercase.
#     comercioexterior_emisor_domicilio_referencia = models.CharField(db_column='COMERCIOEXTERIOR_EMISOR_DOMICILIO_REFERENCIA', max_length=250, blank=True, null=True)  # Field name made lowercase.
#     comercioexterior_emisor_domicilio_municipio = models.CharField(db_column='COMERCIOEXTERIOR_EMISOR_DOMICILIO_MUNICIPIO', max_length=4, blank=True, null=True)  # Field name made lowercase.
#     comercioexterior_emisor_domicilio_estado = models.CharField(db_column='COMERCIOEXTERIOR_EMISOR_DOMICILIO_ESTADO', max_length=4, blank=True, null=True)  # Field name made lowercase.
#     comercioexterior_emisor_domicilio_pais = models.CharField(db_column='COMERCIOEXTERIOR_EMISOR_DOMICILIO_PAIS', max_length=4, blank=True, null=True)  # Field name made lowercase.
#     comercioexterior_emisor_domicilio_codigopostal = models.CharField(db_column='COMERCIOEXTERIOR_EMISOR_DOMICILIO_CODIGOPOSTAL', max_length=5, blank=True, null=True)  # Field name made lowercase.
#     comercioexterior_propietario_numregidtrib = models.CharField(db_column='COMERCIOEXTERIOR_PROPIETARIO_NUMREGIDTRIB', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     comercioexterior_propietario_residenciafiscal = models.CharField(db_column='COMERCIOEXTERIOR_PROPIETARIO_RESIDENCIAFISCAL', max_length=4, blank=True, null=True)  # Field name made lowercase.
#     comercioexterior_receptor_numregidtrib = models.CharField(db_column='COMERCIOEXTERIOR_RECEPTOR_NUMREGIDTRIB', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     comercioexterior_receptor_domicilio_calle = models.CharField(db_column='COMERCIOEXTERIOR_RECEPTOR_DOMICILIO_CALLE', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     comercioexterior_receptor_domicilio_numeroexterior = models.CharField(db_column='COMERCIOEXTERIOR_RECEPTOR_DOMICILIO_NUMEROEXTERIOR', max_length=55, blank=True, null=True)  # Field name made lowercase.
#     comercioexterior_receptor_domicilio_numerointerior = models.CharField(db_column='COMERCIOEXTERIOR_RECEPTOR_DOMICILIO_NUMEROINTERIOR', max_length=55, blank=True, null=True)  # Field name made lowercase.
#     comercioexterior_receptor_domicilio_colonia = models.CharField(db_column='COMERCIOEXTERIOR_RECEPTOR_DOMICILIO_COLONIA', max_length=120, blank=True, null=True)  # Field name made lowercase.
#     comercioexterior_receptor_domicilio_localidad = models.CharField(db_column='COMERCIOEXTERIOR_RECEPTOR_DOMICILIO_LOCALIDAD', max_length=120, blank=True, null=True)  # Field name made lowercase.
#     comercioexterior_receptor_domicilio_referencia = models.CharField(db_column='COMERCIOEXTERIOR_RECEPTOR_DOMICILIO_REFERENCIA', max_length=250, blank=True, null=True)  # Field name made lowercase.
#     comercioexterior_receptor_domicilio_municipio = models.CharField(db_column='COMERCIOEXTERIOR_RECEPTOR_DOMICILIO_MUNICIPIO', max_length=120, blank=True, null=True)  # Field name made lowercase.
#     comercioexterior_receptor_domicilio_estado = models.CharField(db_column='COMERCIOEXTERIOR_RECEPTOR_DOMICILIO_ESTADO', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     comercioexterior_receptor_domicilio_pais = models.CharField(db_column='COMERCIOEXTERIOR_RECEPTOR_DOMICILIO_PAIS', max_length=4, blank=True, null=True)  # Field name made lowercase.
#     comercioexterior_receptor_domicilio_codigopostal = models.CharField(db_column='COMERCIOEXTERIOR_RECEPTOR_DOMICILIO_CODIGOPOSTAL', max_length=12, blank=True, null=True)  # Field name made lowercase.
#     comercioexterior_destinatario_numregidtrib = models.CharField(db_column='COMERCIOEXTERIOR_DESTINATARIO_NUMREGIDTRIB', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     comercioexterior_destinatario_nombre = models.CharField(db_column='COMERCIOEXTERIOR_DESTINATARIO_NOMBRE', max_length=300, blank=True, null=True)  # Field name made lowercase.
#     comercioexterior_destinatario_domicilio_calle = models.CharField(db_column='COMERCIOEXTERIOR_DESTINATARIO_DOMICILIO_CALLE', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     comercioexterior_destinatario_domicilio_numeroexterior = models.CharField(db_column='COMERCIOEXTERIOR_DESTINATARIO_DOMICILIO_NUMEROEXTERIOR', max_length=55, blank=True, null=True)  # Field name made lowercase.
#     comercioexterior_destinatario_domicilio_numerointerior = models.CharField(db_column='COMERCIOEXTERIOR_DESTINATARIO_DOMICILIO_NUMEROINTERIOR', max_length=55, blank=True, null=True)  # Field name made lowercase.
#     comercioexterior_destinatario_domicilio_colonia = models.CharField(db_column='COMERCIOEXTERIOR_DESTINATARIO_DOMICILIO_COLONIA', max_length=120, blank=True, null=True)  # Field name made lowercase.
#     comercioexterior_destinatario_domicilio_localidad = models.CharField(db_column='COMERCIOEXTERIOR_DESTINATARIO_DOMICILIO_LOCALIDAD', max_length=120, blank=True, null=True)  # Field name made lowercase.
#     comercioexterior_destinatario_domicilio_referencia = models.CharField(db_column='COMERCIOEXTERIOR_DESTINATARIO_DOMICILIO_REFERENCIA', max_length=250, blank=True, null=True)  # Field name made lowercase.
#     comercioexterior_destinatario_domicilio_municipio = models.CharField(db_column='COMERCIOEXTERIOR_DESTINATARIO_DOMICILIO_MUNICIPIO', max_length=120, blank=True, null=True)  # Field name made lowercase.
#     comercioexterior_destinatario_domicilio_estado = models.CharField(db_column='COMERCIOEXTERIOR_DESTINATARIO_DOMICILIO_ESTADO', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     comercioexterior_destinatario_domicilio_pais = models.CharField(db_column='COMERCIOEXTERIOR_DESTINATARIO_DOMICILIO_PAIS', max_length=4, blank=True, null=True)  # Field name made lowercase.
#     comercioexterior_destinatario_domicilio_codigopostal = models.CharField(db_column='COMERCIOEXTERIOR_DESTINATARIO_DOMICILIO_CODIGOPOSTAL', max_length=12, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'FacturaComercioExterior'


# class FacturasEgresosDetalles(models.Model):
#     sysid_factura = models.IntegerField(db_column='SYSID_FACTURA', primary_key=True)  # Field name made lowercase.
#     linea = models.IntegerField(db_column='LINEA')  # Field name made lowercase.
#     egresosysid = models.IntegerField(db_column='EGRESOSYSID', unique=True, blank=True, null=True)  # Field name made lowercase.
#     nocertificadodigital = models.CharField(db_column='NOCERTIFICADODIGITAL', max_length=49, blank=True, null=True)  # Field name made lowercase.
#     versiontimbrado = models.CharField(db_column='VERSIONTIMBRADO', max_length=9, blank=True, null=True)  # Field name made lowercase.
#     uuidtimbrado = models.CharField(db_column='UUIDTIMBRADO', max_length=39, blank=True, null=True)  # Field name made lowercase.
#     rfcprovcertificacion = models.CharField(db_column='RFCPROVCERTIFICACION', max_length=13, blank=True, null=True)  # Field name made lowercase.
#     cadenaoriginalsattimbrado = models.CharField(db_column='CADENAORIGINALSATTIMBRADO', max_length=4999, blank=True, null=True)  # Field name made lowercase.
#     sellocfdtimbrado = models.CharField(db_column='SELLOCFDTIMBRADO', max_length=4999, blank=True, null=True)  # Field name made lowercase.
#     nocertificadosattimbrado = models.CharField(db_column='NOCERTIFICADOSATTIMBRADO', max_length=4999, blank=True, null=True)  # Field name made lowercase.
#     formapago = models.CharField(db_column='FORMAPAGO', max_length=4, blank=True, null=True)  # Field name made lowercase.
#     tipocomprobante = models.CharField(db_column='TIPOCOMPROBANTE', max_length=4, blank=True, null=True)  # Field name made lowercase.
#     sellodigitalemisor = models.CharField(db_column='SELLODIGITALEMISOR', max_length=4999, blank=True, null=True)  # Field name made lowercase.
#     fechayhoratimbrado = models.CharField(db_column='FECHAYHORATIMBRADO', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     saldo = models.DecimalField(db_column='SALDO', max_digits=19, decimal_places=5, blank=True, null=True)  # Field name made lowercase.
#     estatus = models.CharField(db_column='ESTATUS', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     iva = models.DecimalField(db_column='IVA', max_digits=19, decimal_places=5, blank=True, null=True)  # Field name made lowercase.
#     ivaretenido = models.DecimalField(db_column='IVARETENIDO', max_digits=19, decimal_places=5, blank=True, null=True)  # Field name made lowercase.
#     isr = models.DecimalField(db_column='ISR', max_digits=19, decimal_places=5, blank=True, null=True)  # Field name made lowercase.
#     ivaporcentaje = models.DecimalField(db_column='IVAPORCENTAJE', max_digits=19, decimal_places=5, blank=True, null=True)  # Field name made lowercase.
#     isrporcentaje = models.DecimalField(db_column='ISRPORCENTAJE', max_digits=19, decimal_places=5, blank=True, null=True)  # Field name made lowercase.
#     tipofactor = models.CharField(db_column='TIPOFACTOR', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     importe = models.DecimalField(db_column='IMPORTE', max_digits=19, decimal_places=5, blank=True, null=True)  # Field name made lowercase.
#     unidadmedidaclave = models.CharField(db_column='UNIDADMEDIDACLAVE', max_length=4, blank=True, null=True)  # Field name made lowercase.
#     productoclave = models.CharField(db_column='PRODUCTOCLAVE', max_length=9, blank=True, null=True)  # Field name made lowercase.
#     cantidad = models.DecimalField(db_column='CANTIDAD', max_digits=7, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     descripcion = models.CharField(db_column='DESCRIPCION', max_length=199, blank=True, null=True)  # Field name made lowercase.
#     valorunitario = models.DecimalField(db_column='VALORUNITARIO', max_digits=19, decimal_places=5, blank=True, null=True)  # Field name made lowercase.
#     cadenaoriginalemisor = models.CharField(db_column='CADENAORIGINALEMISOR', max_length=4999, blank=True, null=True)  # Field name made lowercase.
#     subtotal = models.DecimalField(db_column='SUBTOTAL', max_digits=19, decimal_places=5, blank=True, null=True)  # Field name made lowercase.
#     total = models.DecimalField(db_column='TOTAL', max_digits=19, decimal_places=5, blank=True, null=True)  # Field name made lowercase.
#     sellosat = models.CharField(db_column='SELLOSAT', max_length=4999, blank=True, null=True)  # Field name made lowercase.
#     fechayhoraemision = models.CharField(db_column='FECHAYHORAEMISION', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     tiporelacion = models.CharField(db_column='TIPORELACION', max_length=4, blank=True, null=True)  # Field name made lowercase.
#     ivaretenidoporcentaje = models.DecimalField(db_column='IVARETENIDOPORCENTAJE', max_digits=19, decimal_places=5, blank=True, null=True)  # Field name made lowercase.
#     fechaclarion = models.IntegerField(db_column='FECHACLARION', blank=True, null=True)  # Field name made lowercase.
#     cancelstatus_cfdi33 = models.CharField(db_column='CANCELSTATUS_CFDI33', max_length=99, blank=True, null=True)  # Field name made lowercase.
#     iscancelable_cfdi33 = models.CharField(db_column='ISCANCELABLE_CFDI33', max_length=99, blank=True, null=True)  # Field name made lowercase.
#     folio = models.CharField(db_column='FOLIO', max_length=19, blank=True, null=True)  # Field name made lowercase.
#     usocfdi = models.CharField(db_column='USOCFDI', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     motivo_cancelacion = models.CharField(db_column='MOTIVO_CANCELACION', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     folio_cancelacion = models.CharField(db_column='FOLIO_CANCELACION', max_length=99, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'Facturas_Egresos_Detalles'
#         unique_together = (('sysid_factura', 'linea'),)





# class Gempresa(models.Model):
#     consecutivo = models.IntegerField(db_column='CONSECUTIVO', primary_key=True)  # Field name made lowercase.
#     nombre = models.CharField(db_column='NOMBRE', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     rfc = models.CharField(db_column='RFC', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     calles = models.CharField(db_column='CALLES', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     callesind = models.CharField(db_column='CALLESIND', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     numext = models.CharField(db_column='NUMEXT', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     numextind = models.CharField(db_column='NUMEXTIND', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     codigopostal = models.CharField(db_column='CODIGOPOSTAL', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     codigopostalind = models.CharField(db_column='CODIGOPOSTALIND', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     colonia = models.CharField(db_column='COLONIA', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     coloniaind = models.CharField(db_column='COLONIAIND', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     ciudad = models.CharField(db_column='CIUDAD', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     ciudadind = models.CharField(db_column='CIUDADIND', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     estado = models.CharField(db_column='ESTADO', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     estadoind = models.CharField(db_column='ESTADOIND', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     telefono = models.CharField(db_column='TELEFONO', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     telefonoind = models.CharField(db_column='TELEFONOIND', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     numfax = models.CharField(db_column='NUMFAX', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     numfaxind = models.CharField(db_column='NUMFAXIND', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     email = models.CharField(db_column='EMAIL', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     emailind = models.CharField(db_column='EMAILIND', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     actpreponderante = models.CharField(db_column='ACTPREPONDERANTE', max_length=80, blank=True, null=True)  # Field name made lowercase.
#     programa = models.CharField(db_column='PROGRAMA', max_length=7, blank=True, null=True)  # Field name made lowercase.
#     numeroprograma = models.CharField(db_column='NUMEROPROGRAMA', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     prosec = models.SmallIntegerField(db_column='PROSEC', blank=True, null=True)  # Field name made lowercase.
#     autorizacionprosec = models.CharField(db_column='AUTORIZACIONPROSEC', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     sector1 = models.CharField(db_column='SECTOR1', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     sector2 = models.CharField(db_column='SECTOR2', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     sector3 = models.CharField(db_column='SECTOR3', max_length=5, blank=True, null=True)  # Field name made lowercase.
#     manufacterid = models.CharField(db_column='MANUFACTERID', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     broker = models.CharField(db_column='BROKER', max_length=6, blank=True, null=True)  # Field name made lowercase.
#     responsable = models.CharField(db_column='RESPONSABLE', max_length=80, blank=True, null=True)  # Field name made lowercase.
#     rfcresponsable = models.CharField(db_column='RFCRESPONSABLE', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     resppaterno = models.CharField(db_column='RESPPATERNO', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     respmaterno = models.CharField(db_column='RESPMATERNO', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     respnombre = models.CharField(db_column='RESPNOMBRE', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     puesto = models.CharField(db_column='PUESTO', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     logo = models.CharField(db_column='LOGO', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     actetiquetas = models.SmallIntegerField(db_column='ACTETIQUETAS', blank=True, null=True)  # Field name made lowercase.
#     claveftp = models.CharField(db_column='CLAVEFTP', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     actfracciones = models.SmallIntegerField(db_column='ACTFRACCIONES', blank=True, null=True)  # Field name made lowercase.
#     rutasifra = models.CharField(db_column='RUTASIFRA', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     bufeteinternacional = models.SmallIntegerField(db_column='BUFETEINTERNACIONAL', blank=True, null=True)  # Field name made lowercase.
#     tipoversion = models.CharField(db_column='TIPOVERSION', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     esempresacertificada = models.CharField(db_column='ESEMPRESACERTIFICADA', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     registroempcert = models.CharField(db_column='REGISTROEMPCERT', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     fechainicialempcert = models.IntegerField(db_column='FECHAINICIALEMPCERT', blank=True, null=True)  # Field name made lowercase.
#     fechafinalempcert = models.IntegerField(db_column='FECHAFINALEMPCERT', blank=True, null=True)  # Field name made lowercase.
#     tienelineaexpress = models.CharField(db_column='TIENELINEAEXPRESS', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     tipoformatoped = models.CharField(db_column='TIPOFORMATOPED', max_length=19, blank=True, null=True)  # Field name made lowercase.
#     codigoanterior = models.SmallIntegerField(db_column='CODIGOANTERIOR', blank=True, null=True)  # Field name made lowercase.
#     activacaat = models.SmallIntegerField(db_column='ACTIVACAAT', blank=True, null=True)  # Field name made lowercase.
#     interfasetrans = models.SmallIntegerField(db_column='INTERFASETRANS', blank=True, null=True)  # Field name made lowercase.
#     costosamericanos = models.SmallIntegerField(db_column='COSTOSAMERICANOS', blank=True, null=True)  # Field name made lowercase.
#     scafsololectura = models.SmallIntegerField(db_column='SCAFSOLOLECTURA', blank=True, null=True)  # Field name made lowercase.
#     esempresaservicio = models.CharField(db_column='ESEMPRESASERVICIO', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     sustpartes = models.SmallIntegerField(db_column='SUSTPARTES', blank=True, null=True)  # Field name made lowercase.
#     nombrecliente = models.CharField(db_column='NOMBRECLIENTE', max_length=300, blank=True, null=True)  # Field name made lowercase.
#     actfacmexame = models.SmallIntegerField(db_column='ACTFACMEXAME', blank=True, null=True)  # Field name made lowercase.
#     partereferencia = models.SmallIntegerField(db_column='PARTEREFERENCIA', blank=True, null=True)  # Field name made lowercase.
#     sqllenguaje = models.CharField(db_column='SQLLENGUAJE', max_length=19, blank=True, null=True)  # Field name made lowercase.
#     modosubmaquila = models.CharField(db_column='MODOSUBMAQUILA', max_length=7, blank=True, null=True)  # Field name made lowercase.
#     modooperacionsaldo = models.CharField(db_column='MODOOPERACIONSALDO', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     curp = models.CharField(db_column='CURP', max_length=19, blank=True, null=True)  # Field name made lowercase.
#     rutaarchcer = models.CharField(db_column='RUTAARCHCER', max_length=1499, blank=True, null=True)  # Field name made lowercase.
#     rutaarchkey = models.CharField(db_column='RUTAARCHKEY', max_length=1499, blank=True, null=True)  # Field name made lowercase.
#     claveaccesofiel = models.CharField(db_column='CLAVEACCESOFIEL', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     usuariowebservicevu = models.CharField(db_column='USUARIOWEBSERVICEVU', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     claveaccesowebservicevu = models.CharField(db_column='CLAVEACCESOWEBSERVICEVU', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     emailvu = models.CharField(db_column='EMAILVU', max_length=800, blank=True, null=True)  # Field name made lowercase.
#     nombrebdinter = models.CharField(db_column='NOMBREBDINTER', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     tipofiguravu = models.CharField(db_column='TIPOFIGURAVU', max_length=29, blank=True, null=True)  # Field name made lowercase.
#     rutavucentral = models.CharField(db_column='RUTAVUCENTRAL', max_length=1499, blank=True, null=True)  # Field name made lowercase.
#     rutaarchivosxml = models.CharField(db_column='RUTAARCHIVOSXML', max_length=1499, blank=True, null=True)  # Field name made lowercase.
#     rfcconsulta = models.CharField(db_column='RFCCONSULTA', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     tomaconfiguracionvu = models.CharField(db_column='TOMACONFIGURACIONVU', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     vuunidadesmedida = models.CharField(db_column='VUUNIDADESMEDIDA', max_length=3, blank=True, null=True)  # Field name made lowercase.
#     rfcvalidacionvu = models.CharField(db_column='RFCVALIDACIONVU', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     ctpat_svi = models.CharField(db_column='CTPAT_SVI', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     fechacertificacionanexo31 = models.IntegerField(db_column='FECHACERTIFICACIONANEXO31', blank=True, null=True)  # Field name made lowercase.
#     numerocertificacionanexo31 = models.CharField(db_column='NUMEROCERTIFICACIONANEXO31', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     modalidadanexo31 = models.CharField(db_column='MODALIDADANEXO31', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     tipoempresaanexo31 = models.CharField(db_column='TIPOEMPRESAANEXO31', max_length=50, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'GEmpresa'





# class AuthGroup(models.Model):
#     name = models.CharField(unique=True, max_length=80)

#     class Meta:
#         managed = False
#         db_table = 'auth_group'


# class AuthGroupPermissions(models.Model):
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#     permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_group_permissions'
#         unique_together = (('group', 'permission'),)


# class AuthPermission(models.Model):
#     name = models.CharField(max_length=255)
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
#     codename = models.CharField(max_length=100)

#     class Meta:
#         managed = False
#         db_table = 'auth_permission'
#         unique_together = (('content_type', 'codename'),)


# class AuthUser(models.Model):
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.BooleanField()
#     username = models.CharField(max_length=150)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     email = models.CharField(max_length=254)
#     is_staff = models.BooleanField()
#     is_active = models.BooleanField()
#     date_joined = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'auth_user'


# class AuthUserGroups(models.Model):
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_user_groups'
#         unique_together = (('user', 'group'),)


# class AuthUserUserPermissions(models.Model):
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_user_user_permissions'
#         unique_together = (('user', 'permission'),)


# class Bancos(models.Model):
#     clave = models.CharField(db_column='CLAVE', primary_key=True, max_length=10)  # Field name made lowercase.
#     nombre = models.CharField(db_column='NOMBRE', max_length=199, blank=True, null=True)  # Field name made lowercase.
#     paginaweb = models.CharField(db_column='PAGINAWEB', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     ic_cuentapesos = models.CharField(db_column='IC_CUENTAPESOS', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     ic_cuentadolares = models.CharField(db_column='IC_CUENTADOLARES', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     ic_polizaingresosdolares = models.CharField(db_column='IC_POLIZAINGRESOSDOLARES', max_length=3, blank=True, null=True)  # Field name made lowercase.
#     ic_polizaingresospesos = models.CharField(db_column='IC_POLIZAINGRESOSPESOS', max_length=3, blank=True, null=True)  # Field name made lowercase.
#     ic_polizaegresospesoscheques = models.CharField(db_column='IC_POLIZAEGRESOSPESOSCHEQUES', max_length=3, blank=True, null=True)  # Field name made lowercase.
#     ic_polizaegresosdolarescheuqes = models.CharField(db_column='IC_POLIZAEGRESOSDOLARESCHEUQES', max_length=3, blank=True, null=True)  # Field name made lowercase.
#     ic_polizaegresospesostransferencia = models.CharField(db_column='IC_POLIZAEGRESOSPESOSTRANSFERENCIA', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     ic_polizaegresosdolarestransferencia = models.CharField(db_column='IC_POLIZAEGRESOSDOLARESTRANSFERENCIA', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     ic_clavepesos = models.CharField(db_column='IC_CLAVEPESOS', max_length=5, blank=True, null=True)  # Field name made lowercase.
#     ic_clavedolares = models.CharField(db_column='IC_CLAVEDOLARES', max_length=5, blank=True, null=True)  # Field name made lowercase.
#     rfc = models.CharField(db_column='RFC', unique=True, max_length=14, blank=True, null=True)  # Field name made lowercase.
#     cuentabancariacfdi33 = models.CharField(db_column='CUENTABANCARIACFDI33', max_length=18, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'bancos'

# class Cliente(models.Model):
#     clave = models.CharField(db_column='CLAVE', primary_key=True, max_length=14)  # Field name made lowercase.
#     cliente = models.CharField(db_column='CLIENTE', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     ciudad = models.CharField(db_column='CIUDAD', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     estado = models.CharField(db_column='ESTADO', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     pais = models.CharField(db_column='PAIS', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     direccion = models.CharField(db_column='DIRECCION', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     lada = models.CharField(db_column='LADA', max_length=6, blank=True, null=True)  # Field name made lowercase.
#     tel1 = models.CharField(db_column='TEL1', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     tel2 = models.CharField(db_column='TEL2', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     fax = models.CharField(db_column='FAX', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     contacto = models.CharField(db_column='CONTACTO', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     puesto = models.CharField(db_column='PUESTO', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     teldirecto = models.CharField(db_column='TELDIRECTO', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     ext = models.CharField(db_column='EXT', max_length=6, blank=True, null=True)  # Field name made lowercase.
#     horario = models.CharField(db_column='HORARIO', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     observacion = models.CharField(db_column='OBSERVACION', max_length=1000, blank=True, null=True)  # Field name made lowercase.
#     email = models.CharField(db_column='EMAIL', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     tipoticket = models.CharField(db_column='TIPOTICKET', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     servicio = models.CharField(db_column='SERVICIO', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     advertencia = models.CharField(db_column='ADVERTENCIA', max_length=2000, blank=True, null=True)  # Field name made lowercase.
#     costohora = models.DecimalField(db_column='COSTOHORA', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     moneda = models.CharField(db_column='MONEDA', max_length=8, blank=True, null=True)  # Field name made lowercase.
#     tipocliente = models.CharField(db_column='TIPOCLIENTE', max_length=59, blank=True, null=True)  # Field name made lowercase.
#     responsable = models.CharField(db_column='RESPONSABLE', max_length=6, blank=True, null=True)  # Field name made lowercase.
#     categoria = models.CharField(db_column='CATEGORIA', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     rfc = models.CharField(db_column='RFC', max_length=18, blank=True, null=True)  # Field name made lowercase.
#     cp = models.CharField(db_column='CP', max_length=14, blank=True, null=True)  # Field name made lowercase.
#     pagina = models.CharField(db_column='PAGINA', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     activaradvertencia = models.SmallIntegerField(db_column='ACTIVARADVERTENCIA', blank=True, null=True)  # Field name made lowercase.
#     medio = models.CharField(db_column='MEDIO', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     fecharegistro = models.IntegerField(db_column='FECHAREGISTRO', blank=True, null=True)  # Field name made lowercase.
#     colonia = models.CharField(db_column='COLONIA', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     problemacliente = models.CharField(db_column='PROBLEMACLIENTE', max_length=1000, blank=True, null=True)  # Field name made lowercase.
#     causaproblemasolucion = models.CharField(db_column='CAUSAPROBLEMASOLUCION', max_length=1000, blank=True, null=True)  # Field name made lowercase.
#     diafactura = models.CharField(db_column='DIAFACTURA', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     prospecto = models.SmallIntegerField(db_column='PROSPECTO', blank=True, null=True)  # Field name made lowercase.
#     vende = models.CharField(db_column='VENDE', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     descripcion = models.CharField(db_column='DESCRIPCION', max_length=1500, blank=True, null=True)  # Field name made lowercase.
#     competencia = models.CharField(db_column='COMPETENCIA', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     analisismercado = models.CharField(db_column='ANALISISMERCADO', max_length=1000, blank=True, null=True)  # Field name made lowercase.
#     finanzas = models.CharField(db_column='FINANZAS', max_length=1000, blank=True, null=True)  # Field name made lowercase.
#     capacidadpotencial = models.CharField(db_column='CAPACIDADPOTENCIAL', max_length=1000, blank=True, null=True)  # Field name made lowercase.
#     o_identificacionoficial = models.CharField(db_column='O_IDENTIFICACIONOFICIAL', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     o_ruta = models.CharField(db_column='O_RUTA', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     o_nombre_conyuge = models.CharField(db_column='O_NOMBRE_CONYUGE', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     o_direccion_conyuge = models.CharField(db_column='O_DIRECCION_CONYUGE', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     o_colonia_conyuge = models.CharField(db_column='O_COLONIA_CONYUGE', max_length=60, blank=True, null=True)  # Field name made lowercase.
#     o_codigo_postal_conyuge = models.CharField(db_column='O_CODIGO_POSTAL_CONYUGE', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     o_telefono_conyuge = models.CharField(db_column='O_TELEFONO_CONYUGE', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     puesto_actividadlaboral = models.CharField(db_column='PUESTO_ACTIVIDADLABORAL', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     antiguedad_actividadlaboral = models.IntegerField(db_column='ANTIGUEDAD_ACTIVIDADLABORAL', blank=True, null=True)  # Field name made lowercase.
#     sueldomencomp_actividadlaboral = models.DecimalField(db_column='SUELDOMENCOMP_ACTIVIDADLABORAL', max_digits=9, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     nombreempresa_actividadlaboral = models.CharField(db_column='NOMBREEMPRESA_ACTIVIDADLABORAL', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     domicioempresa_actividadlaboral = models.CharField(db_column='DOMICIOEMPRESA_ACTIVIDADLABORAL', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     colonia_actividadlaboral = models.CharField(db_column='COLONIA_ACTIVIDADLABORAL', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     otrosingresos_actividadlaboral = models.CharField(db_column='OTROSINGRESOS_ACTIVIDADLABORAL', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     telefono_actividadlaboral = models.CharField(db_column='TELEFONO_ACTIVIDADLABORAL', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     cp_actividadlaboral = models.CharField(db_column='CP_ACTIVIDADLABORAL', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     ext_actividadlaboral = models.CharField(db_column='EXT_ACTIVIDADLABORAL', max_length=5, blank=True, null=True)  # Field name made lowercase.
#     cel_actividadlaboral = models.CharField(db_column='CEL_ACTIVIDADLABORAL', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     paginaweb_actividadlaboral = models.CharField(db_column='PAGINAWEB_ACTIVIDADLABORAL', max_length=52, blank=True, null=True)  # Field name made lowercase.
#     o_empresa_conyuge = models.CharField(db_column='O_EMPRESA_CONYUGE', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     o_puesto_conyuge = models.CharField(db_column='O_PUESTO_CONYUGE', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     o_cel_conyuge = models.CharField(db_column='O_CEL_CONYUGE', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     o_email_conyuge = models.CharField(db_column='O_EMAIL_CONYUGE', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     o_antiguedad_conyuge = models.IntegerField(db_column='O_ANTIGUEDAD_CONYUGE', blank=True, null=True)  # Field name made lowercase.
#     o_sueldo_conyuge = models.DecimalField(db_column='O_SUELDO_CONYUGE', max_digits=11, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     o_estadocivil = models.CharField(db_column='O_ESTADOCIVIL', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     o_fechanacimiento = models.IntegerField(db_column='O_FECHANACIMIENTO', blank=True, null=True)  # Field name made lowercase.
#     o_dom_realizartrabajo = models.CharField(db_column='O_DOM_REALIZARTRABAJO', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     o_coloniarealizartrabajo = models.CharField(db_column='O_COLONIAREALIZARTRABAJO', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     o_telefonorealizartrabajo = models.CharField(db_column='O_TELEFONOREALIZARTRABAJO', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     o_codigopostalrealizartrabajo = models.CharField(db_column='O_CODIGOPOSTALREALIZARTRABAJO', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     o_mismodatos = models.SmallIntegerField(db_column='O_MISMODATOS', blank=True, null=True)  # Field name made lowercase.
#     nombrefiscal = models.CharField(db_column='NOMBREFISCAL', max_length=250, blank=True, null=True)  # Field name made lowercase.
#     domiciliofiscal = models.CharField(db_column='DOMICILIOFISCAL', max_length=250, blank=True, null=True)  # Field name made lowercase.
#     rfcfiscal = models.CharField(db_column='RFCFISCAL', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     ciudadfiscal = models.CharField(db_column='CIUDADFISCAL', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     estadofiscal = models.CharField(db_column='ESTADOFISCAL', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     paisfiscal = models.CharField(db_column='PAISFISCAL', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     cpfiscal = models.CharField(db_column='CPFISCAL', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     contactofacturacion = models.CharField(db_column='CONTACTOFACTURACION', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     fecharecepcionfacturas = models.IntegerField(db_column='FECHARECEPCIONFACTURAS', blank=True, null=True)  # Field name made lowercase.
#     fechapagofacturas = models.IntegerField(db_column='FECHAPAGOFACTURAS', blank=True, null=True)  # Field name made lowercase.
#     coloniafiscal = models.CharField(db_column='COLONIAFISCAL', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     formapago_facturacion = models.CharField(db_column='FORMAPAGO_FACTURACION', max_length=49, blank=True, null=True)  # Field name made lowercase.
#     ic_cuentacliente = models.CharField(db_column='IC_CUENTACLIENTE', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     ic_cuentaventas = models.CharField(db_column='IC_CUENTAVENTAS', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     ic_cuentamantenimiento = models.CharField(db_column='IC_CUENTAMANTENIMIENTO', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     ic_cuentaotrosgastos = models.CharField(db_column='IC_CUENTAOTROSGASTOS', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     ic_cuentaventasbufete = models.CharField(db_column='IC_CUENTAVENTASBUFETE', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     formatofactura = models.CharField(db_column='FORMATOFACTURA', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     numeroext = models.CharField(db_column='NUMEROEXT', max_length=19, blank=True, null=True)  # Field name made lowercase.
#     regimenaplicado = models.CharField(db_column='REGIMENAPLICADO', max_length=99, blank=True, null=True)  # Field name made lowercase.
#     tiporregimenfiscal = models.CharField(db_column='TIPORREGIMENFISCAL', max_length=19, blank=True, null=True)  # Field name made lowercase.
#     numctapago = models.CharField(db_column='NUMCTAPAGO', max_length=4, blank=True, null=True)  # Field name made lowercase.
#     nointerior = models.TextField(db_column='NOINTERIOR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     emailfactelect = models.CharField(db_column='EMAILFACTELECT', max_length=149, blank=True, null=True)  # Field name made lowercase.
#     clienteactivo = models.SmallIntegerField(db_column='CLIENTEACTIVO', blank=True, null=True)  # Field name made lowercase.
#     clienteinactivo = models.SmallIntegerField(db_column='CLIENTEINACTIVO', blank=True, null=True)  # Field name made lowercase.
#     nacionalidad = models.CharField(db_column='NACIONALIDAD', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     numregfiex = models.CharField(db_column='NUMREGFIEX', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     curp_fac = models.CharField(db_column='CURP_FAC', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     notas = models.CharField(db_column='NOTAS', max_length=254, blank=True, null=True)  # Field name made lowercase.
#     cfdi33_receptor_usocfdi = models.CharField(db_column='CFDI33_RECEPTOR_USOCFDI', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     cfdi33_receptor_usocfdidescripcion = models.CharField(db_column='CFDI33_RECEPTOR_USOCFDIDESCRIPCION', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     cfdi33_residencia_fiscal = models.CharField(db_column='CFDI33_RESIDENCIA_FISCAL', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     cfdi33_residenciafiscaldescripcion = models.CharField(db_column='CFDI33_RESIDENCIAFISCALDESCRIPCION', max_length=249, blank=True, null=True)  # Field name made lowercase.
#     cfdi33_numregidtrib = models.CharField(db_column='CFDI33_NUMREGIDTRIB', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     cfdi33_metododepago = models.CharField(db_column='CFDI33_METODODEPAGO', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     cfdi33_metododepagodescripcion = models.CharField(db_column='CFDI33_METODODEPAGODESCRIPCION', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     cfdi33_regimenfiscal = models.CharField(db_column='CFDI33_REGIMENFISCAL', max_length=3, blank=True, null=True)  # Field name made lowercase.
#     cfdi33_domiciliofiscal = models.CharField(db_column='CFDI33_DOMICILIOFISCAL', max_length=10, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'cliente'

# class Configuracion(models.Model):
#     consecutivo = models.IntegerField(db_column='CONSECUTIVO', primary_key=True)  # Field name made lowercase.
#     nombreempresa = models.CharField(db_column='NOMBREEMPRESA', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     rutabd = models.CharField(db_column='RUTABD', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     pathrespaldo = models.CharField(db_column='PATHRESPALDO', max_length=1001, blank=True, null=True)  # Field name made lowercase.
#     emailto = models.CharField(db_column='EMAILTO', max_length=1000, blank=True, null=True)  # Field name made lowercase.
#     emailfrom = models.CharField(db_column='EMAILFROM', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     emailsubject = models.CharField(db_column='EMAILSUBJECT', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     emailtext = models.CharField(db_column='EMAILTEXT', max_length=2000, blank=True, null=True)  # Field name made lowercase.
#     smtserver = models.CharField(db_column='SMTSERVER', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     logotipo = models.CharField(db_column='LOGOTIPO', max_length=300, blank=True, null=True)  # Field name made lowercase.
#     ponerlogo = models.SmallIntegerField(db_column='PONERLOGO', blank=True, null=True)  # Field name made lowercase.
#     enviarticket1 = models.SmallIntegerField(db_column='ENVIARTICKET1', blank=True, null=True)  # Field name made lowercase.
#     email1 = models.CharField(db_column='EMAIL1', max_length=1000, blank=True, null=True)  # Field name made lowercase.
#     pregunar1 = models.SmallIntegerField(db_column='PREGUNAR1', blank=True, null=True)  # Field name made lowercase.
#     enviarticket2 = models.SmallIntegerField(db_column='ENVIARTICKET2', blank=True, null=True)  # Field name made lowercase.
#     email2 = models.CharField(db_column='EMAIL2', max_length=1000, blank=True, null=True)  # Field name made lowercase.
#     pregunar2 = models.SmallIntegerField(db_column='PREGUNAR2', blank=True, null=True)  # Field name made lowercase.
#     enviarticket3 = models.SmallIntegerField(db_column='ENVIARTICKET3', blank=True, null=True)  # Field name made lowercase.
#     email3 = models.CharField(db_column='EMAIL3', max_length=1000, blank=True, null=True)  # Field name made lowercase.
#     pregunar3 = models.SmallIntegerField(db_column='PREGUNAR3', blank=True, null=True)  # Field name made lowercase.
#     informarhorasds = models.SmallIntegerField(db_column='INFORMARHORASDS', blank=True, null=True)  # Field name made lowercase.
#     claveclientelocal = models.CharField(db_column='CLAVECLIENTELOCAL', max_length=9, blank=True, null=True)  # Field name made lowercase.
#     logologin = models.CharField(db_column='LOGOLOGIN', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     preguntarfaqs = models.SmallIntegerField(db_column='PREGUNTARFAQS', blank=True, null=True)  # Field name made lowercase.
#     direccion = models.CharField(db_column='DIRECCION', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     telefonos = models.CharField(db_column='TELEFONOS', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     email = models.CharField(db_column='EMAIL', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     moneda = models.CharField(db_column='MONEDA', max_length=7, blank=True, null=True)  # Field name made lowercase.
#     cotizaciones = models.SmallIntegerField(db_column='COTIZACIONES', blank=True, null=True)  # Field name made lowercase.
#     fechalastversion = models.IntegerField(db_column='FECHALASTVERSION', blank=True, null=True)  # Field name made lowercase.
#     horalastversion = models.IntegerField(db_column='HORALASTVERSION', blank=True, null=True)  # Field name made lowercase.
#     tipocambio = models.SmallIntegerField(db_column='TIPOCAMBIO', blank=True, null=True)  # Field name made lowercase.
#     ciudad = models.CharField(db_column='CIUDAD', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     estado = models.CharField(db_column='ESTADO', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     notacotizacion = models.CharField(db_column='NOTACOTIZACION', max_length=1000, blank=True, null=True)  # Field name made lowercase.
#     enbezadocotizacion = models.CharField(db_column='ENBEZADOCOTIZACION', max_length=1000, blank=True, null=True)  # Field name made lowercase.
#     claveitem = models.SmallIntegerField(db_column='CLAVEITEM', blank=True, null=True)  # Field name made lowercase.
#     cotizacionxpos = models.IntegerField(db_column='COTIZACIONXPOS', blank=True, null=True)  # Field name made lowercase.
#     cotizacionypos = models.IntegerField(db_column='COTIZACIONYPOS', blank=True, null=True)  # Field name made lowercase.
#     cotizacionancho = models.IntegerField(db_column='COTIZACIONANCHO', blank=True, null=True)  # Field name made lowercase.
#     cotizacionlargo = models.IntegerField(db_column='COTIZACIONLARGO', blank=True, null=True)  # Field name made lowercase.
#     codigopostal = models.CharField(db_column='CODIGOPOSTAL', max_length=14, blank=True, null=True)  # Field name made lowercase.
#     siguientereferencia = models.IntegerField(db_column='SIGUIENTEREFERENCIA', blank=True, null=True)  # Field name made lowercase.
#     autonumerarreferencia = models.SmallIntegerField(db_column='AUTONUMERARREFERENCIA', blank=True, null=True)  # Field name made lowercase.
#     logo_posx = models.IntegerField(db_column='LOGO_POSX', blank=True, null=True)  # Field name made lowercase.
#     logo_posy = models.IntegerField(db_column='LOGO_POSY', blank=True, null=True)  # Field name made lowercase.
#     logo_ancho = models.IntegerField(db_column='LOGO_ANCHO', blank=True, null=True)  # Field name made lowercase.
#     logo_largo = models.IntegerField(db_column='LOGO_LARGO', blank=True, null=True)  # Field name made lowercase.
#     reqfvencimientoticket = models.SmallIntegerField(db_column='REQFVENCIMIENTOTICKET', blank=True, null=True)  # Field name made lowercase.
#     tiempoestimadorealticket = models.SmallIntegerField(db_column='TIEMPOESTIMADOREALTICKET', blank=True, null=True)  # Field name made lowercase.
#     rutaservidor = models.TextField(db_column='RUTASERVIDOR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     formatofactura = models.CharField(db_column='FORMATOFACTURA', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     activarescalamientocliente = models.SmallIntegerField(db_column='ACTIVARESCALAMIENTOCLIENTE', blank=True, null=True)  # Field name made lowercase.
#     escalamientoticket = models.CharField(db_column='ESCALAMIENTOTICKET', max_length=1000, blank=True, null=True)  # Field name made lowercase.
#     escalamientobitacora = models.CharField(db_column='ESCALAMIENTOBITACORA', max_length=1000, blank=True, null=True)  # Field name made lowercase.
#     direccionpagina = models.CharField(db_column='DIRECCIONPAGINA', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     actesccierreadmin = models.SmallIntegerField(db_column='ACTESCCIERREADMIN', blank=True, null=True)  # Field name made lowercase.
#     msgclientecierreadmin = models.CharField(db_column='MSGCLIENTECIERREADMIN', max_length=1000, blank=True, null=True)  # Field name made lowercase.
#     porutilminbruta = models.DecimalField(db_column='PORUTILMINBRUTA', max_digits=7, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     noeditartiemporeal = models.SmallIntegerField(db_column='NOEDITARTIEMPOREAL', blank=True, null=True)  # Field name made lowercase.
#     diasregistrarbitacora = models.IntegerField(db_column='DIASREGISTRARBITACORA', blank=True, null=True)  # Field name made lowercase.
#     permitirfechacalculada = models.SmallIntegerField(db_column='PERMITIRFECHACALCULADA', blank=True, null=True)  # Field name made lowercase.
#     fechacalculada = models.IntegerField(db_column='FECHACALCULADA', blank=True, null=True)  # Field name made lowercase.
#     fechacalculadapc = models.CharField(db_column='FECHACALCULADAPC', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     tipofecharegistroactividades = models.SmallIntegerField(db_column='TIPOFECHAREGISTROACTIVIDADES', blank=True, null=True)  # Field name made lowercase.
#     colonia = models.CharField(db_column='COLONIA', max_length=80, blank=True, null=True)  # Field name made lowercase.
#     fax = models.CharField(db_column='FAX', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     web = models.CharField(db_column='WEB', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     cartarepcotizaciones = models.TextField(db_column='CARTAREPCOTIZACIONES', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     permitirfacturacionconsecutiva = models.SmallIntegerField(db_column='PERMITIRFACTURACIONCONSECUTIVA', blank=True, null=True)  # Field name made lowercase.
#     notacotizacioningles = models.CharField(db_column='NOTACOTIZACIONINGLES', max_length=1000, blank=True, null=True)  # Field name made lowercase.
#     cartarepcotizacioningles = models.CharField(db_column='CARTAREPCOTIZACIONINGLES', max_length=1000, blank=True, null=True)  # Field name made lowercase.
#     encabezadocotizacioningles = models.CharField(db_column='ENCABEZADOCOTIZACIONINGLES', max_length=1000, blank=True, null=True)  # Field name made lowercase.
#     diasvencimientoprospect = models.IntegerField(db_column='DIASVENCIMIENTOPROSPECT', blank=True, null=True)  # Field name made lowercase.
#     activarcomisiones = models.SmallIntegerField(db_column='ACTIVARCOMISIONES', blank=True, null=True)  # Field name made lowercase.
#     ivafacturacion = models.DecimalField(db_column='IVAFACTURACION', max_digits=9, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     ivacotizacion = models.DecimalField(db_column='IVACOTIZACION', max_digits=11, decimal_places=7, blank=True, null=True)  # Field name made lowercase.
#     retencionflete = models.DecimalField(db_column='RETENCIONFLETE', max_digits=9, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     imprimirlogos = models.SmallIntegerField(db_column='IMPRIMIRLOGOS', blank=True, null=True)  # Field name made lowercase.
#     pmcantidadcontactos = models.IntegerField(db_column='PMCANTIDADCONTACTOS', blank=True, null=True)  # Field name made lowercase.
#     pmcantidadoportunidades = models.IntegerField(db_column='PMCANTIDADOPORTUNIDADES', blank=True, null=True)  # Field name made lowercase.
#     pmcantidadcotizacionesgan = models.IntegerField(db_column='PMCANTIDADCOTIZACIONESGAN', blank=True, null=True)  # Field name made lowercase.
#     hayretencionfleteenfacturas = models.SmallIntegerField(db_column='HAYRETENCIONFLETEENFACTURAS', blank=True, null=True)  # Field name made lowercase.
#     ivacxp = models.DecimalField(db_column='IVACXP', max_digits=9, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     facturaconsecutivacxp = models.SmallIntegerField(db_column='FACTURACONSECUTIVACXP', blank=True, null=True)  # Field name made lowercase.
#     sufreretencionivacxp = models.SmallIntegerField(db_column='SUFRERETENCIONIVACXP', blank=True, null=True)  # Field name made lowercase.
#     sufreretencionirscxp = models.SmallIntegerField(db_column='SUFRERETENCIONIRSCXP', blank=True, null=True)  # Field name made lowercase.
#     retencionivacxp = models.DecimalField(db_column='RETENCIONIVACXP', max_digits=9, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     retencionisrcxp = models.DecimalField(db_column='RETENCIONISRCXP', max_digits=9, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     aplicaivalosarticulos = models.SmallIntegerField(db_column='APLICAIVALOSARTICULOS', blank=True, null=True)  # Field name made lowercase.
#     mostrarvencidos = models.SmallIntegerField(db_column='MOSTRARVENCIDOS', blank=True, null=True)  # Field name made lowercase.
#     diasvencimientosinformar = models.IntegerField(db_column='DIASVENCIMIENTOSINFORMAR', blank=True, null=True)  # Field name made lowercase.
#     mandarcorreoasuntosvencidos = models.SmallIntegerField(db_column='MANDARCORREOASUNTOSVENCIDOS', blank=True, null=True)  # Field name made lowercase.
#     frecuencia = models.CharField(db_column='FRECUENCIA', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     correoenviadoasuntos = models.SmallIntegerField(db_column='CORREOENVIADOASUNTOS', blank=True, null=True)  # Field name made lowercase.
#     fechaenvio = models.IntegerField(db_column='FECHAENVIO', blank=True, null=True)  # Field name made lowercase.
#     recordarpassword = models.SmallIntegerField(db_column='RECORDARPASSWORD', blank=True, null=True)  # Field name made lowercase.
#     digitosdespuespunto = models.IntegerField(db_column='DIGITOSDESPUESPUNTO', blank=True, null=True)  # Field name made lowercase.
#     permitirremisionesconsecutivas = models.SmallIntegerField(db_column='PERMITIRREMISIONESCONSECUTIVAS', blank=True, null=True)  # Field name made lowercase.
#     ivadefaultremision = models.DecimalField(db_column='IVADEFAULTREMISION', max_digits=9, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     formaturaremision = models.CharField(db_column='FORMATURAREMISION', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     inv_avisarcantidadmaxima = models.SmallIntegerField(db_column='INV_AVISARCANTIDADMAXIMA', blank=True, null=True)  # Field name made lowercase.
#     inv_avisarminimo = models.SmallIntegerField(db_column='INV_AVISARMINIMO', blank=True, null=True)  # Field name made lowercase.
#     inv_salidamercancia = models.CharField(db_column='INV_SALIDAMERCANCIA', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     inv_permitirfacturarsincantidad = models.SmallIntegerField(db_column='INV_PERMITIRFACTURARSINCANTIDAD', blank=True, null=True)  # Field name made lowercase.
#     inv_permitirremisionsincantidad = models.SmallIntegerField(db_column='INV_PERMITIRREMISIONSINCANTIDAD', blank=True, null=True)  # Field name made lowercase.
#     inv_ivadefault = models.DecimalField(db_column='INV_IVADEFAULT', max_digits=9, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     servidorftp = models.CharField(db_column='SERVIDORFTP', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     httpsitio = models.CharField(db_column='HTTPSITIO', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     tipoconexion = models.CharField(db_column='TIPOCONEXION', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     fechaactualizacion = models.IntegerField(db_column='FECHAACTUALIZACION', blank=True, null=True)  # Field name made lowercase.
#     usuarioftp = models.CharField(db_column='USUARIOFTP', max_length=254, blank=True, null=True)  # Field name made lowercase.
#     passwordftp = models.CharField(db_column='PASSWORDFTP', max_length=254, blank=True, null=True)  # Field name made lowercase.
#     metaoportunidad = models.DecimalField(db_column='METAOPORTUNIDAD', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     metacotizacion = models.DecimalField(db_column='METACOTIZACION', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     numeromaxpartidasrem = models.IntegerField(db_column='NUMEROMAXPARTIDASREM', blank=True, null=True)  # Field name made lowercase.
#     numeroremision = models.IntegerField(db_column='NUMEROREMISION', blank=True, null=True)  # Field name made lowercase.
#     numerofactura = models.IntegerField(db_column='NUMEROFACTURA', blank=True, null=True)  # Field name made lowercase.
#     transferencia_binaria = models.SmallIntegerField(db_column='TRANSFERENCIA_BINARIA', blank=True, null=True)  # Field name made lowercase.
#     directorio_ftp = models.CharField(db_column='DIRECTORIO_FTP', max_length=253, blank=True, null=True)  # Field name made lowercase.
#     ic_cuentaiva_fronterizo = models.CharField(db_column='IC_CUENTAIVA_FRONTERIZO', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     ic_cuentaiva_interior = models.CharField(db_column='IC_CUENTAIVA_INTERIOR', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     ic_numeropoliza = models.IntegerField(db_column='IC_NUMEROPOLIZA', blank=True, null=True)  # Field name made lowercase.
#     ic_cp_cuentaiva_fronterizo = models.CharField(db_column='IC_CP_CUENTAIVA_FRONTERIZO', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     ic_cp_cuentaiva_interior = models.CharField(db_column='IC_CP_CUENTAIVA_INTERIOR', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     ic_cp_cuentaiva_interrior_acreditable = models.CharField(db_column='IC_CP_CUENTAIVA_INTERRIOR_ACREDITABLE', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     ic_cp_cuentaiva_fonterizo_acreditable = models.CharField(db_column='IC_CP_CUENTAIVA_FONTERIZO_ACREDITABLE', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     ic_cuentaivapendiente_fronterizo = models.CharField(db_column='IC_CUENTAIVAPENDIENTE_FRONTERIZO', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     ic_cuentaivapendiente_interior = models.CharField(db_column='IC_CUENTAIVAPENDIENTE_INTERIOR', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     variosformatosfactura = models.SmallIntegerField(db_column='VARIOSFORMATOSFACTURA', blank=True, null=True)  # Field name made lowercase.
#     aplicaivaporcobrar = models.SmallIntegerField(db_column='APLICAIVAPORCOBRAR', blank=True, null=True)  # Field name made lowercase.
#     puertosmtp = models.IntegerField(db_column='PUERTOSMTP', blank=True, null=True)  # Field name made lowercase.
#     formatonotcredito = models.CharField(db_column='FORMATONOTCREDITO', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     permitirnotacconsecutiva = models.SmallIntegerField(db_column='PERMITIRNOTACCONSECUTIVA', blank=True, null=True)  # Field name made lowercase.
#     numeronota = models.IntegerField(db_column='NUMERONOTA', blank=True, null=True)  # Field name made lowercase.
#     avisoconvenio = models.SmallIntegerField(db_column='AVISOCONVENIO', blank=True, null=True)  # Field name made lowercase.
#     permitirgastosconsecutivos = models.SmallIntegerField(db_column='PERMITIRGASTOSCONSECUTIVOS', blank=True, null=True)  # Field name made lowercase.
#     ivadefaultgasto = models.DecimalField(db_column='IVADEFAULTGASTO', max_digits=9, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     numeromaxpartidasgasto = models.IntegerField(db_column='NUMEROMAXPARTIDASGASTO', blank=True, null=True)  # Field name made lowercase.
#     numerogasto = models.IntegerField(db_column='NUMEROGASTO', blank=True, null=True)  # Field name made lowercase.
#     formatogastos = models.CharField(db_column='FORMATOGASTOS', max_length=24, blank=True, null=True)  # Field name made lowercase.
#     perconsecutivoelectronico = models.SmallIntegerField(db_column='PERCONSECUTIVOELECTRONICO', blank=True, null=True)  # Field name made lowercase.
#     facdigitalinicio = models.IntegerField(db_column='FACDIGITALINICIO', blank=True, null=True)  # Field name made lowercase.
#     facdigitalfin = models.IntegerField(db_column='FACDIGITALFIN', blank=True, null=True)  # Field name made lowercase.
#     formatodigital = models.CharField(db_column='FORMATODIGITAL', max_length=34, blank=True, null=True)  # Field name made lowercase.
#     nocertificado = models.CharField(db_column='NOCERTIFICADO', max_length=99, blank=True, null=True)  # Field name made lowercase.
#     pathfacturas = models.CharField(db_column='PATHFACTURAS', max_length=249, blank=True, null=True)  # Field name made lowercase.
#     pathapplication = models.CharField(db_column='PATHAPPLICATION', max_length=999, blank=True, null=True)  # Field name made lowercase.
#     serie = models.CharField(db_column='SERIE', max_length=19, blank=True, null=True)  # Field name made lowercase.
#     noaprobacion = models.IntegerField(db_column='NOAPROBACION', blank=True, null=True)  # Field name made lowercase.
#     anoaprobacion = models.IntegerField(db_column='ANOAPROBACION', blank=True, null=True)  # Field name made lowercase.
#     pathfilekey = models.CharField(db_column='PATHFILEKEY', max_length=254, blank=True, null=True)  # Field name made lowercase.
#     pathimgcedulafiscal = models.CharField(db_column='PATHIMGCEDULAFISCAL', max_length=254, blank=True, null=True)  # Field name made lowercase.
#     pathfilecer = models.CharField(db_column='PATHFILECER', max_length=254, blank=True, null=True)  # Field name made lowercase.
#     passwordkeyfile = models.CharField(db_column='PASSWORDKEYFILE', max_length=24, blank=True, null=True)  # Field name made lowercase.
#     consecutivocartaporte = models.DecimalField(db_column='CONSECUTIVOCARTAPORTE', max_digits=9, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
#     diasregistraractividades = models.IntegerField(db_column='DIASREGISTRARACTIVIDADES', blank=True, null=True)  # Field name made lowercase.
#     autentificacion = models.SmallIntegerField(db_column='AUTENTIFICACION', blank=True, null=True)  # Field name made lowercase.
#     emailuser = models.CharField(db_column='EMAILUSER', max_length=59, blank=True, null=True)  # Field name made lowercase.
#     emailpassword = models.CharField(db_column='EMAILPASSWORD', max_length=49, blank=True, null=True)  # Field name made lowercase.
#     webservicepac = models.CharField(db_column='WEBSERVICEPAC', max_length=299, blank=True, null=True)  # Field name made lowercase.
#     webserviceuser = models.CharField(db_column='WEBSERVICEUSER', max_length=59, blank=True, null=True)  # Field name made lowercase.
#     webservicepassword = models.CharField(db_column='WEBSERVICEPASSWORD', max_length=29, blank=True, null=True)  # Field name made lowercase.
#     pathaplicacionpac = models.CharField(db_column='PATHAPLICACIONPAC', max_length=999, blank=True, null=True)  # Field name made lowercase.
#     pathcancelfilepfx = models.CharField(db_column='PATHCANCELFILEPFX', max_length=999, blank=True, null=True)  # Field name made lowercase.
#     pfxpwd = models.CharField(db_column='PFXPWD', max_length=29, blank=True, null=True)  # Field name made lowercase.
#     pathfacturasout = models.CharField(db_column='PATHFACTURASOUT', max_length=999, blank=True, null=True)  # Field name made lowercase.
#     invoicetype = models.CharField(db_column='INVOICETYPE', max_length=29, blank=True, null=True)  # Field name made lowercase.
#     nodecimales = models.IntegerField(db_column='NODECIMALES', blank=True, null=True)  # Field name made lowercase.
#     perconsecutivonotaelectronico = models.SmallIntegerField(db_column='PERCONSECUTIVONOTAELECTRONICO', blank=True, null=True)  # Field name made lowercase.
#     notdigitalinicio = models.IntegerField(db_column='NOTDIGITALINICIO', blank=True, null=True)  # Field name made lowercase.
#     notdigitalfin = models.IntegerField(db_column='NOTDIGITALFIN', blank=True, null=True)  # Field name made lowercase.
#     formatonotdigital = models.CharField(db_column='FORMATONOTDIGITAL', max_length=34, blank=True, null=True)  # Field name made lowercase.
#     nocertificadonot = models.CharField(db_column='NOCERTIFICADONOT', max_length=99, blank=True, null=True)  # Field name made lowercase.
#     serienot = models.CharField(db_column='SERIENOT', max_length=19, blank=True, null=True)  # Field name made lowercase.
#     noaprobacionnot = models.IntegerField(db_column='NOAPROBACIONNOT', blank=True, null=True)  # Field name made lowercase.
#     anoaprobacionnot = models.IntegerField(db_column='ANOAPROBACIONNOT', blank=True, null=True)  # Field name made lowercase.
#     pathfilekeynot = models.CharField(db_column='PATHFILEKEYNOT', max_length=254, blank=True, null=True)  # Field name made lowercase.
#     pathfilecernot = models.CharField(db_column='PATHFILECERNOT', max_length=254, blank=True, null=True)  # Field name made lowercase.
#     passwordkeyfilenot = models.CharField(db_column='PASSWORDKEYFILENOT', max_length=24, blank=True, null=True)  # Field name made lowercase.
#     pathcancelfilepfxnot = models.CharField(db_column='PATHCANCELFILEPFXNOT', max_length=999, blank=True, null=True)  # Field name made lowercase.
#     pfxpwdnot = models.CharField(db_column='PFXPWDNOT', max_length=29, blank=True, null=True)  # Field name made lowercase.
#     invoicetypenot = models.CharField(db_column='INVOICETYPENOT', max_length=29, blank=True, null=True)  # Field name made lowercase.
#     date_cer = models.IntegerField(db_column='DATE_CER', blank=True, null=True)  # Field name made lowercase.
#     date_key = models.IntegerField(db_column='DATE_KEY', blank=True, null=True)  # Field name made lowercase.
#     vercuentasenfactua = models.SmallIntegerField(db_column='VERCUENTASENFACTUA', blank=True, null=True)  # Field name made lowercase.
#     nombrebanco_pesos = models.CharField(db_column='NOMBREBANCO_PESOS', max_length=199, blank=True, null=True)  # Field name made lowercase.
#     numcuenta_pesos = models.CharField(db_column='NUMCUENTA_PESOS', max_length=19, blank=True, null=True)  # Field name made lowercase.
#     numclabe_pesos = models.CharField(db_column='NUMCLABE_PESOS', max_length=19, blank=True, null=True)  # Field name made lowercase.
#     nombrebanco_dlls = models.CharField(db_column='NOMBREBANCO_DLLS', max_length=199, blank=True, null=True)  # Field name made lowercase.
#     numcuenta_dlls = models.CharField(db_column='NUMCUENTA_DLLS', max_length=19, blank=True, null=True)  # Field name made lowercase.
#     numclabe_dlls = models.CharField(db_column='NUMCLABE_DLLS', max_length=19, blank=True, null=True)  # Field name made lowercase.
#     pathimportarfacelec = models.CharField(db_column='PATHIMPORTARFACELEC', max_length=511, blank=True, null=True)  # Field name made lowercase.
#     pathexportarfacelec = models.CharField(db_column='PATHEXPORTARFACELEC', max_length=511, blank=True, null=True)  # Field name made lowercase.
#     cfdi33_aplicacion = models.CharField(db_column='CFDI33_APLICACION', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     cfdi33_activa = models.IntegerField(db_column='CFDI33_ACTIVA', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'configuracion'


# class DjangoAdminLog(models.Model):
#     action_time = models.DateTimeField()
#     object_id = models.TextField(blank=True, null=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.SmallIntegerField()
#     change_message = models.TextField()
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'django_admin_log'


# class DjangoContentType(models.Model):
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)

#     class Meta:
#         managed = False
#         db_table = 'django_content_type'
#         unique_together = (('app_label', 'model'),)


# class DjangoMigrations(models.Model):
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'django_migrations'


# class Facfacturaretencion(models.Model):
#     sysid = models.IntegerField(db_column='SYSID', primary_key=True)  # Field name made lowercase.
#     factura = models.CharField(db_column='FACTURA', max_length=19, blank=True, null=True)  # Field name made lowercase.
#     fechafactura = models.IntegerField(db_column='FECHAFACTURA', blank=True, null=True)  # Field name made lowercase.
#     rfc = models.CharField(db_column='RFC', max_length=19, blank=True, null=True)  # Field name made lowercase.
#     moneda = models.CharField(db_column='MONEDA', max_length=19, blank=True, null=True)  # Field name made lowercase.
#     subtotal = models.DecimalField(db_column='SUBTOTAL', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
#     iva = models.DecimalField(db_column='IVA', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
#     retencioniva = models.DecimalField(db_column='RETENCIONIVA', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
#     retencionisr = models.DecimalField(db_column='RETENCIONISR', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
#     total = models.DecimalField(db_column='TOTAL', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'facfacturaretencion'



# class Factdetfacturas(models.Model):
#     consecutivo = models.IntegerField(db_column='CONSECUTIVO', primary_key=True)  # Field name made lowercase.
#     linea = models.IntegerField(db_column='LINEA')  # Field name made lowercase.
#     item = models.CharField(db_column='ITEM', max_length=39, blank=True, null=True)  # Field name made lowercase.
#     descripcion = models.TextField(db_column='DESCRIPCION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     costounitario = models.DecimalField(db_column='COSTOUNITARIO', max_digits=21, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     cantidad = models.DecimalField(db_column='CANTIDAD', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     total = models.DecimalField(db_column='TOTAL', max_digits=25, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     categoria = models.CharField(db_column='CATEGORIA', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     unidadmedida = models.CharField(db_column='UNIDADMEDIDA', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     totaldolares = models.DecimalField(db_column='TOTALDOLARES', max_digits=25, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     moneda = models.CharField(db_column='MONEDA', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     ic_centrocosto = models.CharField(db_column='IC_CENTROCOSTO', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     costounitariopesos = models.DecimalField(db_column='COSTOUNITARIOPESOS', max_digits=21, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     fechainiciocobro = models.IntegerField(db_column='FECHAINICIOCOBRO', blank=True, null=True)  # Field name made lowercase.
#     fechafincobro = models.IntegerField(db_column='FECHAFINCOBRO', blank=True, null=True)  # Field name made lowercase.
#     concepto = models.CharField(db_column='CONCEPTO', max_length=39, blank=True, null=True)  # Field name made lowercase.
#     peso = models.DecimalField(db_column='PESO', max_digits=11, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     partidaiva = models.DecimalField(db_column='PARTIDAIVA', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     partidaivaporcentaje = models.DecimalField(db_column='PARTIDAIVAPORCENTAJE', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     partidaisr = models.DecimalField(db_column='PARTIDAISR', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     partidaisrporcentaje = models.DecimalField(db_column='PARTIDAISRPORCENTAJE', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     partidaivaretenido = models.DecimalField(db_column='PARTIDAIVARETENIDO', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     partidaivaretenidoporcentaje = models.DecimalField(db_column='PARTIDAIVARETENIDOPORCENTAJE', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     cfdi33_claveprodserv = models.CharField(db_column='CFDI33_CLAVEPRODSERV', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     cfdi33_claveprodservdescripcion = models.CharField(db_column='CFDI33_CLAVEPRODSERVDESCRIPCION', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     cfdi33_claveunidad = models.CharField(db_column='CFDI33_CLAVEUNIDAD', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     cfdi33_claveunidaddescripcion = models.CharField(db_column='CFDI33_CLAVEUNIDADDESCRIPCION', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     partidaaplicaiva = models.IntegerField(db_column='PARTIDAAPLICAIVA', blank=True, null=True)  # Field name made lowercase.
#     partidaaplicaisr = models.IntegerField(db_column='PARTIDAAPLICAISR', blank=True, null=True)  # Field name made lowercase.
#     partidaaplicaiva_retenido = models.IntegerField(db_column='PARTIDAAPLICAIVA_RETENIDO', blank=True, null=True)  # Field name made lowercase.
#     partidaiva_dlls = models.DecimalField(db_column='PARTIDAIVA_DLLS', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     partidaisr_dlls = models.DecimalField(db_column='PARTIDAISR_DLLS', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     partidaivaretenido_dlls = models.DecimalField(db_column='PARTIDAIVARETENIDO_DLLS', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     cfdi33_cartaporte = models.IntegerField(db_column='CFDI33_CARTAPORTE', blank=True, null=True)  # Field name made lowercase.
#     cfdi33_cuentapredial = models.CharField(db_column='CFDI33_CUENTAPREDIAL', max_length=154, blank=True, null=True)  # Field name made lowercase.
#     cfdi33_descuentopesos = models.DecimalField(db_column='CFDI33_DESCUENTOPESOS', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     cfdi33_descuentodolares = models.DecimalField(db_column='CFDI33_DESCUENTODOLARES', max_digits=17, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     comercioexterior_activo = models.IntegerField(db_column='COMERCIOEXTERIOR_ACTIVO', blank=True, null=True)  # Field name made lowercase.
#     comercioexterior_noidentificacion = models.CharField(db_column='COMERCIOEXTERIOR_NOIDENTIFICACION', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     comercioexterior_fraccionarancelaria = models.CharField(db_column='COMERCIOEXTERIOR_FRACCIONARANCELARIA', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     comercioexterior_cantidadaduana = models.DecimalField(db_column='COMERCIOEXTERIOR_CANTIDADADUANA', max_digits=15, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
#     comercioexterior_unidadaduana = models.CharField(db_column='COMERCIOEXTERIOR_UNIDADADUANA', max_length=4, blank=True, null=True)  # Field name made lowercase.
#     comercioexterior_valorunitarioaduana = models.DecimalField(db_column='COMERCIOEXTERIOR_VALORUNITARIOADUANA', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     comercioexterior_valordolares = models.DecimalField(db_column='COMERCIOEXTERIOR_VALORDOLARES', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     comercioexterior_descripcionesespecificas_marca = models.CharField(db_column='COMERCIOEXTERIOR_DESCRIPCIONESESPECIFICAS_MARCA', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     comercioexterior_descripcionesespecificas_modelo = models.CharField(db_column='COMERCIOEXTERIOR_DESCRIPCIONESESPECIFICAS_MODELO', max_length=80, blank=True, null=True)  # Field name made lowercase.
#     comercioexterior_descripcionesespecificas_submodelo = models.CharField(db_column='COMERCIOEXTERIOR_DESCRIPCIONESESPECIFICAS_SUBMODELO', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     comercioexterior_descripcionesespecificas_numeroserie = models.CharField(db_column='COMERCIOEXTERIOR_DESCRIPCIONESESPECIFICAS_NUMEROSERIE', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     tipoconcepto_anticipos_cfd33 = models.CharField(db_column='TIPOCONCEPTO_ANTICIPOS_CFD33', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     cfdi33_objetoimp = models.CharField(db_column='CFDI33_OBJETOIMP', max_length=3, blank=True, null=True)  # Field name made lowercase.
#     rfcacuentaterceros = models.CharField(db_column='RFCACUENTATERCEROS', max_length=18, blank=True, null=True)  # Field name made lowercase.
#     nombreacuentaterceros = models.CharField(db_column='NOMBREACUENTATERCEROS', max_length=254, blank=True, null=True)  # Field name made lowercase.
#     regimenfiscalacuentaterceros = models.CharField(db_column='REGIMENFISCALACUENTATERCEROS', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     domiciliofiscalacuentaterceros = models.CharField(db_column='DOMICILIOFISCALACUENTATERCEROS', max_length=10, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'factdetfacturas'
#         unique_together = (('consecutivo', 'linea'),)


# class Factdetpagos(models.Model):
#     numero = models.IntegerField(db_column='NUMERO', primary_key=True)  # Field name made lowercase.
#     factura = models.CharField(db_column='FACTURA', max_length=14)  # Field name made lowercase.
#     importe = models.DecimalField(db_column='IMPORTE', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     importedolares = models.DecimalField(db_column='IMPORTEDOLARES', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     formapago = models.CharField(db_column='FORMAPAGO', max_length=24, blank=True, null=True)  # Field name made lowercase.
#     notascredito = models.CharField(db_column='NOTASCREDITO', max_length=49, blank=True, null=True)  # Field name made lowercase.
#     linea = models.IntegerField(db_column='LINEA', blank=True, null=True)  # Field name made lowercase.
#     importereal = models.DecimalField(db_column='IMPORTEREAL', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     saldo = models.DecimalField(db_column='SALDO', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     importereal_dll = models.DecimalField(db_column='IMPORTEREAL_DLL', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     saldo_dolares = models.DecimalField(db_column='SALDO_DOLARES', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     saldo_anterior = models.DecimalField(db_column='SALDO_ANTERIOR', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     saldo_anterior_dolares = models.DecimalField(db_column='SALDO_ANTERIOR_DOLARES', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     fechacomplemenoint = models.IntegerField(db_column='FECHACOMPLEMENOINT', blank=True, null=True)  # Field name made lowercase.
#     cfdifechacomplemeno = models.CharField(db_column='CFDIFECHACOMPLEMENO', max_length=64, blank=True, null=True)  # Field name made lowercase.
#     equivalenciadr = models.DecimalField(db_column='EQUIVALENCIADR', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     objetoimpdr = models.CharField(db_column='OBJETOIMPDR', max_length=19, blank=True, null=True)  # Field name made lowercase.
#     ret_basedr = models.DecimalField(db_column='RET_BASEDR', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     ret_impuestodr = models.CharField(db_column='RET_IMPUESTODR', max_length=4, blank=True, null=True)  # Field name made lowercase.
#     ret_tipofactordr = models.CharField(db_column='RET_TIPOFACTORDR', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     ret_tasaocuotadr = models.DecimalField(db_column='RET_TASAOCUOTADR', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     ret_importedr = models.DecimalField(db_column='RET_IMPORTEDR', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     tras_basedr = models.DecimalField(db_column='TRAS_BASEDR', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     tras_impuestodr = models.CharField(db_column='TRAS_IMPUESTODR', max_length=4, blank=True, null=True)  # Field name made lowercase.
#     tras_tipofactordr = models.CharField(db_column='TRAS_TIPOFACTORDR', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     tras_tasaocuotadr = models.DecimalField(db_column='TRAS_TASAOCUOTADR', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     tras_importedr = models.DecimalField(db_column='TRAS_IMPORTEDR', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     ret_basedr_1 = models.DecimalField(db_column='RET_BASEDR_1', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     ret_impuestodr_1 = models.CharField(db_column='RET_IMPUESTODR_1', max_length=4, blank=True, null=True)  # Field name made lowercase.
#     ret_tipofactordr_1 = models.CharField(db_column='RET_TIPOFACTORDR_1', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     ret_tasaocuotadr_1 = models.DecimalField(db_column='RET_TASAOCUOTADR_1', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     ret_importedr_1 = models.DecimalField(db_column='RET_IMPORTEDR_1', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'factdetpagos'
#         unique_together = (('numero', 'factura'),)



# class Factfactura(models.Model):
#     consecutivo = models.IntegerField(db_column='CONSECUTIVO', primary_key=True)  # Field name made lowercase.
#     factura = models.CharField(db_column='FACTURA', unique=True, max_length=14, blank=True, null=True)  # Field name made lowercase.
#     cliente = models.CharField(db_column='CLIENTE', max_length=9, blank=True, null=True)  # Field name made lowercase.
#     fecha = models.IntegerField(db_column='FECHA', blank=True, null=True)  # Field name made lowercase.
#     tipocambio = models.DecimalField(db_column='TIPOCAMBIO', max_digits=9, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     estatus = models.CharField(db_column='ESTATUS', max_length=14, blank=True, null=True)  # Field name made lowercase.
#     ordencompra = models.CharField(db_column='ORDENCOMPRA', max_length=12, blank=True, null=True)  # Field name made lowercase.
#     moneda = models.CharField(db_column='MONEDA', max_length=7, blank=True, null=True)  # Field name made lowercase.
#     condicionpago = models.CharField(db_column='CONDICIONPAGO', max_length=59, blank=True, null=True)  # Field name made lowercase.
#     operador = models.CharField(db_column='OPERADOR', max_length=6, blank=True, null=True)  # Field name made lowercase.
#     contacto = models.CharField(db_column='CONTACTO', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     comentario = models.CharField(db_column='COMENTARIO', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     porcentajeiva = models.DecimalField(db_column='PORCENTAJEIVA', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     descuento = models.DecimalField(db_column='DESCUENTO', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     subtotal = models.DecimalField(db_column='SUBTOTAL', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     flete = models.DecimalField(db_column='FLETE', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     iva = models.DecimalField(db_column='IVA', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     valorpagado = models.DecimalField(db_column='VALORPAGADO', max_digits=17, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     total = models.DecimalField(db_column='TOTAL', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     saldo = models.DecimalField(db_column='SALDO', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     ticket = models.CharField(db_column='TICKET', max_length=12, blank=True, null=True)  # Field name made lowercase.
#     cotizacion = models.CharField(db_column='COTIZACION', max_length=12, blank=True, null=True)  # Field name made lowercase.
#     lineacotizacion = models.IntegerField(db_column='LINEACOTIZACION', blank=True, null=True)  # Field name made lowercase.
#     observaciones = models.CharField(db_column='OBSERVACIONES', max_length=999, blank=True, null=True)  # Field name made lowercase.
#     fechaembargue = models.IntegerField(db_column='FECHAEMBARGUE', blank=True, null=True)  # Field name made lowercase.
#     viaembargue = models.CharField(db_column='VIAEMBARGUE', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     lab = models.CharField(db_column='LAB', max_length=49, blank=True, null=True)  # Field name made lowercase.
#     embarcarcliente = models.CharField(db_column='EMBARCARCLIENTE', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     aplicadescuento = models.SmallIntegerField(db_column='APLICADESCUENTO', blank=True, null=True)  # Field name made lowercase.
#     porcentajedescuento = models.DecimalField(db_column='PORCENTAJEDESCUENTO', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     descuentodolares = models.DecimalField(db_column='DESCUENTODOLARES', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     ivadolares = models.DecimalField(db_column='IVADOLARES', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     subtotaldolares = models.DecimalField(db_column='SUBTOTALDOLARES', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     fletedolares = models.DecimalField(db_column='FLETEDOLARES', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     valorpagadodolares = models.DecimalField(db_column='VALORPAGADODOLARES', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     totaldolares = models.DecimalField(db_column='TOTALDOLARES', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     saldodolares = models.DecimalField(db_column='SALDODOLARES', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     pago = models.CharField(db_column='PAGO', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     programada = models.CharField(db_column='PROGRAMADA', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     vendedor = models.CharField(db_column='VENDEDOR', max_length=6, blank=True, null=True)  # Field name made lowercase.
#     inventariado = models.SmallIntegerField(db_column='INVENTARIADO', blank=True, null=True)  # Field name made lowercase.
#     anticipo = models.DecimalField(db_column='ANTICIPO', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     anticipodolares = models.DecimalField(db_column='ANTICIPODOLARES', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     retencioniva = models.DecimalField(db_column='RETENCIONIVA', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     retencionpesos = models.DecimalField(db_column='RETENCIONPESOS', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     retenciondolares = models.DecimalField(db_column='RETENCIONDOLARES', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     otrosgastos = models.DecimalField(db_column='OTROSGASTOS', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     hora = models.IntegerField(db_column='HORA', blank=True, null=True)  # Field name made lowercase.
#     comision = models.DecimalField(db_column='COMISION', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     comisiondolares = models.DecimalField(db_column='COMISIONDOLARES', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     empresa = models.CharField(db_column='EMPRESA', max_length=14, blank=True, null=True)  # Field name made lowercase.
#     notascredito = models.CharField(db_column='NOTASCREDITO', max_length=49, blank=True, null=True)  # Field name made lowercase.
#     porcentajeretencioniva = models.DecimalField(db_column='PORCENTAJERETENCIONIVA', max_digits=9, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
#     retencionivapesos = models.DecimalField(db_column='RETENCIONIVAPESOS', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     retencionivadolares = models.DecimalField(db_column='RETENCIONIVADOLARES', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     porcentajeretencionisr = models.DecimalField(db_column='PORCENTAJERETENCIONISR', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     retencionisrpesos = models.DecimalField(db_column='RETENCIONISRPESOS', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     retencionisrdolares = models.DecimalField(db_column='RETENCIONISRDOLARES', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     aplicaretencioniva = models.SmallIntegerField(db_column='APLICARETENCIONIVA', blank=True, null=True)  # Field name made lowercase.
#     aplicaretencionisr = models.SmallIntegerField(db_column='APLICARETENCIONISR', blank=True, null=True)  # Field name made lowercase.
#     isfacturaelectronica = models.SmallIntegerField(db_column='ISFACTURAELECTRONICA', blank=True, null=True)  # Field name made lowercase.
#     sellodigital = models.CharField(db_column='SELLODIGITAL', max_length=999, blank=True, null=True)  # Field name made lowercase.
#     cadenaoriginal = models.TextField(db_column='CADENAORIGINAL', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     foliopac = models.CharField(db_column='FOLIOPAC', max_length=99, blank=True, null=True)  # Field name made lowercase.
#     fetype = models.CharField(db_column='FETYPE', max_length=9, blank=True, null=True)  # Field name made lowercase.
#     noaprovacion = models.CharField(db_column='NOAPROVACION', max_length=29, blank=True, null=True)  # Field name made lowercase.
#     anioaprovacion = models.CharField(db_column='ANIOAPROVACION', max_length=19, blank=True, null=True)  # Field name made lowercase.
#     seriecfd = models.CharField(db_column='SERIECFD', max_length=29, blank=True, null=True)  # Field name made lowercase.
#     sellopac = models.TextField(db_column='SELLOPAC', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     nocertificado = models.CharField(db_column='NOCERTIFICADO', max_length=59, blank=True, null=True)  # Field name made lowercase.
#     nocertificadosat = models.CharField(db_column='NOCERTIFICADOSAT', max_length=79, blank=True, null=True)  # Field name made lowercase.
#     fechacertificacion = models.CharField(db_column='FECHACERTIFICACION', max_length=24, blank=True, null=True)  # Field name made lowercase.
#     fechacertificacionsistema = models.IntegerField(db_column='FECHACERTIFICACIONSISTEMA', blank=True, null=True)  # Field name made lowercase.
#     cartaporte = models.IntegerField(db_column='CARTAPORTE', blank=True, null=True)  # Field name made lowercase.
#     clientedestino = models.CharField(db_column='CLIENTEDESTINO', max_length=9, blank=True, null=True)  # Field name made lowercase.
#     destino = models.CharField(db_column='DESTINO', max_length=44, blank=True, null=True)  # Field name made lowercase.
#     origen = models.CharField(db_column='ORIGEN', max_length=44, blank=True, null=True)  # Field name made lowercase.
#     recogeren = models.CharField(db_column='RECOGEREN', max_length=44, blank=True, null=True)  # Field name made lowercase.
#     entregaraen = models.CharField(db_column='ENTREGARAEN', max_length=44, blank=True, null=True)  # Field name made lowercase.
#     sellocartaporte = models.CharField(db_column='SELLOCARTAPORTE', max_length=19, blank=True, null=True)  # Field name made lowercase.
#     operadorcartaporte = models.CharField(db_column='OPERADORCARTAPORTE', max_length=79, blank=True, null=True)  # Field name made lowercase.
#     sellodigitalsat = models.CharField(db_column='SELLODIGITALSAT', max_length=999, blank=True, null=True)  # Field name made lowercase.
#     cadenaoriginalsat = models.TextField(db_column='CADENAORIGINALSAT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     emisor_nombre = models.CharField(db_column='EMISOR_NOMBRE', max_length=199, blank=True, null=True)  # Field name made lowercase.
#     emisor_direccion = models.CharField(db_column='EMISOR_DIRECCION', max_length=199, blank=True, null=True)  # Field name made lowercase.
#     emisor_colonia = models.CharField(db_column='EMISOR_COLONIA', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     emisor_cp = models.CharField(db_column='EMISOR_CP', max_length=14, blank=True, null=True)  # Field name made lowercase.
#     emisor_estado = models.CharField(db_column='EMISOR_ESTADO', max_length=19, blank=True, null=True)  # Field name made lowercase.
#     emisor_pais = models.CharField(db_column='EMISOR_PAIS', max_length=24, blank=True, null=True)  # Field name made lowercase.
#     emisor_rfc = models.CharField(db_column='EMISOR_RFC', max_length=19, blank=True, null=True)  # Field name made lowercase.
#     emisor_numeroext = models.CharField(db_column='EMISOR_NUMEROEXT', max_length=24, blank=True, null=True)  # Field name made lowercase.
#     emisor_ciudad = models.CharField(db_column='EMISOR_CIUDAD', max_length=19, blank=True, null=True)  # Field name made lowercase.
#     receptor_nombre = models.CharField(db_column='RECEPTOR_NOMBRE', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     receptor_direccion = models.CharField(db_column='RECEPTOR_DIRECCION', max_length=250, blank=True, null=True)  # Field name made lowercase.
#     receptor_ciudad = models.CharField(db_column='RECEPTOR_CIUDAD', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     receptor_estado = models.CharField(db_column='RECEPTOR_ESTADO', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     receptor_cp = models.CharField(db_column='RECEPTOR_CP', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     receptor_pais = models.CharField(db_column='RECEPTOR_PAIS', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     receptor_numeroext = models.CharField(db_column='RECEPTOR_NUMEROEXT', max_length=19, blank=True, null=True)  # Field name made lowercase.
#     receptor_colonia = models.CharField(db_column='RECEPTOR_COLONIA', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     receptor_rfc = models.CharField(db_column='RECEPTOR_RFC', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     facturaexpedida = models.CharField(db_column='FACTURAEXPEDIDA', max_length=299, blank=True, null=True)  # Field name made lowercase.
#     istransferencia = models.SmallIntegerField(db_column='ISTRANSFERENCIA', blank=True, null=True)  # Field name made lowercase.
#     numctapago = models.CharField(db_column='NUMCTAPAGO', max_length=4, blank=True, null=True)  # Field name made lowercase.
#     observaciones2 = models.TextField(db_column='OBSERVACIONES2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     proyecto = models.CharField(db_column='PROYECTO', max_length=24, blank=True, null=True)  # Field name made lowercase.
#     c1 = models.CharField(db_column='C1', max_length=254, blank=True, null=True)  # Field name made lowercase.
#     c2 = models.CharField(db_column='C2', max_length=254, blank=True, null=True)  # Field name made lowercase.
#     c3 = models.CharField(db_column='C3', max_length=254, blank=True, null=True)  # Field name made lowercase.
#     c4 = models.CharField(db_column='C4', max_length=254, blank=True, null=True)  # Field name made lowercase.
#     c5 = models.CharField(db_column='C5', max_length=254, blank=True, null=True)  # Field name made lowercase.
#     c6 = models.CharField(db_column='C6', max_length=254, blank=True, null=True)  # Field name made lowercase.
#     c7 = models.CharField(db_column='C7', max_length=254, blank=True, null=True)  # Field name made lowercase.
#     c8 = models.CharField(db_column='C8', max_length=254, blank=True, null=True)  # Field name made lowercase.
#     c9 = models.CharField(db_column='C9', max_length=254, blank=True, null=True)  # Field name made lowercase.
#     c10 = models.CharField(db_column='C10', max_length=254, blank=True, null=True)  # Field name made lowercase.
#     c11 = models.CharField(db_column='C11', max_length=254, blank=True, null=True)  # Field name made lowercase.
#     c12 = models.CharField(db_column='C12', max_length=254, blank=True, null=True)  # Field name made lowercase.
#     c13 = models.CharField(db_column='C13', max_length=254, blank=True, null=True)  # Field name made lowercase.
#     c14 = models.CharField(db_column='C14', max_length=254, blank=True, null=True)  # Field name made lowercase.
#     c15 = models.CharField(db_column='C15', max_length=254, blank=True, null=True)  # Field name made lowercase.
#     c16 = models.CharField(db_column='C16', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     c17 = models.CharField(db_column='C17', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     c18 = models.CharField(db_column='C18', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     c19 = models.CharField(db_column='C19', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     c20 = models.CharField(db_column='C20', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     otros_cartaporte = models.DecimalField(db_column='OTROS_CARTAPORTE', max_digits=13, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
#     emisor_nointerior = models.TextField(db_column='EMISOR_NOINTERIOR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     receptor_nointerior = models.TextField(db_column='RECEPTOR_NOINTERIOR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     reembarco = models.CharField(db_column='REEMBARCO', max_length=119, blank=True, null=True)  # Field name made lowercase.
#     reembarcarcecon = models.CharField(db_column='REEMBARCARCECON', max_length=119, blank=True, null=True)  # Field name made lowercase.
#     condujo = models.CharField(db_column='CONDUJO', max_length=149, blank=True, null=True)  # Field name made lowercase.
#     conducira = models.CharField(db_column='CONDUCIRA', max_length=149, blank=True, null=True)  # Field name made lowercase.
#     de1 = models.CharField(db_column='DE1', max_length=99, blank=True, null=True)  # Field name made lowercase.
#     de2 = models.CharField(db_column='DE2', max_length=99, blank=True, null=True)  # Field name made lowercase.
#     a1 = models.CharField(db_column='A1', max_length=119, blank=True, null=True)  # Field name made lowercase.
#     a2 = models.CharField(db_column='A2', max_length=119, blank=True, null=True)  # Field name made lowercase.
#     documento = models.CharField(db_column='DOCUMENTO', max_length=39, blank=True, null=True)  # Field name made lowercase.
#     notractor = models.CharField(db_column='NOTRACTOR', max_length=19, blank=True, null=True)  # Field name made lowercase.
#     remolque = models.CharField(db_column='REMOLQUE', max_length=24, blank=True, null=True)  # Field name made lowercase.
#     valoragregado = models.CharField(db_column='VALORAGREGADO', max_length=14, blank=True, null=True)  # Field name made lowercase.
#     porcentajeinterespagare = models.IntegerField(db_column='PORCENTAJEINTERESPAGARE', blank=True, null=True)  # Field name made lowercase.
#     complementoiva = models.SmallIntegerField(db_column='COMPLEMENTOIVA', blank=True, null=True)  # Field name made lowercase.
#     addcomplementonotario = models.SmallIntegerField(db_column='ADDCOMPLEMENTONOTARIO', blank=True, null=True)  # Field name made lowercase.
#     inmueble_tipo = models.CharField(db_column='INMUEBLE_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     inmueble_calle = models.CharField(db_column='INMUEBLE_CALLE', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     inmueble_noexterior = models.CharField(db_column='INMUEBLE_NOEXTERIOR', max_length=55, blank=True, null=True)  # Field name made lowercase.
#     inmueble_nointerior = models.CharField(db_column='INMUEBLE_NOINTERIOR', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     inmueble_colonia = models.CharField(db_column='INMUEBLE_COLONIA', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     inmueble_localidad = models.CharField(db_column='INMUEBLE_LOCALIDAD', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     inmueble_referencia = models.CharField(db_column='INMUEBLE_REFERENCIA', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     inmueble_municipio = models.CharField(db_column='INMUEBLE_MUNICIPIO', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     inmueble_estado = models.CharField(db_column='INMUEBLE_ESTADO', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     inmueble_pais = models.CharField(db_column='INMUEBLE_PAIS', max_length=3, blank=True, null=True)  # Field name made lowercase.
#     inmueble_codigopostal = models.CharField(db_column='INMUEBLE_CODIGOPOSTAL', max_length=5, blank=True, null=True)  # Field name made lowercase.
#     operacion_numinstrumentonotarial = models.IntegerField(db_column='OPERACION_NUMINSTRUMENTONOTARIAL', blank=True, null=True)  # Field name made lowercase.
#     operacion_fechainstnotarial = models.IntegerField(db_column='OPERACION_FECHAINSTNOTARIAL', blank=True, null=True)  # Field name made lowercase.
#     operacion_montooperacion = models.DecimalField(db_column='OPERACION_MONTOOPERACION', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
#     operacion_subtotal = models.DecimalField(db_column='OPERACION_SUBTOTAL', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
#     operacion_iva = models.DecimalField(db_column='OPERACION_IVA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
#     notario_curp = models.CharField(db_column='NOTARIO_CURP', max_length=19, blank=True, null=True)  # Field name made lowercase.
#     notario_numnotaria = models.IntegerField(db_column='NOTARIO_NUMNOTARIA', blank=True, null=True)  # Field name made lowercase.
#     notario_entidadfederativa = models.CharField(db_column='NOTARIO_ENTIDADFEDERATIVA', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     notaria_adscripcion = models.CharField(db_column='NOTARIA_ADSCRIPCION', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     enajenante_coprosocconyugale = models.CharField(db_column='ENAJENANTE_COPROSOCCONYUGALE', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     adquiriente_coprosocconyugale = models.CharField(db_column='ADQUIRIENTE_COPROSOCCONYUGALE', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     emitirdestinatarioencartaporte = models.SmallIntegerField(db_column='EMITIRDESTINATARIOENCARTAPORTE', blank=True, null=True)  # Field name made lowercase.
#     confsendemail = models.CharField(db_column='CONFSENDEMAIL', max_length=19, blank=True, null=True)  # Field name made lowercase.
#     fechasendemail = models.IntegerField(db_column='FECHASENDEMAIL', blank=True, null=True)  # Field name made lowercase.
#     cc = models.CharField(db_column='CC', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     version = models.CharField(db_column='VERSION', max_length=4, blank=True, null=True)  # Field name made lowercase.
#     pagprovefecporfiduc = models.DecimalField(db_column='PAGPROVEFECPORFIDUC', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     rendimfideicom = models.DecimalField(db_column='RENDIMFIDEICOM', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     deducccorresp = models.DecimalField(db_column='DEDUCCCORRESP', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     monttotret = models.DecimalField(db_column='MONTTOTRET', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     montresfiscdistfibras = models.DecimalField(db_column='MONTRESFISCDISTFIBRAS', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     montotrosconceptdistr = models.DecimalField(db_column='MONTOTROSCONCEPTDISTR', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     descrmontotrosconceptdistr = models.CharField(db_column='DESCRMONTOTROSCONCEPTDISTR', max_length=499, blank=True, null=True)  # Field name made lowercase.
#     esbenefefectdelcobro = models.CharField(db_column='ESBENEFEFECTDELCOBRO', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     paisderesidparaefecfisc = models.CharField(db_column='PAISDERESIDPARAEFECFISC', max_length=3, blank=True, null=True)  # Field name made lowercase.
#     conceptopago_nobeneficiario = models.IntegerField(db_column='CONCEPTOPAGO_NOBENEFICIARIO', blank=True, null=True)  # Field name made lowercase.
#     descripcionconcepto_nobeneficiario = models.CharField(db_column='DESCRIPCIONCONCEPTO_NOBENEFICIARIO', max_length=254, blank=True, null=True)  # Field name made lowercase.
#     rfc = models.CharField(db_column='RFC', max_length=24, blank=True, null=True)  # Field name made lowercase.
#     curp = models.CharField(db_column='CURP', max_length=24, blank=True, null=True)  # Field name made lowercase.
#     nomdenrazsocb = models.CharField(db_column='NOMDENRAZSOCB', max_length=299, blank=True, null=True)  # Field name made lowercase.
#     conceptopago_beneficiario = models.IntegerField(db_column='CONCEPTOPAGO_BENEFICIARIO', blank=True, null=True)  # Field name made lowercase.
#     descripcionconcepto_beneficiario = models.CharField(db_column='DESCRIPCIONCONCEPTO_BENEFICIARIO', max_length=254, blank=True, null=True)  # Field name made lowercase.
#     entidadfederativa = models.CharField(db_column='ENTIDADFEDERATIVA', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     monttotpago = models.DecimalField(db_column='MONTTOTPAGO', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     monttotpagograv = models.DecimalField(db_column='MONTTOTPAGOGRAV', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     monttotpagoexent = models.DecimalField(db_column='MONTTOTPAGOEXENT', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     monttotentradasperiodo = models.DecimalField(db_column='MONTTOTENTRADASPERIODO', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     partpropacumdelfideicom = models.DecimalField(db_column='PARTPROPACUMDELFIDEICOM', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     propdelmonttot_ingresosoentradas = models.DecimalField(db_column='PROPDELMONTTOT_INGRESOSOENTRADAS', max_digits=7, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     concepto_integracingresos = models.CharField(db_column='CONCEPTO_INTEGRACINGRESOS', max_length=99, blank=True, null=True)  # Field name made lowercase.
#     monttotegresperiodo = models.DecimalField(db_column='MONTTOTEGRESPERIODO', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     partpropdelfideicom = models.DecimalField(db_column='PARTPROPDELFIDEICOM', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     propdelmonttot_deduccosalidas = models.DecimalField(db_column='PROPDELMONTTOT_DEDUCCOSALIDAS', max_digits=7, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     concepto_integracegresos = models.CharField(db_column='CONCEPTO_INTEGRACEGRESOS', max_length=99, blank=True, null=True)  # Field name made lowercase.
#     montretrelpagfideic = models.DecimalField(db_column='MONTRETRELPAGFIDEIC', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     descretrelpagfidec = models.CharField(db_column='DESCRETRELPAGFIDEC', max_length=99, blank=True, null=True)  # Field name made lowercase.
#     sistemafinanc = models.CharField(db_column='SISTEMAFINANC', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     monttotaportanioinmanterior = models.DecimalField(db_column='MONTTOTAPORTANIOINMANTERIOR', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     montintrealesdevenganiooinmant = models.DecimalField(db_column='MONTINTREALESDEVENGANIOOINMANT', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     huboretirosanioinmantper = models.CharField(db_column='HUBORETIROSANIOINMANTPER', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     monttotretiradoanioinmantper = models.DecimalField(db_column='MONTTOTRETIRADOANIOINMANTPER', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     monttotexentretiradoanioinmant = models.DecimalField(db_column='MONTTOTEXENTRETIRADOANIOINMANT', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     monttotexedenteanioinmant = models.DecimalField(db_column='MONTTOTEXEDENTEANIOINMANT', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     huboretirosanioinmant = models.CharField(db_column='HUBORETIROSANIOINMANT', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     monttotretiradoanioinmant = models.DecimalField(db_column='MONTTOTRETIRADOANIOINMANT', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     creditodeinstfinanc = models.CharField(db_column='CREDITODEINSTFINANC', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     saldoinsoluto = models.DecimalField(db_column='SALDOINSOLUTO', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     propdeducdelcredit = models.DecimalField(db_column='PROPDEDUCDELCREDIT', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     monttotintnominalesdev = models.DecimalField(db_column='MONTTOTINTNOMINALESDEV', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     monttotintnominalesdevypag = models.DecimalField(db_column='MONTTOTINTNOMINALESDEVYPAG', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     monttotintrealpagdeduc = models.DecimalField(db_column='MONTTOTINTREALPAGDEDUC', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     numcontrato = models.CharField(db_column='NUMCONTRATO', max_length=299, blank=True, null=True)  # Field name made lowercase.
#     montganacum = models.DecimalField(db_column='MONTGANACUM', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     montperdded = models.DecimalField(db_column='MONTPERDDED', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     idfideicom = models.CharField(db_column='IDFIDEICOM', max_length=19, blank=True, null=True)  # Field name made lowercase.
#     nomfideicom = models.CharField(db_column='NOMFIDEICOM', max_length=99, blank=True, null=True)  # Field name made lowercase.
#     descripfideicom = models.CharField(db_column='DESCRIPFIDEICOM', max_length=299, blank=True, null=True)  # Field name made lowercase.
#     cvetipdivoutil = models.CharField(db_column='CVETIPDIVOUTIL', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     montisracredretmexico = models.DecimalField(db_column='MONTISRACREDRETMEXICO', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     montisracredretextranjero = models.DecimalField(db_column='MONTISRACREDRETEXTRANJERO', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     montretextdivext = models.DecimalField(db_column='MONTRETEXTDIVEXT', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     tiposocdistrdiv = models.CharField(db_column='TIPOSOCDISTRDIV', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     montisracrednal = models.DecimalField(db_column='MONTISRACREDNAL', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     montdivacumnal = models.DecimalField(db_column='MONTDIVACUMNAL', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     montdivacumext = models.DecimalField(db_column='MONTDIVACUMEXT', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     proporcionrem = models.DecimalField(db_column='PROPORCIONREM', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     sistfinanciero = models.CharField(db_column='SISTFINANCIERO', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     retiroaoresretint = models.CharField(db_column='RETIROAORESRETINT', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     operfinancderivad = models.CharField(db_column='OPERFINANCDERIVAD', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     montintnominal = models.DecimalField(db_column='MONTINTNOMINAL', max_digits=7, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     montintreal = models.DecimalField(db_column='MONTINTREAL', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     perdida = models.DecimalField(db_column='PERDIDA', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     contratointermediacion = models.CharField(db_column='CONTRATOINTERMEDIACION', max_length=299, blank=True, null=True)  # Field name made lowercase.
#     ganancia = models.DecimalField(db_column='GANANCIA', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     perdida_enajenaciondeacciones = models.DecimalField(db_column='PERDIDA_ENAJENACIONDEACCIONES', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     tiporetencion = models.IntegerField(db_column='TIPORETENCION', blank=True, null=True)  # Field name made lowercase.
#     tipopagoret = models.CharField(db_column='TIPOPAGORET', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     retencionestado = models.SmallIntegerField(db_column='RETENCIONESTADO', blank=True, null=True)  # Field name made lowercase.
#     retencionco = models.CharField(db_column='RETENCIONCO', max_length=999, blank=True, null=True)  # Field name made lowercase.
#     retencioncosat = models.TextField(db_column='RETENCIONCOSAT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     retenciontimbre = models.CharField(db_column='RETENCIONTIMBRE', max_length=999, blank=True, null=True)  # Field name made lowercase.
#     retencioncert = models.CharField(db_column='RETENCIONCERT', max_length=59, blank=True, null=True)  # Field name made lowercase.
#     retencionfechacert = models.IntegerField(db_column='RETENCIONFECHACERT', blank=True, null=True)  # Field name made lowercase.
#     retencionejercicio = models.IntegerField(db_column='RETENCIONEJERCICIO', blank=True, null=True)  # Field name made lowercase.
#     retencionmesini = models.IntegerField(db_column='RETENCIONMESINI', blank=True, null=True)  # Field name made lowercase.
#     retencionmesfin = models.IntegerField(db_column='RETENCIONMESFIN', blank=True, null=True)  # Field name made lowercase.
#     retencionfoliopac = models.CharField(db_column='RETENCIONFOLIOPAC', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     claveretsat = models.IntegerField(db_column='CLAVERETSAT', blank=True, null=True)  # Field name made lowercase.
#     baseret = models.DecimalField(db_column='BASERET', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     impuest_otros = models.CharField(db_column='IMPUEST_OTROS', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     montoret_otros = models.DecimalField(db_column='MONTORET_OTROS', max_digits=15, decimal_places=5, blank=True, null=True)  # Field name made lowercase.
#     tipopagoret_otros = models.CharField(db_column='TIPOPAGORET_OTROS', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     boolformapago = models.SmallIntegerField(db_column='BOOLFORMAPAGO', blank=True, null=True)  # Field name made lowercase.
#     ce = models.SmallIntegerField(db_column='CE', blank=True, null=True)  # Field name made lowercase.
#     cfdi33_emisorregimenfiscal = models.CharField(db_column='CFDI33_EMISORREGIMENFISCAL', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     cfdi33_emisorregimenfiscaldescripcion = models.CharField(db_column='CFDI33_EMISORREGIMENFISCALDESCRIPCION', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     cfdi33_receptor_usocfdi = models.CharField(db_column='CFDI33_RECEPTOR_USOCFDI', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     cfdi33_receptor_usocfdidescripcion = models.CharField(db_column='CFDI33_RECEPTOR_USOCFDIDESCRIPCION', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     cfdi33_generada = models.IntegerField(db_column='CFDI33_GENERADA', blank=True, null=True)  # Field name made lowercase.
#     cfdi33_metodopago = models.CharField(db_column='CFDI33_METODOPAGO', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     cfdi33_metodopagodescripcion = models.CharField(db_column='CFDI33_METODOPAGODESCRIPCION', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     cfdi33_tipocomprobante = models.CharField(db_column='CFDI33_TIPOCOMPROBANTE', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     cfdi33_fechayhoraemision = models.CharField(db_column='CFDI33_FECHAYHORAEMISION', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     cfdi33_aplicaiva = models.IntegerField(db_column='CFDI33_APLICAIVA', blank=True, null=True)  # Field name made lowercase.
#     cfdi33_residenciafiscal = models.CharField(db_column='CFDI33_RESIDENCIAFISCAL', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     cfdi33_residenciafiscaldescripcion = models.CharField(db_column='CFDI33_RESIDENCIAFISCALDESCRIPCION', max_length=249, blank=True, null=True)  # Field name made lowercase.
#     cfdi33_numregidtrib = models.CharField(db_column='CFDI33_NUMREGIDTRIB', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     cfdi33_versiontimbrado = models.CharField(db_column='CFDI33_VERSIONTIMBRADO', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     cfdi33_rfcprovcertificacion = models.CharField(db_column='CFDI33_RFCPROVCERTIFICACION', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     cfdi33_operacion_fechainstnotarial = models.CharField(db_column='CFDI33_OPERACION_FECHAINSTNOTARIAL', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     egreso_cadenaoriginal = models.TextField(db_column='EGRESO_CADENAORIGINAL', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     egreso_sellodigital = models.CharField(db_column='EGRESO_SELLODIGITAL', max_length=999, blank=True, null=True)  # Field name made lowercase.
#     egreso_nocertificado = models.CharField(db_column='EGRESO_NOCERTIFICADO', max_length=99, blank=True, null=True)  # Field name made lowercase.
#     egreso_foliopac = models.CharField(db_column='EGRESO_FOLIOPAC', max_length=99, blank=True, null=True)  # Field name made lowercase.
#     egreso_fechacertificacion = models.CharField(db_column='EGRESO_FECHACERTIFICACION', max_length=24, blank=True, null=True)  # Field name made lowercase.
#     egreso_sellocfdtimbrado = models.CharField(db_column='EGRESO_SELLOCFDTIMBRADO', max_length=99, blank=True, null=True)  # Field name made lowercase.
#     egreso_cfdi33_rfcprovcertificacion = models.CharField(db_column='EGRESO_CFDI33_RFCPROVCERTIFICACION', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     egreso_cfdi33_versiontimbrado = models.CharField(db_column='EGRESO_CFDI33_VERSIONTIMBRADO', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     egreso_cadenaoriginalsat = models.TextField(db_column='EGRESO_CADENAORIGINALSAT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     egreso_sellodigitalsat = models.CharField(db_column='EGRESO_SELLODIGITALSAT', max_length=1000, blank=True, null=True)  # Field name made lowercase.
#     egreso_nocertificadosat = models.CharField(db_column='EGRESO_NOCERTIFICADOSAT', max_length=99, blank=True, null=True)  # Field name made lowercase.
#     cfdi33_cartaporte = models.IntegerField(db_column='CFDI33_CARTAPORTE', blank=True, null=True)  # Field name made lowercase.
#     traslado_cfdi33_tipocomprobante = models.CharField(db_column='TRASLADO_CFDI33_TIPOCOMPROBANTE', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     traslado_cadenaoriginal = models.TextField(db_column='TRASLADO_CADENAORIGINAL', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     traslado_sellodigital = models.CharField(db_column='TRASLADO_SELLODIGITAL', max_length=1000, blank=True, null=True)  # Field name made lowercase.
#     traslado_nocertificado = models.CharField(db_column='TRASLADO_NOCERTIFICADO', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     traslado_foliopac = models.CharField(db_column='TRASLADO_FOLIOPAC', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     traslado_fechacertificacion = models.CharField(db_column='TRASLADO_FECHACERTIFICACION', max_length=24, blank=True, null=True)  # Field name made lowercase.
#     traslado_cfdi33_rfcprovcertificacion = models.CharField(db_column='TRASLADO_CFDI33_RFCPROVCERTIFICACION', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     traslado_cfdi33_versiontimbrado = models.CharField(db_column='TRASLADO_CFDI33_VERSIONTIMBRADO', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     traslado_cadenaoriginalsat = models.TextField(db_column='TRASLADO_CADENAORIGINALSAT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     traslado_sellodigitalsat = models.CharField(db_column='TRASLADO_SELLODIGITALSAT', max_length=1000, blank=True, null=True)  # Field name made lowercase.
#     traslado_nocertificadosat = models.CharField(db_column='TRASLADO_NOCERTIFICADOSAT', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     traslado_estatus = models.CharField(db_column='TRASLADO_ESTATUS', max_length=19, blank=True, null=True)  # Field name made lowercase.
#     egreso_estatus = models.CharField(db_column='EGRESO_ESTATUS', max_length=19, blank=True, null=True)  # Field name made lowercase.
#     cfdi33_cuentapredial = models.CharField(db_column='CFDI33_CUENTAPREDIAL', max_length=154, blank=True, null=True)  # Field name made lowercase.
#     retencion_sello = models.TextField(db_column='RETENCION_SELLO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     retencion_fechacertificacion = models.CharField(db_column='RETENCION_FECHACERTIFICACION', max_length=24, blank=True, null=True)  # Field name made lowercase.
#     retencion_versiontimbrado = models.CharField(db_column='RETENCION_VERSIONTIMBRADO', max_length=54, blank=True, null=True)  # Field name made lowercase.
#     retencion_sellodigitalsat = models.TextField(db_column='RETENCION_SELLODIGITALSAT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     retencion_nocertificadosat = models.CharField(db_column='RETENCION_NOCERTIFICADOSAT', max_length=1000, blank=True, null=True)  # Field name made lowercase.
#     retencion_estado = models.CharField(db_column='RETENCION_ESTADO', max_length=24, blank=True, null=True)  # Field name made lowercase.
#     retencion_fechayhoraemision = models.CharField(db_column='RETENCION_FECHAYHORAEMISION', max_length=34, blank=True, null=True)  # Field name made lowercase.
#     retencion_monttotpago = models.DecimalField(db_column='RETENCION_MONTTOTPAGO', max_digits=17, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     retencion_monttotpagograv = models.DecimalField(db_column='RETENCION_MONTTOTPAGOGRAV', max_digits=17, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     retencion_monttotpagoexent = models.DecimalField(db_column='RETENCION_MONTTOTPAGOEXENT', max_digits=17, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     cfdi33_egreso_fechayhoraemision = models.CharField(db_column='CFDI33_EGRESO_FECHAYHORAEMISION', max_length=24, blank=True, null=True)  # Field name made lowercase.
#     retencion_montototret = models.DecimalField(db_column='RETENCION_MONTOTOTRET', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     retencion_impretenidos_montoret = models.DecimalField(db_column='RETENCION_IMPRETENIDOS_MONTORET', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     retencion_impretenidos_impuesto = models.CharField(db_column='RETENCION_IMPRETENIDOS_IMPUESTO', max_length=19, blank=True, null=True)  # Field name made lowercase.
#     retenciones_descretenc = models.DecimalField(db_column='RETENCIONES_DESCRETENC', max_digits=17, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     traslado_cfdi33_fechayhoraemision = models.CharField(db_column='TRASLADO_CFDI33_FECHAYHORAEMISION', max_length=24, blank=True, null=True)  # Field name made lowercase.
#     comercioexterior_activo = models.IntegerField(db_column='COMERCIOEXTERIOR_ACTIVO', blank=True, null=True)  # Field name made lowercase.
#     aplica_anticipos_cfdi33 = models.IntegerField(db_column='APLICA_ANTICIPOS_CFDI33', blank=True, null=True)  # Field name made lowercase.
#     cancelstatus_cfdi33 = models.CharField(db_column='CANCELSTATUS_CFDI33', max_length=99, blank=True, null=True)  # Field name made lowercase.
#     iscancelable_cfdi33 = models.CharField(db_column='ISCANCELABLE_CFDI33', max_length=99, blank=True, null=True)  # Field name made lowercase.
#     tiporelacioncfdi33 = models.CharField(db_column='TIPORELACIONCFDI33', max_length=4, blank=True, null=True)  # Field name made lowercase.
#     ine_activo = models.IntegerField(db_column='INE_ACTIVO', blank=True, null=True)  # Field name made lowercase.
#     tipoproceso = models.CharField(db_column='TIPOPROCESO', max_length=29, blank=True, null=True)  # Field name made lowercase.
#     tipocomite = models.CharField(db_column='TIPOCOMITE', max_length=29, blank=True, null=True)  # Field name made lowercase.
#     idcontabilidad = models.CharField(db_column='IDCONTABILIDAD', max_length=29, blank=True, null=True)  # Field name made lowercase.
#     exportacion = models.CharField(db_column='EXPORTACION', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     infoglo_periodicidad = models.CharField(db_column='INFOGLO_PERIODICIDAD', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     infoglo_meses = models.CharField(db_column='INFOGLO_MESES', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     infoglo_anio = models.CharField(db_column='INFOGLO_ANIO', max_length=4, blank=True, null=True)  # Field name made lowercase.
#     motivo_cancelacion = models.CharField(db_column='Motivo_Cancelacion', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     folio_cancelacion = models.CharField(db_column='Folio_Cancelacion', max_length=99, blank=True, null=True)  # Field name made lowercase.
#     cfdi4_tipopagoret = models.CharField(db_column='CFDI4_TIPOPAGORET', max_length=4, blank=True, null=True)  # Field name made lowercase.
#     ret_motivo_cancelacion = models.CharField(db_column='RET_MOTIVO_CANCELACION', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     ret_folio_cancelacion = models.CharField(db_column='RET_FOLIO_CANCELACION', max_length=99, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'factfactura'


# class Factpagos(models.Model):
#     numero = models.IntegerField(db_column='NUMERO', primary_key=True)  # Field name made lowercase.
#     cliente = models.CharField(db_column='CLIENTE', max_length=9, blank=True, null=True)  # Field name made lowercase.
#     usuario = models.CharField(db_column='USUARIO', max_length=6, blank=True, null=True)  # Field name made lowercase.
#     fecha = models.IntegerField(db_column='FECHA', blank=True, null=True)  # Field name made lowercase.
#     hora = models.IntegerField(db_column='HORA', blank=True, null=True)  # Field name made lowercase.
#     importe = models.DecimalField(db_column='IMPORTE', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     referencia = models.CharField(db_column='REFERENCIA', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     observaciones = models.CharField(db_column='OBSERVACIONES', max_length=999, blank=True, null=True)  # Field name made lowercase.
#     estado = models.CharField(db_column='ESTADO', max_length=19, blank=True, null=True)  # Field name made lowercase.
#     aplicado = models.SmallIntegerField(db_column='APLICADO', blank=True, null=True)  # Field name made lowercase.
#     importedolares = models.DecimalField(db_column='IMPORTEDOLARES', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     moneda = models.CharField(db_column='MONEDA', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     tipocambio = models.DecimalField(db_column='TIPOCAMBIO', max_digits=11, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     importereal = models.DecimalField(db_column='IMPORTEREAL', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     banco = models.CharField(db_column='BANCO', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     cadenaoriginal = models.TextField(db_column='CADENAORIGINAL', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sellodigital = models.CharField(db_column='SELLODIGITAL', max_length=1000, blank=True, null=True)  # Field name made lowercase.
#     sellodigitalsat = models.CharField(db_column='SELLODIGITALSAT', max_length=1000, blank=True, null=True)  # Field name made lowercase.
#     nocertificado = models.CharField(db_column='NOCERTIFICADO', max_length=80, blank=True, null=True)  # Field name made lowercase.
#     nocertificadosat = models.CharField(db_column='NOCERTIFICADOSAT', max_length=80, blank=True, null=True)  # Field name made lowercase.
#     foliopac = models.CharField(db_column='FOLIOPAC', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     fechacertificacion = models.CharField(db_column='FECHACERTIFICACION', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     cfdi33_rfcprovcertificacion = models.CharField(db_column='CFDI33_RFCPROVCERTIFICACION', max_length=51, blank=True, null=True)  # Field name made lowercase.
#     cfdi33_versiontimbrado = models.CharField(db_column='CFDI33_VERSIONTIMBRADO', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     cadenaoriginalsat = models.TextField(db_column='CADENAORIGINALSAT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     cfdi33_emisorregimenfiscal = models.CharField(db_column='CFDI33_EMISORREGIMENFISCAL', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     cfdi33_emisorregimenfiscaldescripcion = models.CharField(db_column='CFDI33_EMISORREGIMENFISCALDESCRIPCION', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     cfdi33_receptor_usocfdi = models.CharField(db_column='CFDI33_RECEPTOR_USOCFDI', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     cfdi33_receptor_usocfdidescripcion = models.CharField(db_column='CFDI33_RECEPTOR_USOCFDIDESCRIPCION', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     cfdi33_generada = models.IntegerField(db_column='CFDI33_GENERADA', blank=True, null=True)  # Field name made lowercase.
#     cfdi33_formapago = models.CharField(db_column='CFDI33_FORMAPAGO', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     cfdi33_formapagodescripcion = models.CharField(db_column='CFDI33_FORMAPAGODESCRIPCION', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     cfdi33_tipocomprobante = models.CharField(db_column='CFDI33_TIPOCOMPROBANTE', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     cfdi33_fechayhoraemision = models.CharField(db_column='CFDI33_FECHAYHORAEMISION', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     cfdi33_residenciafiscal = models.CharField(db_column='CFDI33_RESIDENCIAFISCAL', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     cfdi33_residenciafiscaldescripcion = models.CharField(db_column='CFDI33_RESIDENCIAFISCALDESCRIPCION', max_length=250, blank=True, null=True)  # Field name made lowercase.
#     cfdi33_numregidtrib = models.CharField(db_column='CFDI33_NUMREGIDTRIB', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     cep_tipopago = models.CharField(db_column='CEP_TIPOPAGO', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     cep_fechapago = models.CharField(db_column='CEP_FECHAPAGO', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     cep_rfcemisorctaord = models.CharField(db_column='CEP_RFCEMISORCTAORD', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     cep_tipocadpago = models.CharField(db_column='CEP_TIPOCADPAGO', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     cep_certificadopago = models.TextField(db_column='CEP_CERTIFICADOPAGO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     cep_cadpago = models.TextField(db_column='CEP_CADPAGO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     cep_sellopago = models.TextField(db_column='CEP_SELLOPAGO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     cep_bancoemisor = models.CharField(db_column='CEP_BANCOEMISOR', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     cep_ctaordenanteemisor = models.CharField(db_column='CEP_CTAORDENANTEEMISOR', max_length=19, blank=True, null=True)  # Field name made lowercase.
#     cep_nombrebancoemisor = models.CharField(db_column='CEP_NOMBREBANCOEMISOR', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     cep_bancoreceptor = models.CharField(db_column='CEP_BANCORECEPTOR', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     cep_rfcreceptorctaord = models.CharField(db_column='CEP_RFCRECEPTORCTAORD', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     cep_ctaordenantereceptor = models.CharField(db_column='CEP_CTAORDENANTERECEPTOR', max_length=19, blank=True, null=True)  # Field name made lowercase.
#     cep_nombrebancoreceptor = models.CharField(db_column='CEP_NOMBREBANCORECEPTOR', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     factura = models.CharField(db_column='FACTURA', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     cfdi33_metodopago = models.CharField(db_column='CFDI33_METODOPAGO', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     cfdi33_metodopagodescripcion = models.CharField(db_column='CFDI33_METODOPAGODESCRIPCION', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     cfdi33_uso = models.CharField(db_column='CFDI33_USO', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     cfdi33_usodescripcion = models.CharField(db_column='CFDI33_USODESCRIPCION', max_length=249, blank=True, null=True)  # Field name made lowercase.
#     clientenombre = models.CharField(db_column='CLIENTENOMBRE', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     linea = models.IntegerField(db_column='LINEA', blank=True, null=True)  # Field name made lowercase.
#     saldo = models.DecimalField(db_column='SALDO', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     cfdi33_receptorrfc = models.CharField(db_column='CFDI33_RECEPTORRFC', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     cfdi33_receptorpais = models.CharField(db_column='CFDI33_RECEPTORPAIS', max_length=55, blank=True, null=True)  # Field name made lowercase.
#     cfdi33_emisornombre = models.CharField(db_column='CFDI33_EMISORNOMBRE', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     cfdi33_emisorrfc = models.CharField(db_column='CFDI33_EMISORRFC', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     cfdi33_emisorcp = models.CharField(db_column='CFDI33_EMISORCP', max_length=9, blank=True, null=True)  # Field name made lowercase.
#     cfdi33_serie = models.CharField(db_column='CFDI33_SERIE', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     cfdi33_folio = models.CharField(db_column='CFDI33_FOLIO', max_length=45, blank=True, null=True)  # Field name made lowercase.
#     cep_monto = models.DecimalField(db_column='CEP_MONTO', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     cep_ruta = models.CharField(db_column='CEP_RUTA', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     saldo_anterior = models.DecimalField(db_column='SALDO_ANTERIOR', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     importereal_dll = models.DecimalField(db_column='IMPORTEREAL_DLL', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     saldo_dolares = models.DecimalField(db_column='SALDO_DOLARES', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     saldo_anterior_dolares = models.DecimalField(db_column='SALDO_ANTERIOR_DOLARES', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     fechacomplemento = models.CharField(db_column='FECHACOMPLEMENTO', max_length=254, blank=True, null=True)  # Field name made lowercase.
#     fechacomplementoint = models.IntegerField(db_column='FECHACOMPLEMENTOINT', blank=True, null=True)  # Field name made lowercase.
#     horacomplemento = models.IntegerField(db_column='HORACOMPLEMENTO', blank=True, null=True)  # Field name made lowercase.
#     cancelstatus_cfdi33 = models.CharField(db_column='CANCELSTATUS_CFDI33', max_length=99, blank=True, null=True)  # Field name made lowercase.
#     iscancelable_cfdi33 = models.CharField(db_column='ISCANCELABLE_CFDI33', max_length=99, blank=True, null=True)  # Field name made lowercase.
#     tiporelacioncfdi = models.CharField(db_column='TIPORELACIONCFDI', max_length=4, blank=True, null=True)  # Field name made lowercase.
#     ret_impuestop = models.CharField(db_column='RET_IMPUESTOP', max_length=4, blank=True, null=True)  # Field name made lowercase.
#     ret_importep = models.DecimalField(db_column='RET_IMPORTEP', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     tras_basep = models.DecimalField(db_column='TRAS_BASEP', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     tras_impuestop = models.CharField(db_column='TRAS_IMPUESTOP', max_length=4, blank=True, null=True)  # Field name made lowercase.
#     tras_tipofactorp = models.CharField(db_column='TRAS_TIPOFACTORP', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     tras_tasaocuotap = models.DecimalField(db_column='TRAS_TASAOCUOTAP', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     tras_importep = models.DecimalField(db_column='TRAS_IMPORTEP', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     motivo_cancelacion = models.CharField(db_column='Motivo_Cancelacion', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     folio_cancelacion = models.CharField(db_column='Folio_Cancelacion', max_length=99, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'factpagos'



# class Items(models.Model):
#     clave = models.CharField(db_column='CLAVE', primary_key=True, max_length=39)  # Field name made lowercase.
#     descripcion = models.CharField(db_column='DESCRIPCION', max_length=1999, blank=True, null=True)  # Field name made lowercase.
#     precioa = models.DecimalField(db_column='PRECIOA', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     preciob = models.DecimalField(db_column='PRECIOB', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     precioc = models.DecimalField(db_column='PRECIOC', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     moneda = models.CharField(db_column='MONEDA', max_length=7, blank=True, null=True)  # Field name made lowercase.
#     tipo = models.CharField(db_column='TIPO', max_length=8, blank=True, null=True)  # Field name made lowercase.
#     costo = models.DecimalField(db_column='COSTO', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     factora = models.DecimalField(db_column='FACTORA', max_digits=9, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     factorb = models.DecimalField(db_column='FACTORB', max_digits=7, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     factorc = models.DecimalField(db_column='FACTORC', max_digits=7, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     proveedor = models.CharField(db_column='PROVEEDOR', max_length=9, blank=True, null=True)  # Field name made lowercase.
#     familia = models.CharField(db_column='FAMILIA', max_length=19, blank=True, null=True)  # Field name made lowercase.
#     fechacosto = models.IntegerField(db_column='FECHACOSTO', blank=True, null=True)  # Field name made lowercase.
#     unidadmedida = models.CharField(db_column='UNIDADMEDIDA', max_length=4, blank=True, null=True)  # Field name made lowercase.
#     ultimocosto = models.DecimalField(db_column='ULTIMOCOSTO', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     descripcioning = models.CharField(db_column='DESCRIPCIONING', max_length=1999, blank=True, null=True)  # Field name made lowercase.
#     cantidad_existencia = models.DecimalField(db_column='CANTIDAD_EXISTENCIA', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     aplicaretencionflete = models.SmallIntegerField(db_column='APLICARETENCIONFLETE', blank=True, null=True)  # Field name made lowercase.
#     aplicaiva = models.SmallIntegerField(db_column='APLICAIVA', blank=True, null=True)  # Field name made lowercase.
#     aplicaretencioniva = models.SmallIntegerField(db_column='APLICARETENCIONIVA', blank=True, null=True)  # Field name made lowercase.
#     minimoinventario = models.DecimalField(db_column='MINIMOINVENTARIO', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     maximoinventario = models.DecimalField(db_column='MAXIMOINVENTARIO', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
#     articulocompuesto = models.SmallIntegerField(db_column='ARTICULOCOMPUESTO', blank=True, null=True)  # Field name made lowercase.
#     fechaultimocosto = models.IntegerField(db_column='FECHAULTIMOCOSTO', blank=True, null=True)  # Field name made lowercase.
#     articulo_presupuesto = models.SmallIntegerField(db_column='ARTICULO_PRESUPUESTO', blank=True, null=True)  # Field name made lowercase.
#     tiposervicio = models.CharField(db_column='TIPOSERVICIO', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     tipoproducto = models.CharField(db_column='TIPOPRODUCTO', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     descripcioncorta = models.CharField(db_column='DESCRIPCIONCORTA', max_length=249, blank=True, null=True)  # Field name made lowercase.
#     localidad = models.CharField(db_column='LOCALIDAD', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     ic_tipocuenta = models.CharField(db_column='IC_TIPOCUENTA', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     ic_cuenta = models.CharField(db_column='IC_CUENTA', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     aplicaivaxcobrar = models.SmallIntegerField(db_column='APLICAIVAXCOBRAR', blank=True, null=True)  # Field name made lowercase.
#     retieneisr = models.SmallIntegerField(db_column='RETIENEISR', blank=True, null=True)  # Field name made lowercase.
#     cfdi33_claveprodserv = models.CharField(db_column='CFDI33_CLAVEPRODSERV', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     cfdi33_claveprodservdescripcion = models.CharField(db_column='CFDI33_CLAVEPRODSERVDESCRIPCION', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     cfdi33_claveunidad = models.CharField(db_column='CFDI33_CLAVEUNIDAD', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     cfdi33_claveunidaddescripcion = models.CharField(db_column='CFDI33_CLAVEUNIDADDESCRIPCION', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     cfdi33_iva_retenido = models.IntegerField(db_column='CFDI33_IVA_RETENIDO', blank=True, null=True)  # Field name made lowercase.
#     tipoconcepto_cfd33 = models.CharField(db_column='TIPOCONCEPTO_CFD33', max_length=1, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'items'



# class Tipocambio(models.Model):
#     fecha = models.IntegerField(db_column='FECHA', primary_key=True)  # Field name made lowercase.
#     tipocambio = models.DecimalField(db_column='TIPOCAMBIO', max_digits=9, decimal_places=6, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'tipocambio'



# class Unidadmedida(models.Model):
#     clave = models.CharField(db_column='CLAVE', primary_key=True, max_length=14)  # Field name made lowercase.
#     descripcion = models.CharField(db_column='DESCRIPCION', max_length=19, blank=True, null=True)  # Field name made lowercase.
#     cfdi33_unidad = models.CharField(db_column='CFDI33_UNIDAD', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     cfdi33_unidaddescripcion = models.CharField(db_column='CFDI33_UNIDADDESCRIPCION', max_length=500, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'unidadmedida'

