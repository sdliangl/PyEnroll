from sqlalchemy import create_engine, Column, String, INTEGER, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine ("mysql+pymysql://sdliangl:078521@192.168.163.128:3306/PyEnroll")
Session = sessionmaker (bind=engine)

Base = declarative_base ()


class Users (Base):
    __tablename__ = "Users"

    id = Column (INTEGER, primary_key=True)
    UserName = Column (String (20), nullable=False)
    PassWd = Column(String(45))
    CreateDate = Column(DateTime)

    def __repr__(self):
        return "<Users>  {}:{} 密码：{}".format (self.id, self.UserName,self.PassWd)

# Base.metadata.create_all(engine)
#
#
session=Session()
# session.commit()
# session.rollback()
# session.close()

# user = Users(id=1,UserName="liangl",PassWd="joboy",CreateDate=None)
# session=Session()
#
# session.add(user)
# session.commit()
# session.close()

target = session.query(Users).filter(Users.UserName=="Liangl").first()
session.close()
print(target)


