from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from database_management import Base
from datetime import datetime


class Reports(Base):
    __tablename__ = "Reports"

    id = Column(Integer, primary_key=True, index=True)
    reported_by = Column(Integer, ForeignKey("Users.id"), index=True)
    listing_id = Column(Integer, ForeignKey("Listings.id"), index=True)
    reason = Column(String)
    description = Column(Text, nullable=True)
    status = Column(String, default="pending")  # pending / resolved / dismissed
    created_at = Column(DateTime, default=datetime.utcnow)

    reporter = relationship("Users", back_populates="reports")
    listing = relationship("Listings", back_populates="reports")
