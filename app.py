from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/vehiculos_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

celulares_json = {
    "Celulares": []
}

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/info")
def info():
    return render_template('info.html')

@app.route("/inventario")
def inv_celular():
    return render_template('inventario.html', celulares=celulares_json['Celulares'])

@app.route('/crear_celular', methods=['POST', 'GET'])
def agregar_celular():
    if request.method == 'GET':
        return render_template('crear_celular.html')
    
    if request.method == 'POST':
        data = request.form
        equipo_nombre = data.get('equipo_nombre')
        equipo_categoria = data.get('equipo_categoria')
        equipo_modelo = data.get('equipo_modelo')
        equipo_costo = data.get('equipo_costo')

        marca_celular = data.get('marca_celular')
        categoria_celular = data.get('categoria_celular')
        modelo_celular = data.get('modelo_celular')
        nombre_modelo_celular = data.get('nombre_modelo_celular')
        fabricante_nombre = data.get('fabricante_nombre')
        fabricante_pais = data.get('fabricante_pais')

        tipo_caracteristica = data.get('tipo_caracteristica')
        descripcion_caracteristica = data.get('descripcion_caracteristica')

        cantidad_stock = data.get('cantidad_stock')
        ubicacion_almacen = data.get('ubicacion_almacen')

        nombre_proveedor = data.get('nombre_proveedor')
        contacto_proveedor = data.get('contacto_proveedor')

        tipo_accesorio = data.get('tipo_accesorio')
        compatible_con_modelos = data.get('compatible_con_modelos')
        precio = data.get('precio')

        nuevo_celular = {
            "equipo_nombre": equipo_nombre,
            "equipo_categoria": equipo_categoria,
            "equipo_modelo": equipo_modelo,
            "equipo_costo": equipo_costo,

            "marca_celular": marca_celular,
            "categoria_celular": categoria_celular,
            "modelo_celular": modelo_celular,
            "nombre_modelo_celular": nombre_modelo_celular,

            "fabricante_nombre": fabricante_nombre,
            "fabricante_pais": fabricante_pais,

            "tipo_caracteristica": tipo_caracteristica,
            "descripcion_caracteristica": descripcion_caracteristica,

            "cantidad_stock": cantidad_stock,
            "ubicacion_almacen": ubicacion_almacen,

            "nombre_proveedor": nombre_proveedor,
            "contacto_proveedor": contacto_proveedor,

            "tipo_accesorio": tipo_accesorio,
            "compatible_con_modelos": compatible_con_modelos,

            "precio": precio,
        }

        celulares_json['Celulares'].append(nuevo_celular)
        return redirect('/inventario')

if __name__ == "__main__":
    app.run(debug=True)
