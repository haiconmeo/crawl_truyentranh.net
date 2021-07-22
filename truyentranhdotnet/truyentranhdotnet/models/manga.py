from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
DeclarativeBase = declarative_base()

class Manga(DeclarativeBase):
    __tablename__ = 'manga'

    id = Column(Integer, primary_key=True)
    name  = Column(String, index=True)
    link = Column(String)
    categori_id = Column(Integer, ForeignKey('categori.id'))
    category = relationship("Category", back_populates="manga")
    chaper = relationship("Manga", back_populates="manga")