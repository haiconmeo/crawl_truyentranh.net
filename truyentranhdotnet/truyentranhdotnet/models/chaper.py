from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
DeclarativeBase = declarative_base()

class Chaper(DeclarativeBase):
    __tablename__ = 'chaper'

    id = Column(Integer, primary_key=True)
    chaper_name = Column(String, index=True)
    link = Column(String)
    manga_id = Column(Integer, ForeignKey('manga.id'))
    manga = relationship("Manga", back_populates="chaper")
    content= relationship("Content", back_populates="chaper")