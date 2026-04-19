from sqlalchemy import Column, String, Float, Integer, ForeignKey, DateTime, Text, Boolean
from sqlalchemy.orm import relationship
from database_management import Base
from datetime import datetime


class Listings(Base):
    __tablename__ = "Listings"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(Text)
    rent_price = Column(Float)
    deposit = Column(Float)
    city = Column(String)
    address = Column(String)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    available_from = Column(DateTime)
    available_to = Column(DateTime, nullable=True)
    room_type = Column(String)
    furnished = Column(Boolean, default=False)
    utilities_included = Column(Boolean, default=False)
    created_by = Column(Integer, ForeignKey("Users.id"), index=True)
    source = Column(String, default="WhatsApp")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    creator = relationship("Users", back_populates="listings")
    property_details = relationship("PropertyDetails", back_populates="listing", uselist=False)
    images = relationship("ListingImages", back_populates="listing")
    applications = relationship("Applications", back_populates="listing")
    favorites = relationship("Favorites", back_populates="listing")
    whatsapp_groups = relationship("GroupListings", back_populates="listing")
    reports = relationship("Reports", back_populates="listing")
