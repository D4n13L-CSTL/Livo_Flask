from modelClass.BaseDAO import WriteDAO, BaseDAO


class ReportarPago(WriteDAO):
    def reportar_pago(self,id_atleta,id_club, monto,fecha_pago,referencia,id_metodo):
        query = """
            insert into pagos (id_atleta,id_club, monto,fecha_pago,referencia,id_metodo) VALUES (%s,%s,%s,%s,%s,%s)
        """
        return self.insert_and_return_id(query,(id_atleta,id_club, monto,fecha_pago,referencia,id_metodo))