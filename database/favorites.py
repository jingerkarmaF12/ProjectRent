from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database_management import Base
from datetime import datetime


class Favorites(Base):
    __tablename__ = "Favorites"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("Users.id"), index=True)
    listing_id = Column(Integer, ForeignKey("Listings.id"), index=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("Users", back_populates="favorites")
    listing = relationship("Listings", back_populates="favorites")
