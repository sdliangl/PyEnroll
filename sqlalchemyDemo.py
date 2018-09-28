from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://sdliangl:078521@192.168.163.128:3306/PyEnroll")

Session = sessionmaker(bind=engine)