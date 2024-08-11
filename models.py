from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Marca(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)

class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)

class Modelo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    marca_id = db.Column(db.Integer, db.ForeignKey('marca.id'), nullable=False)
    marca = db.relationship('Marca', backref=db.backref('modelos', lazy=True))

class Fabricante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    pais = db.Column(db.String(50), nullable=False)

class Caracteristica(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.String(200), nullable=False)

class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cantidad = db.Column(db.Integer, nullable=False)
    ubicacion = db.Column(db.String(100), nullable=False)

class Proveedor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    contacto = db.Column(db.String(100), nullable=False)

class Accesorio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(50), nullable=False)
    compatible_con_modelos = db.Column(db.String(200), nullable=False)

class Celular(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'), nullable=False)
    modelo_id = db.Column(db.Integer, db.ForeignKey('modelo.id'), nullable=False)
    costo = db.Column(db.Float, nullable=False)

    categoria = db.relationship('Categoria', backref=db.backref('celulares', lazy=True))
    modelo = db.relationship('Modelo', backref=db.backref('celulares', lazy=True))

    fabricante_id = db.Column(db.Integer, db.ForeignKey('fabricante.id'), nullable=False)
    fabricante = db.relationship('Fabricante', backref=db.backref('celulares', lazy=True))

    caracteristica_id = db.Column(db.Integer, db.ForeignKey('caracteristica.id'), nullable=False)
    caracteristica = db.relationship('Caracteristica', backref=db.backref('celulares', lazy=True))

    stock_id = db.Column(db.Integer, db.ForeignKey('stock.id'), nullable=False)
    stock = db.relationship('Stock', backref=db.backref('celulares', lazy=True))

    proveedor_id = db.Column(db.Integer, db.ForeignKey('proveedor.id'), nullable=False)
    proveedor = db.relationship('Proveedor', backref=db.backref('celulares', lazy=True))

    accesorio_id = db.Column(db.Integer, db.ForeignKey('accesorio.id'), nullable=False)
    accesorio = db.relationship('Accesorio', backref=db.backref('celulares', lazy=True))

    precio = db.Column(db.Float, nullable=False)


