from django.db import models


class FactFactura(models.Model):
    consecutivo = models.IntegerField(db_column='CONSECUTIVO', primary_key=True)  # Field name made lowercase.
    factura = models.CharField(db_column='FACTURA', unique=True, max_length=14, blank=True, null=True)  # Field name made lowercase.
    cliente = models.CharField(db_column='CLIENTE', max_length=9, blank=True, null=True)  # Field name made lowercase.
    fecha = models.IntegerField(db_column='FECHA', blank=True, null=True)  # Field name made lowercase.
    tipocambio = models.DecimalField(db_column='TIPOCAMBIO', max_digits=9, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    estatus = models.CharField(db_column='ESTATUS', max_length=14, blank=True, null=True)  # Field name made lowercase.
    # ordencompra = models.CharField(db_column='ORDENCOMPRA', max_length=12, blank=True, null=True)  # Field name made lowercase.
    moneda = models.CharField(db_column='MONEDA', max_length=7, blank=True, null=True)  # Field name made lowercase.
    condicionpago = models.CharField(db_column='CONDICIONPAGO', max_length=59, blank=True, null=True)  # Field name made lowercase.
    operador = models.CharField(db_column='OPERADOR', max_length=6, blank=True, null=True)  # Field name made lowercase.
    # contacto = models.CharField(db_column='CONTACTO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    # comentario = models.CharField(db_column='COMENTARIO', max_length=40, blank=True, null=True)  # Field name made lowercase.
    porcentajeiva = models.DecimalField(db_column='PORCENTAJEIVA', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    descuento = models.DecimalField(db_column='DESCUENTO', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    subtotal = models.DecimalField(db_column='SUBTOTAL', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    flete = models.DecimalField(db_column='FLETE', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    iva = models.DecimalField(db_column='IVA', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    valorpagado = models.DecimalField(db_column='VALORPAGADO', max_digits=17, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    total = models.DecimalField(db_column='TOTAL', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    saldo = models.DecimalField(db_column='SALDO', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    # ticket = models.CharField(db_column='TICKET', max_length=12, blank=True, null=True)  # Field name made lowercase.
    # cotizacion = models.CharField(db_column='COTIZACION', max_length=12, blank=True, null=True)  # Field name made lowercase.
    # lineacotizacion = models.IntegerField(db_column='LINEACOTIZACION', blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='OBSERVACIONES', max_length=999, blank=True, null=True)  # Field name made lowercase.
    # fechaembargue = models.IntegerField(db_column='FECHAEMBARGUE', blank=True, null=True)  # Field name made lowercase.
    # viaembargue = models.CharField(db_column='VIAEMBARGUE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    # lab = models.CharField(db_column='LAB', max_length=49, blank=True, null=True)  # Field name made lowercase.
    # embarcarcliente = models.CharField(db_column='EMBARCARCLIENTE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    # aplicadescuento = models.SmallIntegerField(db_column='APLICADESCUENTO', blank=True, null=True)  # Field name made lowercase.
    porcentajedescuento = models.DecimalField(db_column='PORCENTAJEDESCUENTO', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    descuentodolares = models.DecimalField(db_column='DESCUENTODOLARES', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    ivadolares = models.DecimalField(db_column='IVADOLARES', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    subtotaldolares = models.DecimalField(db_column='SUBTOTALDOLARES', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    fletedolares = models.DecimalField(db_column='FLETEDOLARES', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    valorpagadodolares = models.DecimalField(db_column='VALORPAGADODOLARES', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    totaldolares = models.DecimalField(db_column='TOTALDOLARES', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    saldodolares = models.DecimalField(db_column='SALDODOLARES', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    pago = models.CharField(db_column='PAGO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    programada = models.CharField(db_column='PROGRAMADA', max_length=20, blank=True, null=True)  # Field name made lowercase.
    # vendedor = models.CharField(db_column='VENDEDOR', max_length=6, blank=True, null=True)  # Field name made lowercase.
    # inventariado = models.SmallIntegerField(db_column='INVENTARIADO', blank=True, null=True)  # Field name made lowercase.
    anticipo = models.DecimalField(db_column='ANTICIPO', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    anticipodolares = models.DecimalField(db_column='ANTICIPODOLARES', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    retencioniva = models.DecimalField(db_column='RETENCIONIVA', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    retencionpesos = models.DecimalField(db_column='RETENCIONPESOS', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    retenciondolares = models.DecimalField(db_column='RETENCIONDOLARES', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    # otrosgastos = models.DecimalField(db_column='OTROSGASTOS', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    hora = models.IntegerField(db_column='HORA', blank=True, null=True)  # Field name made lowercase.
    # comision = models.DecimalField(db_column='COMISION', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    # comisiondolares = models.DecimalField(db_column='COMISIONDOLARES', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    empresa = models.CharField(db_column='EMPRESA', max_length=14, blank=True, null=True)  # Field name made lowercase.
    # notascredito = models.CharField(db_column='NOTASCREDITO', max_length=49, blank=True, null=True)  # Field name made lowercase.
    porcentajeretencioniva = models.DecimalField(db_column='PORCENTAJERETENCIONIVA', max_digits=9, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    retencionivapesos = models.DecimalField(db_column='RETENCIONIVAPESOS', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    retencionivadolares = models.DecimalField(db_column='RETENCIONIVADOLARES', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    porcentajeretencionisr = models.DecimalField(db_column='PORCENTAJERETENCIONISR', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    retencionisrpesos = models.DecimalField(db_column='RETENCIONISRPESOS', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    retencionisrdolares = models.DecimalField(db_column='RETENCIONISRDOLARES', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    aplicaretencioniva = models.SmallIntegerField(db_column='APLICARETENCIONIVA', blank=True, null=True)  # Field name made lowercase.
    aplicaretencionisr = models.SmallIntegerField(db_column='APLICARETENCIONISR', blank=True, null=True)  # Field name made lowercase.
    # isfacturaelectronica = models.SmallIntegerField(db_column='ISFACTURAELECTRONICA', blank=True, null=True)  # Field name made lowercase.
    sellodigital = models.CharField(db_column='SELLODIGITAL', max_length=999, blank=True, null=True)  # Field name made lowercase.
    cadenaoriginal = models.TextField(db_column='CADENAORIGINAL', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    foliopac = models.CharField(db_column='FOLIOPAC', max_length=99, blank=True, null=True)  # Field name made lowercase.
    # fetype = models.CharField(db_column='FETYPE', max_length=9, blank=True, null=True)  # Field name made lowercase.
    # noaprovacion = models.CharField(db_column='NOAPROVACION', max_length=29, blank=True, null=True)  # Field name made lowercase.
    # anioaprovacion = models.CharField(db_column='ANIOAPROVACION', max_length=19, blank=True, null=True)  # Field name made lowercase.
    seriecfd = models.CharField(db_column='SERIECFD', max_length=29, blank=True, null=True)  # Field name made lowercase.
    # sellopac = models.TextField(db_column='SELLOPAC', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    nocertificado = models.CharField(db_column='NOCERTIFICADO', max_length=59, blank=True, null=True)  # Field name made lowercase.
    nocertificadosat = models.CharField(db_column='NOCERTIFICADOSAT', max_length=79, blank=True, null=True)  # Field name made lowercase.
    fechacertificacion = models.CharField(db_column='FECHACERTIFICACION', max_length=24, blank=True, null=True)  # Field name made lowercase.
    fechacertificacionsistema = models.IntegerField(db_column='FECHACERTIFICACIONSISTEMA', blank=True, null=True)  # Field name made lowercase.
    # cartaporte = models.IntegerField(db_column='CARTAPORTE', blank=True, null=True)  # Field name made lowercase.
    # clientedestino = models.CharField(db_column='CLIENTEDESTINO', max_length=9, blank=True, null=True)  # Field name made lowercase.
    # destino = models.CharField(db_column='DESTINO', max_length=44, blank=True, null=True)  # Field name made lowercase.
    # origen = models.CharField(db_column='ORIGEN', max_length=44, blank=True, null=True)  # Field name made lowercase.
    # recogeren = models.CharField(db_column='RECOGEREN', max_length=44, blank=True, null=True)  # Field name made lowercase.
    # entregaraen = models.CharField(db_column='ENTREGARAEN', max_length=44, blank=True, null=True)  # Field name made lowercase.
    # sellocartaporte = models.CharField(db_column='SELLOCARTAPORTE', max_length=19, blank=True, null=True)  # Field name made lowercase.
    # operadorcartaporte = models.CharField(db_column='OPERADORCARTAPORTE', max_length=79, blank=True, null=True)  # Field name made lowercase.
    sellodigitalsat = models.CharField(db_column='SELLODIGITALSAT', max_length=999, blank=True, null=True)  # Field name made lowercase.
    cadenaoriginalsat = models.TextField(db_column='CADENAORIGINALSAT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    emisor_nombre = models.CharField(db_column='EMISOR_NOMBRE', max_length=199, blank=True, null=True)  # Field name made lowercase.
    emisor_direccion = models.CharField(db_column='EMISOR_DIRECCION', max_length=199, blank=True, null=True)  # Field name made lowercase.
    emisor_colonia = models.CharField(db_column='EMISOR_COLONIA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    emisor_cp = models.CharField(db_column='EMISOR_CP', max_length=14, blank=True, null=True)  # Field name made lowercase.
    emisor_estado = models.CharField(db_column='EMISOR_ESTADO', max_length=19, blank=True, null=True)  # Field name made lowercase.
    emisor_pais = models.CharField(db_column='EMISOR_PAIS', max_length=24, blank=True, null=True)  # Field name made lowercase.
    emisor_rfc = models.CharField(db_column='EMISOR_RFC', max_length=19, blank=True, null=True)  # Field name made lowercase.
    emisor_numeroext = models.CharField(db_column='EMISOR_NUMEROEXT', max_length=24, blank=True, null=True)  # Field name made lowercase.
    emisor_ciudad = models.CharField(db_column='EMISOR_CIUDAD', max_length=19, blank=True, null=True)  # Field name made lowercase.
    
    receptor_nombre = models.CharField(db_column='RECEPTOR_NOMBRE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    receptor_direccion = models.CharField(db_column='RECEPTOR_DIRECCION', max_length=250, blank=True, null=True)  # Field name made lowercase.
    receptor_ciudad = models.CharField(db_column='RECEPTOR_CIUDAD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    receptor_estado = models.CharField(db_column='RECEPTOR_ESTADO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    receptor_cp = models.CharField(db_column='RECEPTOR_CP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    receptor_pais = models.CharField(db_column='RECEPTOR_PAIS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    receptor_numeroext = models.CharField(db_column='RECEPTOR_NUMEROEXT', max_length=19, blank=True, null=True)  # Field name made lowercase.
    receptor_colonia = models.CharField(db_column='RECEPTOR_COLONIA', max_length=100, blank=True, null=True)  # Field name made lowercase.
    receptor_rfc = models.CharField(db_column='RECEPTOR_RFC', max_length=20, blank=True, null=True)  # Field name made lowercase.
    
    facturaexpedida = models.CharField(db_column='FACTURAEXPEDIDA', max_length=299, blank=True, null=True)  # Field name made lowercase.
    # istransferencia = models.SmallIntegerField(db_column='ISTRANSFERENCIA', blank=True, null=True)  # Field name made lowercase.
    # numctapago = models.CharField(db_column='NUMCTAPAGO', max_length=4, blank=True, null=True)  # Field name made lowercase.
    # observaciones2 = models.TextField(db_column='OBSERVACIONES2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    # proyecto = models.CharField(db_column='PROYECTO', max_length=24, blank=True, null=True)  # Field name made lowercase.
    # c1 = models.CharField(db_column='C1', max_length=254, blank=True, null=True)  # Field name made lowercase.
    # c2 = models.CharField(db_column='C2', max_length=254, blank=True, null=True)  # Field name made lowercase.
    # c3 = models.CharField(db_column='C3', max_length=254, blank=True, null=True)  # Field name made lowercase.
    # c4 = models.CharField(db_column='C4', max_length=254, blank=True, null=True)  # Field name made lowercase.
    # c5 = models.CharField(db_column='C5', max_length=254, blank=True, null=True)  # Field name made lowercase.
    # c6 = models.CharField(db_column='C6', max_length=254, blank=True, null=True)  # Field name made lowercase.
    # c7 = models.CharField(db_column='C7', max_length=254, blank=True, null=True)  # Field name made lowercase.
    # c8 = models.CharField(db_column='C8', max_length=254, blank=True, null=True)  # Field name made lowercase.
    # c9 = models.CharField(db_column='C9', max_length=254, blank=True, null=True)  # Field name made lowercase.
    # c10 = models.CharField(db_column='C10', max_length=254, blank=True, null=True)  # Field name made lowercase.
    # c11 = models.CharField(db_column='C11', max_length=254, blank=True, null=True)  # Field name made lowercase.
    # c12 = models.CharField(db_column='C12', max_length=254, blank=True, null=True)  # Field name made lowercase.
    # c13 = models.CharField(db_column='C13', max_length=254, blank=True, null=True)  # Field name made lowercase.
    # c14 = models.CharField(db_column='C14', max_length=254, blank=True, null=True)  # Field name made lowercase.
    # c15 = models.CharField(db_column='C15', max_length=254, blank=True, null=True)  # Field name made lowercase.
    # c16 = models.CharField(db_column='C16', max_length=255, blank=True, null=True)  # Field name made lowercase.
    # c17 = models.CharField(db_column='C17', max_length=255, blank=True, null=True)  # Field name made lowercase.
    # c18 = models.CharField(db_column='C18', max_length=255, blank=True, null=True)  # Field name made lowercase.
    # c19 = models.CharField(db_column='C19', max_length=255, blank=True, null=True)  # Field name made lowercase.
    # c20 = models.CharField(db_column='C20', max_length=255, blank=True, null=True)  # Field name made lowercase.
    # otros_cartaporte = models.DecimalField(db_column='OTROS_CARTAPORTE', max_digits=13, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    # emisor_nointerior = models.TextField(db_column='EMISOR_NOINTERIOR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    # receptor_nointerior = models.TextField(db_column='RECEPTOR_NOINTERIOR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    # reembarco = models.CharField(db_column='REEMBARCO', max_length=119, blank=True, null=True)  # Field name made lowercase.
    # reembarcarcecon = models.CharField(db_column='REEMBARCARCECON', max_length=119, blank=True, null=True)  # Field name made lowercase.
    # condujo = models.CharField(db_column='CONDUJO', max_length=149, blank=True, null=True)  # Field name made lowercase.
    # conducira = models.CharField(db_column='CONDUCIRA', max_length=149, blank=True, null=True)  # Field name made lowercase.
    # de1 = models.CharField(db_column='DE1', max_length=99, blank=True, null=True)  # Field name made lowercase.
    # de2 = models.CharField(db_column='DE2', max_length=99, blank=True, null=True)  # Field name made lowercase.
    # a1 = models.CharField(db_column='A1', max_length=119, blank=True, null=True)  # Field name made lowercase.
    # a2 = models.CharField(db_column='A2', max_length=119, blank=True, null=True)  # Field name made lowercase.
    # documento = models.CharField(db_column='DOCUMENTO', max_length=39, blank=True, null=True)  # Field name made lowercase.
    # notractor = models.CharField(db_column='NOTRACTOR', max_length=19, blank=True, null=True)  # Field name made lowercase.
    # remolque = models.CharField(db_column='REMOLQUE', max_length=24, blank=True, null=True)  # Field name made lowercase.
    # valoragregado = models.CharField(db_column='VALORAGREGADO', max_length=14, blank=True, null=True)  # Field name made lowercase.
    # porcentajeinterespagare = models.IntegerField(db_column='PORCENTAJEINTERESPAGARE', blank=True, null=True)  # Field name made lowercase.
    # complementoiva = models.SmallIntegerField(db_column='COMPLEMENTOIVA', blank=True, null=True)  # Field name made lowercase.
    addcomplementonotario = models.SmallIntegerField(db_column='ADDCOMPLEMENTONOTARIO', blank=True, null=True)  # Field name made lowercase.
    inmueble_tipo = models.CharField(db_column='INMUEBLE_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    inmueble_calle = models.CharField(db_column='INMUEBLE_CALLE', max_length=150, blank=True, null=True)  # Field name made lowercase.
    inmueble_noexterior = models.CharField(db_column='INMUEBLE_NOEXTERIOR', max_length=55, blank=True, null=True)  # Field name made lowercase.
    inmueble_nointerior = models.CharField(db_column='INMUEBLE_NOINTERIOR', max_length=30, blank=True, null=True)  # Field name made lowercase.
    inmueble_colonia = models.CharField(db_column='INMUEBLE_COLONIA', max_length=100, blank=True, null=True)  # Field name made lowercase.
    inmueble_localidad = models.CharField(db_column='INMUEBLE_LOCALIDAD', max_length=100, blank=True, null=True)  # Field name made lowercase.
    inmueble_referencia = models.CharField(db_column='INMUEBLE_REFERENCIA', max_length=100, blank=True, null=True)  # Field name made lowercase.
    inmueble_municipio = models.CharField(db_column='INMUEBLE_MUNICIPIO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    inmueble_estado = models.CharField(db_column='INMUEBLE_ESTADO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    inmueble_pais = models.CharField(db_column='INMUEBLE_PAIS', max_length=3, blank=True, null=True)  # Field name made lowercase.
    inmueble_codigopostal = models.CharField(db_column='INMUEBLE_CODIGOPOSTAL', max_length=5, blank=True, null=True)  # Field name made lowercase.
    operacion_numinstrumentonotarial = models.IntegerField(db_column='OPERACION_NUMINSTRUMENTONOTARIAL', blank=True, null=True)  # Field name made lowercase.
    operacion_fechainstnotarial = models.IntegerField(db_column='OPERACION_FECHAINSTNOTARIAL', blank=True, null=True)  # Field name made lowercase.
    operacion_montooperacion = models.DecimalField(db_column='OPERACION_MONTOOPERACION', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    operacion_subtotal = models.DecimalField(db_column='OPERACION_SUBTOTAL', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    operacion_iva = models.DecimalField(db_column='OPERACION_IVA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    notario_curp = models.CharField(db_column='NOTARIO_CURP', max_length=19, blank=True, null=True)  # Field name made lowercase.
    notario_numnotaria = models.IntegerField(db_column='NOTARIO_NUMNOTARIA', blank=True, null=True)  # Field name made lowercase.
    notario_entidadfederativa = models.CharField(db_column='NOTARIO_ENTIDADFEDERATIVA', max_length=2, blank=True, null=True)  # Field name made lowercase.
    notaria_adscripcion = models.CharField(db_column='NOTARIA_ADSCRIPCION', max_length=255, blank=True, null=True)  # Field name made lowercase.
    enajenante_coprosocconyugale = models.CharField(db_column='ENAJENANTE_COPROSOCCONYUGALE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    adquiriente_coprosocconyugale = models.CharField(db_column='ADQUIRIENTE_COPROSOCCONYUGALE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    emitirdestinatarioencartaporte = models.SmallIntegerField(db_column='EMITIRDESTINATARIOENCARTAPORTE', blank=True, null=True)  # Field name made lowercase.
    confsendemail = models.CharField(db_column='CONFSENDEMAIL', max_length=19, blank=True, null=True)  # Field name made lowercase.
    fechasendemail = models.IntegerField(db_column='FECHASENDEMAIL', blank=True, null=True)  # Field name made lowercase.
    cc = models.CharField(db_column='CC', max_length=2, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(db_column='VERSION', max_length=4, blank=True, null=True)  # Field name made lowercase.
    pagprovefecporfiduc = models.DecimalField(db_column='PAGPROVEFECPORFIDUC', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    rendimfideicom = models.DecimalField(db_column='RENDIMFIDEICOM', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    deducccorresp = models.DecimalField(db_column='DEDUCCCORRESP', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    monttotret = models.DecimalField(db_column='MONTTOTRET', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    montresfiscdistfibras = models.DecimalField(db_column='MONTRESFISCDISTFIBRAS', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    montotrosconceptdistr = models.DecimalField(db_column='MONTOTROSCONCEPTDISTR', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    descrmontotrosconceptdistr = models.CharField(db_column='DESCRMONTOTROSCONCEPTDISTR', max_length=499, blank=True, null=True)  # Field name made lowercase.
    esbenefefectdelcobro = models.CharField(db_column='ESBENEFEFECTDELCOBRO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    paisderesidparaefecfisc = models.CharField(db_column='PAISDERESIDPARAEFECFISC', max_length=3, blank=True, null=True)  # Field name made lowercase.
    conceptopago_nobeneficiario = models.IntegerField(db_column='CONCEPTOPAGO_NOBENEFICIARIO', blank=True, null=True)  # Field name made lowercase.
    descripcionconcepto_nobeneficiario = models.CharField(db_column='DESCRIPCIONCONCEPTO_NOBENEFICIARIO', max_length=254, blank=True, null=True)  # Field name made lowercase.
    rfc = models.CharField(db_column='RFC', max_length=24, blank=True, null=True)  # Field name made lowercase.
    curp = models.CharField(db_column='CURP', max_length=24, blank=True, null=True)  # Field name made lowercase.
    nomdenrazsocb = models.CharField(db_column='NOMDENRAZSOCB', max_length=299, blank=True, null=True)  # Field name made lowercase.
    conceptopago_beneficiario = models.IntegerField(db_column='CONCEPTOPAGO_BENEFICIARIO', blank=True, null=True)  # Field name made lowercase.
    descripcionconcepto_beneficiario = models.CharField(db_column='DESCRIPCIONCONCEPTO_BENEFICIARIO', max_length=254, blank=True, null=True)  # Field name made lowercase.
    entidadfederativa = models.CharField(db_column='ENTIDADFEDERATIVA', max_length=2, blank=True, null=True)  # Field name made lowercase.
    monttotpago = models.DecimalField(db_column='MONTTOTPAGO', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    monttotpagograv = models.DecimalField(db_column='MONTTOTPAGOGRAV', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    monttotpagoexent = models.DecimalField(db_column='MONTTOTPAGOEXENT', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    monttotentradasperiodo = models.DecimalField(db_column='MONTTOTENTRADASPERIODO', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    partpropacumdelfideicom = models.DecimalField(db_column='PARTPROPACUMDELFIDEICOM', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    propdelmonttot_ingresosoentradas = models.DecimalField(db_column='PROPDELMONTTOT_INGRESOSOENTRADAS', max_digits=7, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    concepto_integracingresos = models.CharField(db_column='CONCEPTO_INTEGRACINGRESOS', max_length=99, blank=True, null=True)  # Field name made lowercase.
    monttotegresperiodo = models.DecimalField(db_column='MONTTOTEGRESPERIODO', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    partpropdelfideicom = models.DecimalField(db_column='PARTPROPDELFIDEICOM', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    propdelmonttot_deduccosalidas = models.DecimalField(db_column='PROPDELMONTTOT_DEDUCCOSALIDAS', max_digits=7, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    concepto_integracegresos = models.CharField(db_column='CONCEPTO_INTEGRACEGRESOS', max_length=99, blank=True, null=True)  # Field name made lowercase.
    montretrelpagfideic = models.DecimalField(db_column='MONTRETRELPAGFIDEIC', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    descretrelpagfidec = models.CharField(db_column='DESCRETRELPAGFIDEC', max_length=99, blank=True, null=True)  # Field name made lowercase.
    sistemafinanc = models.CharField(db_column='SISTEMAFINANC', max_length=2, blank=True, null=True)  # Field name made lowercase.
    monttotaportanioinmanterior = models.DecimalField(db_column='MONTTOTAPORTANIOINMANTERIOR', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    montintrealesdevenganiooinmant = models.DecimalField(db_column='MONTINTREALESDEVENGANIOOINMANT', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    huboretirosanioinmantper = models.CharField(db_column='HUBORETIROSANIOINMANTPER', max_length=2, blank=True, null=True)  # Field name made lowercase.
    monttotretiradoanioinmantper = models.DecimalField(db_column='MONTTOTRETIRADOANIOINMANTPER', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    monttotexentretiradoanioinmant = models.DecimalField(db_column='MONTTOTEXENTRETIRADOANIOINMANT', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    monttotexedenteanioinmant = models.DecimalField(db_column='MONTTOTEXEDENTEANIOINMANT', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    huboretirosanioinmant = models.CharField(db_column='HUBORETIROSANIOINMANT', max_length=2, blank=True, null=True)  # Field name made lowercase.
    monttotretiradoanioinmant = models.DecimalField(db_column='MONTTOTRETIRADOANIOINMANT', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    creditodeinstfinanc = models.CharField(db_column='CREDITODEINSTFINANC', max_length=2, blank=True, null=True)  # Field name made lowercase.
    saldoinsoluto = models.DecimalField(db_column='SALDOINSOLUTO', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    propdeducdelcredit = models.DecimalField(db_column='PROPDEDUCDELCREDIT', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    monttotintnominalesdev = models.DecimalField(db_column='MONTTOTINTNOMINALESDEV', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    monttotintnominalesdevypag = models.DecimalField(db_column='MONTTOTINTNOMINALESDEVYPAG', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    monttotintrealpagdeduc = models.DecimalField(db_column='MONTTOTINTREALPAGDEDUC', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    numcontrato = models.CharField(db_column='NUMCONTRATO', max_length=299, blank=True, null=True)  # Field name made lowercase.
    montganacum = models.DecimalField(db_column='MONTGANACUM', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    montperdded = models.DecimalField(db_column='MONTPERDDED', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    idfideicom = models.CharField(db_column='IDFIDEICOM', max_length=19, blank=True, null=True)  # Field name made lowercase.
    nomfideicom = models.CharField(db_column='NOMFIDEICOM', max_length=99, blank=True, null=True)  # Field name made lowercase.
    descripfideicom = models.CharField(db_column='DESCRIPFIDEICOM', max_length=299, blank=True, null=True)  # Field name made lowercase.
    cvetipdivoutil = models.CharField(db_column='CVETIPDIVOUTIL', max_length=2, blank=True, null=True)  # Field name made lowercase.
    montisracredretmexico = models.DecimalField(db_column='MONTISRACREDRETMEXICO', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    montisracredretextranjero = models.DecimalField(db_column='MONTISRACREDRETEXTRANJERO', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    montretextdivext = models.DecimalField(db_column='MONTRETEXTDIVEXT', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    tiposocdistrdiv = models.CharField(db_column='TIPOSOCDISTRDIV', max_length=1, blank=True, null=True)  # Field name made lowercase.
    montisracrednal = models.DecimalField(db_column='MONTISRACREDNAL', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    montdivacumnal = models.DecimalField(db_column='MONTDIVACUMNAL', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    montdivacumext = models.DecimalField(db_column='MONTDIVACUMEXT', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    proporcionrem = models.DecimalField(db_column='PROPORCIONREM', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    sistfinanciero = models.CharField(db_column='SISTFINANCIERO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    retiroaoresretint = models.CharField(db_column='RETIROAORESRETINT', max_length=2, blank=True, null=True)  # Field name made lowercase.
    operfinancderivad = models.CharField(db_column='OPERFINANCDERIVAD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    montintnominal = models.DecimalField(db_column='MONTINTNOMINAL', max_digits=7, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    montintreal = models.DecimalField(db_column='MONTINTREAL', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    perdida = models.DecimalField(db_column='PERDIDA', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    contratointermediacion = models.CharField(db_column='CONTRATOINTERMEDIACION', max_length=299, blank=True, null=True)  # Field name made lowercase.
    ganancia = models.DecimalField(db_column='GANANCIA', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    perdida_enajenaciondeacciones = models.DecimalField(db_column='PERDIDA_ENAJENACIONDEACCIONES', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    tiporetencion = models.IntegerField(db_column='TIPORETENCION', blank=True, null=True)  # Field name made lowercase.
    tipopagoret = models.CharField(db_column='TIPOPAGORET', max_length=1, blank=True, null=True)  # Field name made lowercase.
    retencionestado = models.SmallIntegerField(db_column='RETENCIONESTADO', blank=True, null=True)  # Field name made lowercase.
    retencionco = models.CharField(db_column='RETENCIONCO', max_length=999, blank=True, null=True)  # Field name made lowercase.
    retencioncosat = models.TextField(db_column='RETENCIONCOSAT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    retenciontimbre = models.CharField(db_column='RETENCIONTIMBRE', max_length=999, blank=True, null=True)  # Field name made lowercase.
    retencioncert = models.CharField(db_column='RETENCIONCERT', max_length=59, blank=True, null=True)  # Field name made lowercase.
    retencionfechacert = models.IntegerField(db_column='RETENCIONFECHACERT', blank=True, null=True)  # Field name made lowercase.
    retencionejercicio = models.IntegerField(db_column='RETENCIONEJERCICIO', blank=True, null=True)  # Field name made lowercase.
    retencionmesini = models.IntegerField(db_column='RETENCIONMESINI', blank=True, null=True)  # Field name made lowercase.
    retencionmesfin = models.IntegerField(db_column='RETENCIONMESFIN', blank=True, null=True)  # Field name made lowercase.
    retencionfoliopac = models.CharField(db_column='RETENCIONFOLIOPAC', max_length=40, blank=True, null=True)  # Field name made lowercase.
    claveretsat = models.IntegerField(db_column='CLAVERETSAT', blank=True, null=True)  # Field name made lowercase.
    baseret = models.DecimalField(db_column='BASERET', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    impuest_otros = models.CharField(db_column='IMPUEST_OTROS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    montoret_otros = models.DecimalField(db_column='MONTORET_OTROS', max_digits=15, decimal_places=5, blank=True, null=True)  # Field name made lowercase.
    tipopagoret_otros = models.CharField(db_column='TIPOPAGORET_OTROS', max_length=20, blank=True, null=True)  # Field name made lowercase.
    boolformapago = models.SmallIntegerField(db_column='BOOLFORMAPAGO', blank=True, null=True)  # Field name made lowercase.
    ce = models.SmallIntegerField(db_column='CE', blank=True, null=True)  # Field name made lowercase.
    cfdi_emisorregimenfiscal = models.CharField(db_column='CFDI33_EMISORREGIMENFISCAL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cfdi_emisorregimenfiscaldescripcion = models.CharField(db_column='CFDI33_EMISORREGIMENFISCALDESCRIPCION', max_length=500, blank=True, null=True)  # Field name made lowercase.
    cfdi_receptor_usocfdi = models.CharField(db_column='CFDI33_RECEPTOR_USOCFDI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cfdi_receptor_usocfdidescripcion = models.CharField(db_column='CFDI33_RECEPTOR_USOCFDIDESCRIPCION', max_length=500, blank=True, null=True)  # Field name made lowercase.
    cfdi_generada = models.IntegerField(db_column='CFDI33_GENERADA', blank=True, null=True)  # Field name made lowercase.
    cfdi_metodopago = models.CharField(db_column='CFDI33_METODOPAGO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cfdi_metodopagodescripcion = models.CharField(db_column='CFDI33_METODOPAGODESCRIPCION', max_length=500, blank=True, null=True)  # Field name made lowercase.
    cfdi_tipocomprobante = models.CharField(db_column='CFDI33_TIPOCOMPROBANTE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cfdi_fechayhoraemision = models.CharField(db_column='CFDI33_FECHAYHORAEMISION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cfdi_aplicaiva = models.IntegerField(db_column='CFDI33_APLICAIVA', blank=True, null=True)  # Field name made lowercase.
    cfdi_residenciafiscal = models.CharField(db_column='CFDI33_RESIDENCIAFISCAL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cfdi_residenciafiscaldescripcion = models.CharField(db_column='CFDI33_RESIDENCIAFISCALDESCRIPCION', max_length=249, blank=True, null=True)  # Field name made lowercase.
    cfdi_numregidtrib = models.CharField(db_column='CFDI33_NUMREGIDTRIB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cfdi_versiontimbrado = models.CharField(db_column='CFDI33_VERSIONTIMBRADO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cfdi_rfcprovcertificacion = models.CharField(db_column='CFDI33_RFCPROVCERTIFICACION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cfdi_operacion_fechainstnotarial = models.CharField(db_column='CFDI33_OPERACION_FECHAINSTNOTARIAL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cfdi_cartaporte = models.IntegerField(db_column='CFDI33_CARTAPORTE', blank=True, null=True)  # Field name made lowercase.
    cfdi_egreso_fechayhoraemision = models.CharField(db_column='CFDI33_EGRESO_FECHAYHORAEMISION', max_length=24, blank=True, null=True)  # Field name made lowercase.
    cfdi_cuentapredial = models.CharField(db_column='CFDI33_CUENTAPREDIAL', max_length=154, blank=True, null=True)  # Field name made lowercase.
    
    
    egreso_cadenaoriginal = models.TextField(db_column='EGRESO_CADENAORIGINAL', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    egreso_sellodigital = models.CharField(db_column='EGRESO_SELLODIGITAL', max_length=999, blank=True, null=True)  # Field name made lowercase.
    egreso_nocertificado = models.CharField(db_column='EGRESO_NOCERTIFICADO', max_length=99, blank=True, null=True)  # Field name made lowercase.
    egreso_foliopac = models.CharField(db_column='EGRESO_FOLIOPAC', max_length=99, blank=True, null=True)  # Field name made lowercase.
    egreso_fechacertificacion = models.CharField(db_column='EGRESO_FECHACERTIFICACION', max_length=24, blank=True, null=True)  # Field name made lowercase.
    egreso_sellocfdtimbrado = models.CharField(db_column='EGRESO_SELLOCFDTIMBRADO', max_length=99, blank=True, null=True)  # Field name made lowercase.
    egreso_cfdi33_rfcprovcertificacion = models.CharField(db_column='EGRESO_CFDI33_RFCPROVCERTIFICACION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    egreso_cfdi33_versiontimbrado = models.CharField(db_column='EGRESO_CFDI33_VERSIONTIMBRADO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    egreso_cadenaoriginalsat = models.TextField(db_column='EGRESO_CADENAORIGINALSAT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    egreso_sellodigitalsat = models.CharField(db_column='EGRESO_SELLODIGITALSAT', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    egreso_nocertificadosat = models.CharField(db_column='EGRESO_NOCERTIFICADOSAT', max_length=99, blank=True, null=True)  # Field name made lowercase.
    egreso_estatus = models.CharField(db_column='EGRESO_ESTATUS', max_length=19, blank=True, null=True)  # Field name made lowercase.
    
    traslado_cfdi33_tipocomprobante = models.CharField(db_column='TRASLADO_CFDI33_TIPOCOMPROBANTE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    traslado_cadenaoriginal = models.TextField(db_column='TRASLADO_CADENAORIGINAL', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    traslado_sellodigital = models.CharField(db_column='TRASLADO_SELLODIGITAL', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    traslado_nocertificado = models.CharField(db_column='TRASLADO_NOCERTIFICADO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    traslado_foliopac = models.CharField(db_column='TRASLADO_FOLIOPAC', max_length=100, blank=True, null=True)  # Field name made lowercase.
    traslado_fechacertificacion = models.CharField(db_column='TRASLADO_FECHACERTIFICACION', max_length=24, blank=True, null=True)  # Field name made lowercase.
    traslado_cfdi33_rfcprovcertificacion = models.CharField(db_column='TRASLADO_CFDI33_RFCPROVCERTIFICACION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    traslado_cfdi33_versiontimbrado = models.CharField(db_column='TRASLADO_CFDI33_VERSIONTIMBRADO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    traslado_cadenaoriginalsat = models.TextField(db_column='TRASLADO_CADENAORIGINALSAT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    traslado_sellodigitalsat = models.CharField(db_column='TRASLADO_SELLODIGITALSAT', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    traslado_nocertificadosat = models.CharField(db_column='TRASLADO_NOCERTIFICADOSAT', max_length=100, blank=True, null=True)  # Field name made lowercase.
    traslado_estatus = models.CharField(db_column='TRASLADO_ESTATUS', max_length=19, blank=True, null=True)  # Field name made lowercase.
    traslado_cfdi33_fechayhoraemision = models.CharField(db_column='TRASLADO_CFDI33_FECHAYHORAEMISION', max_length=24, blank=True, null=True)  # Field name made lowercase.
    
    
    retencion_sello = models.TextField(db_column='RETENCION_SELLO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    retencion_fechacertificacion = models.CharField(db_column='RETENCION_FECHACERTIFICACION', max_length=24, blank=True, null=True)  # Field name made lowercase.
    retencion_versiontimbrado = models.CharField(db_column='RETENCION_VERSIONTIMBRADO', max_length=54, blank=True, null=True)  # Field name made lowercase.
    retencion_sellodigitalsat = models.TextField(db_column='RETENCION_SELLODIGITALSAT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    retencion_nocertificadosat = models.CharField(db_column='RETENCION_NOCERTIFICADOSAT', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    retencion_estado = models.CharField(db_column='RETENCION_ESTADO', max_length=24, blank=True, null=True)  # Field name made lowercase.
    retencion_fechayhoraemision = models.CharField(db_column='RETENCION_FECHAYHORAEMISION', max_length=34, blank=True, null=True)  # Field name made lowercase.
    retencion_monttotpago = models.DecimalField(db_column='RETENCION_MONTTOTPAGO', max_digits=17, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    retencion_monttotpagograv = models.DecimalField(db_column='RETENCION_MONTTOTPAGOGRAV', max_digits=17, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    retencion_monttotpagoexent = models.DecimalField(db_column='RETENCION_MONTTOTPAGOEXENT', max_digits=17, decimal_places=6, blank=True, null=True)  # Field name made lowercase.    
    retencion_montototret = models.DecimalField(db_column='RETENCION_MONTOTOTRET', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    retencion_impretenidos_montoret = models.DecimalField(db_column='RETENCION_IMPRETENIDOS_MONTORET', max_digits=15, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    retencion_impretenidos_impuesto = models.CharField(db_column='RETENCION_IMPRETENIDOS_IMPUESTO', max_length=19, blank=True, null=True)  # Field name made lowercase.
    retenciones_descretenc = models.DecimalField(db_column='RETENCIONES_DESCRETENC', max_digits=17, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    ret_motivo_cancelacion = models.CharField(db_column='RET_MOTIVO_CANCELACION', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ret_folio_cancelacion = models.CharField(db_column='RET_FOLIO_CANCELACION', max_length=99, blank=True, null=True)  # Field name made lowercase.
    
    
    comercioexterior_activo = models.IntegerField(db_column='COMERCIOEXTERIOR_ACTIVO', blank=True, null=True)  # Field name made lowercase.
    aplica_anticipos_cfdi33 = models.IntegerField(db_column='APLICA_ANTICIPOS_CFDI33', blank=True, null=True)  # Field name made lowercase.
    cancelstatus_cfdi33 = models.CharField(db_column='CANCELSTATUS_CFDI33', max_length=99, blank=True, null=True)  # Field name made lowercase.
    iscancelable_cfdi33 = models.CharField(db_column='ISCANCELABLE_CFDI33', max_length=99, blank=True, null=True)  # Field name made lowercase.
    tiporelacioncfdi33 = models.CharField(db_column='TIPORELACIONCFDI33', max_length=4, blank=True, null=True)  # Field name made lowercase.
    ine_activo = models.IntegerField(db_column='INE_ACTIVO', blank=True, null=True)  # Field name made lowercase.
    tipoproceso = models.CharField(db_column='TIPOPROCESO', max_length=29, blank=True, null=True)  # Field name made lowercase.
    tipocomite = models.CharField(db_column='TIPOCOMITE', max_length=29, blank=True, null=True)  # Field name made lowercase.
    idcontabilidad = models.CharField(db_column='IDCONTABILIDAD', max_length=29, blank=True, null=True)  # Field name made lowercase.
    exportacion = models.CharField(db_column='EXPORTACION', max_length=2, blank=True, null=True)  # Field name made lowercase.
    infoglo_periodicidad = models.CharField(db_column='INFOGLO_PERIODICIDAD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    infoglo_meses = models.CharField(db_column='INFOGLO_MESES', max_length=2, blank=True, null=True)  # Field name made lowercase.
    infoglo_anio = models.CharField(db_column='INFOGLO_ANIO', max_length=4, blank=True, null=True)  # Field name made lowercase.
    motivo_cancelacion = models.CharField(db_column='Motivo_Cancelacion', max_length=2, blank=True, null=True)  # Field name made lowercase.
    folio_cancelacion = models.CharField(db_column='Folio_Cancelacion', max_length=99, blank=True, null=True)  # Field name made lowercase.
    cfdi_tipopagoret = models.CharField(db_column='CFDI4_TIPOPAGORET', max_length=4, blank=True, null=True)  # Field name made lowercase.
    

    class Meta:
        abstract = True #avoid make migrations form this model
        db_table = 'FactFactura'