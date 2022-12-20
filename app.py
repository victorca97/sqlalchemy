from flask import Flask
from routes.administradores import administradores
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:admin@localhost/administradores"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

SQLAlchemy(app)

app.register_blueprint(administradores)


# Declara una clase base para las tablas
Base = declarative_base()

# Declara una clase de tabla
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    age = Column(Integer)

def create_database(admin_name):
    # Crea una conexión a un servidor de base de datos MySQL
    engine= create_engine('mysql://root:admin@localhost/')

    # Crea la base de datos "admin1_db"
    engine.execute(f"CREATE DATABASE {admin_name}")
    # Crea una conexión a la base de datos para el administrador especificado
    engine = create_engine(f'mysql://root:admin@localhost/{admin_name}')

    # Crea la tabla en la base de datos
    Base.metadata.create_all(engine)

    # Crea una sesión de base de datos
    #Session = sessionmaker(bind=engine)
    #session = Session()

    # Agrega un nuevo registro a la tabla
    #new_user = User(name='John', age=30)
    #session.add(new_user)
    #session.commit()

    # Consulta los registros de la tabla
    #users = session.query(User).all()
    #for user in users:
    #    print(user.name, user.age)
 

# Crea una base de datos y tablas para el administrador "admin1"
#create_database("admin1")

# Crea una base de datos y tablas para el administrador "admin2"
#create_database("admin2")

