from flask import request


class BasePago:
    def __init__(self, pagos):
        self.pagos = pagos
        
class ReportePagoAtleta(BasePago):
    def __init__(self, pagos):
        super().__init__(pagos)
    
    def reporte_de_pago(self):
        #id_atleta,id_club, monto,fecha_pago,referencia,id_metodo
        id_atleta  = request.cookies.get()
        return self.pagos.reportar_pago()