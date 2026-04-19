from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database_management import Base
from datetime import datetime


class GroupListings(Base):
    __tablename__ = "GroupListings"

    id = Column(Integer, primary_key=True, index=True)
    group_id = Column(Integer, ForeignKey("WhatsAppGroups.id"), index=True)
    listing_id = Column(Integer, ForeignKey("Listings.id"), index=True)
    extracted_at = Column(DateTime, default=datetime.utcnow)

    group = relationship("WhatsAppGroups", back_populates="listings")
    listing = relationship("Listings", back_populates="whatsapp_groups")
