from datetime import datetime
from app import db


class Divisa(db.Model):
    __tablename__='divisa'
    id_Divisa = db.Column(db.Integer, primary_key = True)
    Nombre = db.Column(db.String(50), unique = True, nullable = False)
    Nomenclatura = db.Column(db.String, unique = True, nullable = False)
    Relacion_Pesos = db.Column(db.Float(50))
    #Divisas = db.relationship('Cuenta_Bancaria', backref='Divisa', lazy=True)

    def __repr__(self):
        return '<divisa {}>'.format(self.Nombre)

        
class Cuenta_Credito(db.Model):
    __tablename__='CuentaCredito'
    id_Tarjeta_Credito = db.Column(db.Integer, primary_key = True)
    Pasivos_Totales= db.Column(db.Float, nullable = False)
    Limite_Credito = db.Column(db.Float, nullable = False)
    Credito_Restante = db.Column(db.Float, nullable = False)
    #Cuentas_Credito = db.relationship('Tipo_Cuenta', backref='Cuenta_Credito', lazy=True)

    def __repr__(self):
        return '<CuentaCredito {}>'.format(self.Credito_Restante)

        
class Plan_Pago(db.Model):
    __tablename__='PlanPago'
    id_Plan_Pago = db.Column(db.Integer, primary_key = True)
    Fecha_Inicial  = db.Column(db.String(50), nullable=False)
    Fecha_Final = db.Column(db.String(50), nullable=False)
    Valor_Cuotas = db.Column(db.Float, nullable = False)
    #Planes_Pago = db.relationship('Cuenta_Prestamos', backref=db.backref('Plan_Pago', lazy=True))

    def __repr__(self):
        return '<PlanPago {}>'.format(self.Valor_Cuotas)

        
class Cuenta_Prestamos(db.Model):
    __tablename__='CuentaPrestamos'
    id_Prestamos = db.Column(db.Integer, primary_key = True)
    Monto  = db.Column(db.Float, nullable = False)
    Periodo = db.Column(db.Float, nullable = False)
    id_Plan_Pago = db.Column(db.Integer, db.ForeignKey('PlanPago.id_Plan_Pago'), nullable= False)
    #Cuentas_Prestamos = db.relationship('Tipo_Cuenta', backref='Cuenta_Prestamos', lazy=True)'''

    def __repr__(self):
        return '<CuentaPrestamos {}>'.format(self.Monto)

        
class Cuenta_Cheques(db.Model):
    __tablename__='CuentaCheques'
    id_CuentaCheque = db.Column(db.Integer, primary_key = True)
    Depositar  = db.Column(db.Float, nullable = True)
    Retirar = db.Column(db.Float, nullable = True)
    Pagar  = db.Column(db.Float, nullable = True)
    Estado = db.Column(db.String(50), nullable = False)
    id_Cheque = db.Column(db.Integer, db.ForeignKey('Cheques.id_Cheque'), nullable= True)
    id_Tarjeta_Debito = db.Column(db.Integer, db.ForeignKey('TarjetaDebito.id_Tarjeta_Debito'), nullable= True)
    #Cuentas_Cheques = db.relationship('Tipo_Cuenta', backref='Cuenta_Cheques', lazy=True)

    def __repr__(self):
        return '<CuentaCheques {}>'.format(self.Estado)

        
class Cheque(db.Model):
    __tablename__='Cheques'
    id_Cheque = db.Column(db.Integer, primary_key = True)
    Monto  = db.Column(db.Float, nullable = False)
    Fecha = db.Column(db.DateTime(), nullable=False)
    Beneficiario = db.Column(db.String(50), nullable = False)
    #Cuentas_Cheques = db.relationship('Tipo_Cuenta', backref='Cuenta_Cheques', lazy=True)

    def __repr__(self):
        return '<Cheques {}>'.format(self.Monto)

        
class Tarjeta_Debito(db.Model):
    __tablename__='TarjetaDebito'
    id_Tarjeta_Debito = db.Column(db.Integer, primary_key = True)
    Monto  = db.Column(db.Float, nullable = False)

    def __repr__(self):
        return '<TarjetaDebito {}>'.format(self.Monto)

        
class Cuenta_Inversion(db.Model):
    __tablename__='CuentaInversion'
    id_Cuenta_Inversion = db.Column(db.Integer, primary_key = True)
    Monto = db.Column(db.Float, nullable = False)
    #Cuentas_Inversion = db.relationship('Tipo_Cuenta', backref='Cuenta_Inversion', lazy=True)

    def __repr__(self):
        return '<CuentaInversion {}>'.format(self.Monto)

        
class Tipo_Cuenta(db.Model):
    __tablename__='TipoCuenta'
    id_Tipo_Cuenta = db.Column(db.Integer, primary_key = True)
    Nombre = db.Column(db.String(50), nullable = False)
    Numero_Cuenta = db.Column(db.Integer,nullable=False) 
    Descripcion = db.Column(db.String(50), nullable = False)
    Saldo = db.Column(db.Integer,nullable=False)
    tipo = db.Column(db.String(50), nullable = False)
    '''
    id_Tarjeta_Credito = db.Column(db.Integer, db.ForeignKey('CuentaCredito.id_Tarjeta_Credito'), nullable= True)
    id_Prestamos = db.Column(db.Integer, db.ForeignKey('CuentaPrestamos.id_Prestamos'), nullable= True)
    id_CuentaCheque = db.Column(db.Integer, db.ForeignKey('CuentaCheques.id_CuentaCheque'), nullable= True)
    id_Cuenta_Inversion = db.Column(db.Integer, db.ForeignKey('CuentaInversion.id_Cuenta_Inversion'), nullable= True)
    #Tipos_Cuentas = db.relationship('Cuenta_Bancaria', backref='Tipo_Cuenta', lazy=True)
    '''
  
class Presupuesto(db.Model):
    __tablename__='presupuesto'
    Id_presupuesto=db.Column(db.Integer, primary_key=True)
    Nombre_Presupuesto=db.Column(db.String(50), nullable=True)
    Monto_Presupuesto=db.Column(db.Float,nullable=False)
    P_Recurrencia=db.Column(db.String(10))
    Id_Transaccion=db.Column(db.Integer, db.ForeignKey('transaccion.Id_Transaccion'), nullable=False)
    #Presupuestos = db.relationship('Cuenta_Bancaria', backref='Presupuesto', lazy=True)

    def __repr__(self):
        return '<presupuesto {}>'.format(self.Nombre_Presupuesto)

        
class Transaccion(db.Model):
    __tablename__='transaccion'
    Id_Transaccion=db.Column(db.Integer, primary_key=True)
    Cuenta_Receptor=db.Column(db.Integer,nullable=False)
    #Transacciones = db.relationship('Presupuesto', backref='Transaccion', lazy=True)
    Id_Ingreso=db.Column(db.Integer,db.ForeignKey('ingreso.Id_Ingreso'), nullable = True)
    Id_Reembolso=db.Column(db.Integer,db.ForeignKey('reembolso.Id_Reembolso'),  nullable = True)
    Id_Gasto=db.Column(db.Integer,db.ForeignKey('gasto.Id_Gasto'), nullable = True)
    
    def __repr__(self):
        return '<transaccion {}>'.format(self.Cuenta_Receptor)

        
class Ingreso(db.Model):
    __tablename__='ingreso'
    Id_Ingreso=db.Column(db.Integer,primary_key=True)
    Fecha=db.Column(db.DateTime(), nullable=False)
    Monto=db.Column(db.Float,nullable=False)
    Descripcion=db.Column(db.Text)
    #Ingresos = db.relationship('Transaccion', backref='Ingreso', lazy=True)

    def __repr__(self):
        return '<ingreso {}>'.format(self.Monto)

        
class Reembolso(db.Model):
    __tablename__='reembolso'
    Id_Reembolso=db.Column(db.Integer,primary_key=True)
    Fecha=db.Column(db.DateTime(),nullable=False)
    Monto=db.Column(db.Float,nullable=False)
    Descripcion=db.Column(db.Text)
    #Reembolsos = db.relationship('Transaccion', backref='Reembolso', lazy=True)

    def __repr__(self):
        return '<reembolso {}>'.format(self.Descripcion)

        
class Gasto(db.Model):
    __tablename__='gasto'
    Id_Gasto=db.Column(db.Integer,primary_key=True)
    Fecha=db.Column(db.DateTime(),nullable=False)
    Monto=db.Column(db.Float,nullable=False)
    Descripcion=db.Column(db.Text)
    #Gastos = db.relationship('Transaccion', backref='Gasto', lazy=True)

    def __repr__(self):
        return '<gasto {}>'.format(self.Descripcion)

        
class Cuenta_Bancaria(db.Model):
    __tablename__='CuentaBancaria'
    id_Cuenta_Bancaria = db.Column(db.Integer, primary_key = True)
    id_Divisa = db.Column(db.Integer, db.ForeignKey('divisa.id_Divisa'), nullable = False) 
    Patrimonio_Actual = db.Column(db.Float, nullable = False)
    id_Tipo_Cuenta = db.Column(db.Integer, db.ForeignKey('TipoCuenta.id_Tipo_Cuenta'), nullable = False)
    Id_presupuesto = db.Column(db.Integer, db.ForeignKey('presupuesto.Id_presupuesto'), nullable = False)

    def __repr__(self):
        return '<CuentaBancaria {}>'.format(self.Patrimonio_Actual)