from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
DeclarativeBase = declarative_base()

class Category(DeclarativeBase):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    link = Column(String)
    manga  = relationship("ProductInflation", back_populates="product")