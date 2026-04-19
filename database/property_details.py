from sqlalchemy import Column, String, Float, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from database_management import Base


class PropertyDetails(Base):
    __tablename__ = "PropertyDetails"

    id = Column(Integer, primary_key=True, index=True)
    listing_id = Column(Integer, ForeignKey("Listings.id"), unique=True, index=True)
    size_sqm = Column(Float)
    number_of_rooms = Column(Integer)
    number_of_bathrooms = Column(Integer)
    floor = Column(Integer)
    has_wifi = Column(Boolean, default=False)
    has_washing_machine = Column(Boolean, default=False)
    has_kitchen = Column(Boolean, default=False)
    pets_allowed = Column(Boolean, default=False)

    listing = relationship("Listings", back_populates="property_details")
