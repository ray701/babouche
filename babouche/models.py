from sqlalchemy import (
    Column,
    Index,
    Integer,
    String,
    Text,
    Date,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class MyModel(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    value = Column(Integer)

Index('my_index', MyModel.name, unique=True, mysql_length=255)


class Page(Base):
    """
    The SQLAlchemy declarative model class for a Page object.
    """
    __tablename__ = 'pages'
    id = Column(Integer, primary_key=True)
    name = Column(String(length=255))
    data = Column(Text)

    def __init__(self, name, data):
        self.name = name
        self.data = data

