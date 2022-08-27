from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy import create_engine
import datetime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine("sqlite:///test.db", echo=True)


class Book(Base):
    __tablename__ = "book"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    qty = Column(Integer)
    newcol = Column(String)


# this table should be present in our db intially.
class version(Base):
    __tablename__= "versions"
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    stamp = Column('stamp', DateTime, default=datetime.datetime.now())
    revisionnum = Column('revisionnum',String, nullable=False)

#    op.execute("INSERT INTO versions(revisionnum) VALUES ('${up_revision}', datetime())")
