from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database_management import Base
from datetime import datetime


class ListingImages(Base):
    __tablename__ = "ListingImages"

    id = Column(Integer, primary_key=True, index=True)
    listing_id = Column(Integer, ForeignKey("Listings.id"), index=True)
    image_url = Column(String)
    uploaded_at = Column(DateTime, default=datetime.utcnow)

    listing = relationship("Listings", back_populates="images")
