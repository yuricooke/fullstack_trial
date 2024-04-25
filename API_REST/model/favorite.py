from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from model import Base

class Favorite(Base):
    __tablename__ = 'favorites'

    user_id = Column(Integer, ForeignKey('user.user_id'), primary_key=True)
    hike_id = Column(Integer, ForeignKey('hike.hike_id'), primary_key=True)

    user = relationship("User", back_populates="favorites")
    hike = relationship("Hike", back_populates="favorites")