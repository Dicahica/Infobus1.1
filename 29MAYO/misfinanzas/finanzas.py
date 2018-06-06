from app import app, db
from app.models import Divisa, Cuenta_Credito, Plan_Pago, Cuenta_Prestamos, Cuenta_Cheques, Cheque, Tarjeta_Debito, Cuenta_Inversion, Tipo_Cuenta, Presupuesto, Transaccion, Ingreso, Reembolso, Gasto, Cuenta_Bancaria #tablas


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Divisa': Divisa, 'Cuenta_Credito': Cuenta_Credito, 'Plan_Pago': Plan_Pago, 'Cuenta_Prestamos': Cuenta_Prestamos, 'Cuenta_Cheques': Cuenta_Cheques, 'Cheque': Cheque, 'Tarjeta_Debito': Tarjeta_Debito, 'Cuenta_Inversion': Cuenta_Inversion, 'Tipo_Cuenta': Tipo_Cuenta, 'Presupuesto': Presupuesto, 'Transaccion': Transaccion, 'Ingreso': Ingreso, 'Reembolso': Reembolso, 'Gasto': Gasto, 'Cuenta_Bancaria': Cuenta_Bancaria}#aqui van los nombres de las tablas