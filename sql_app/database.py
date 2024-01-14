from sqlalchemy import create_engine, Column, Integer, String,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:@localhost:3306/salloum"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
metadata = Base.metadata

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(8))
    is_active = Column(Integer, default=1)




class TODO(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True)
    title = Column(String(50), unique=True, nullable=False)
    description = Column(String(50), nullable=False)
    done = Column(Integer, default=0)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    priority = Column(Integer, default=0)
    user = relationship("User", backref="todos")
