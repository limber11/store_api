# Importación de la base de datos
from app.database import db

# Definición de la clase Producto
class Producto(db.Model):
    # Configuración de la tabla de la base de datos
    __tablename__ = "productos"

    # Definición de columnas
    id = db.Column(db.Integer, primary_key=True)  # Clave primaria de tipo entero
    name = db.Column(db.String(100), nullable=False)  # Nombre del producto (cadena de máximo 100 caracteres, no nulo)
    description = db.Column(db.String(100), nullable=False)  # Descripción del producto (cadena de máximo 100 caracteres, no nulo)
    price = db.Column(db.Float, nullable=False)  # Precio del producto (flotante, no nulo)
    stock = db.Column(db.Integer, nullable=False)  # Stock del producto (entero, no nulo)

    # Constructor
    def __init__(self, name, description, price, stock):
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock

    # Método para guardar el producto en la base de datos
    def save(self):
        db.session.add(self)
        db.session.commit()

    # Método estático para obtener todos los productos de la base de datos
    @staticmethod
    def get_all():
        return Producto.query.all()

    # Método estático para obtener un producto por su ID
    @staticmethod
    def get_by_id(id):
        return Producto.query.get(id)

    # Método para actualizar los atributos del producto en la base de datos
    def update(self, name=None, description=None, price=None, stock=None):
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if price is not None:
            self.price = price
        if stock is not None:
            self.stock = stock
        db.session.commit()

    # Método para eliminar el producto de la base de datos
    def delete(self):
        db.session.delete(self)
        db.session.commit()
