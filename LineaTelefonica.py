class LineaTelefonica:
    '''----------------------------------------------------------------
    # atributos
    ----------------------------------------------------------------'''
    
    # Numero de llamadas realizadas
    numeroLlamadas = 0
    
    # Numero de minutos consumidos
    numeroMinutos = 0
    
    # Costo total de las llamadas
    costoLlamadas = 0

    # Estrato de la línea telefónica
    estrato = 0

    # Descuento para llamadas
    descuento = 0.0  # Tipo: float. Rango de valores: 0.0 a 25.5
    
    # Dinero disponible para gastar
    saldo = 0

    '''----------------------------------------------------------------
    # Metodos
    ----------------------------------------------------------------'''
    
    # Inicializar el número de llamadas, número de minutos y costo de llamadas en 0.
    def __init__(self):
        # TODO Parte2 PuntoA: Completar el método según la documentación dada.
        self.numeroLlamadas = 0
        self.numeroMinutos = 0
        self.costoLlamadas = 0         

    #Retorna el costo total de las llamadas realizadas.
    def darCostoLlamadas(self):
        # TODO Parte2 PuntoB: Completar el método según la documentación dada.
        return self.costoLlamadas

    # Retorna el número de llamadas realizadas por esta línea.
    def darNumeroLlamadas(self):
        # TODO Parte2 PuntoC: Completar el método según la documentación dada.
        return self.numeroLlamadas
        
    # Retorna el número de minutos consumidos.
    def darNumeroMinutos(self):
        # TODO Parte2 PuntoD: Completar el método según la documentación dada.
        return self.numeroMinutos

    # Reinicia la línea telefónica, dejando todos sus valores en cero.
    # post: El número de llamadas, número de minutos y costo de llamadas son 0.
    def reiniciar(self):
        # TODO Parte2 PuntoE: Completar el método según la documentación dada.
        self.numeroLlamadas = 0
        self.numeroMinutos = 0
        self.costoLlamadas = 0

    # Agrega una llamada local a la línea telefónica
    # post: Se incrementá en 1 numeroDeLlamadas, se incremento numeroDeMinutos en minutos, costoLlamadas aumentá en ( minutos * 35 ).
    # :param pMinutos Número de minutos de la llamada. pMinutos >0.
    def agregarLlamadaLocal(self, pMinutos):
        
        # Una llamada más
        self.numeroLlamadas += 1
        # Suma los minutos consumidos
        self.numeroMinutos += pMinutos
        # Suma el costo (costo por minuto: 35 pesos)
        self.costoLlamadas += pMinutos * 35

    """
        Agrega una llamada de larga distancia a la línea telefónica.
        
        post: Se incrementá en 1 numeroDeLlamadas, se incremento numeroDeMinutos en minutos, costoLlamadas aumentá en ( minutos * 380 )
        
        :param pMinutos: Número de minutos de la llamada. pMinutos >0.
        """
    def agregarLlamadaLargaDistancia(self, pMinutos):
        # TODO Parte2 PuntoF: Completar el método según la documentación dada.
        # Una llamada más
        self.numeroLlamadas += 1
        # Suma los minutos consumidos
        self.numeroMinutos += pMinutos
        # Suma el costo (costo por minuto: 380 pesos)
        self.costoLlamadas += pMinutos * 380        
        # Resta el costo de la llamada a saldo
        self.saldo - (pMinutos * 380)

    '''
        Agrega una llamada a celular a la lÍnea telefónica
        post: Se incrementá en 1 numeroDeLlamadas, se incremento numeroDeMinutos en minutos, costoLlamadas aumentá en ( minutos * 999 )
        :param pMinutos Número de minutos de la llamada. pMinutos >0.
    '''
    def agregarLlamadaCelular(self, pMinutos):
        # TODO Parte2 PuntoG: Completar el método según la documentación dada.
        # Una llamada más
        self.numeroLlamadas += 1
        # Suma los minutos consumidos
        self.numeroMinutos += pMinutos
        # Suma el costo (costo por minuto: 999 pesos)
        self.costoLlamadas += pMinutos * 999

    def darDescuento(self):
        # Retorna el descuento para llamadas
        return self.descuento
    
    def aplicarDescuento(self):
        descuentoAplicado = (self.costoLlamadas * self.descuento) / 100
        return descuentoAplicado

    def consulatarSaldo(self):
        return self.saldo
    
    def recargaSaldo(self, valor):
        self.saldo += valor
        return self.saldo

    def motivarCliente(self):
        self.saldo += (self.numeroMinutos // 30) * 1000
        return self.saldo
     
