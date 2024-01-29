from sqlalchemy import create_engine
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base


SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

engine = create_engine()

Base = declarative_base()



class User (Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key = True)
    username = Column (String(20), nullable = False)
    password = Column (String(12), nullable = False)

    user_producto = relationship ('Producto', back_populates = 'producto')
    user_producto_electrico = relationship ('Producto_Electrico', back_populates = 'producto_electrico')


class Producto (Base):
    __tablename__ = 'productos'
    id = Column(Integer, primary_key = True)
    clothes = Column( String(25), nullable = False)

    # users_id = Base.Column(Base.Integer, Base.ForeignKey('users.id'))
    user = relationship ('User', back_populates = 'user')
    

class Producto_Electrico (Base):
    __tablename__ = 'electricos'
    id = Column(Integer, primary_key = True)
    electronic = Column( String(25), nullable = False)

    # users_id = Base.Column(Base.Integer, Base.ForeignKey('users.id'))
    user = relationship ('User', back_populates = 'user')



    


