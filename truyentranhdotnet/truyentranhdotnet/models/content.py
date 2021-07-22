from sqlalchemy import Column, String, Integer, DateTime,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime
DeclarativeBase = declarative_base()

class Content(DeclarativeBase):
    __tablename__ = 'content'

    id = Column(Integer, primary_key=True)
    offset = Column(Integer)
    link = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, onupdate=datetime.datetime.now)
    chaper_id =  Column(Integer, ForeignKey('chaper.id'))
    chaper = relationship("Chaper", back_populates="content")