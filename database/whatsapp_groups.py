from sqlalchemy import Column, String, Integer, DateTime, Text
from sqlalchemy.orm import relationship
from database_management import Base
from datetime import datetime


class WhatsAppGroups(Base):
    __tablename__ = "WhatsAppGroups"

    id = Column(Integer, primary_key=True, index=True)
    group_name = Column(String)
    group_link = Column(String)
    city = Column(String)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    listings = relationship("GroupListings", back_populates="group")
