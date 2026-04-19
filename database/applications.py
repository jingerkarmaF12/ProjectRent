from sqlalchemy import Column, String, Float, Integer, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from database_management import Base
from datetime import datetime


class Applications(Base):
    __tablename__ = "Applications"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("Users.id"), index=True)
    listing_id = Column(Integer, ForeignKey("Listings.id"), index=True)
    message = Column(Text, nullable=True)
    status = Column(String, default="pending")  # pending / accepted / rejected
    created_at = Column(DateTime, default=datetime.utcnow)

    applicant = relationship("Users", back_populates="applications")
    listing = relationship("Listings", back_populates="applications")
