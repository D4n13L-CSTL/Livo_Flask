from .db import ReportarPago
from conexiones.cursores import get_cursor

pago_atleta  = ReportarPago(get_cursor)