from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from database_management import Base
from datetime import datetime


class Messages(Base):
    __tablename__ = "Messages"

    id = Column(Integer, primary_key=True, index=True)
    sender_id = Column(Integer, ForeignKey("Users.id"), index=True)
    receiver_id = Column(Integer, ForeignKey("Users.id"), index=True)
    listing_id = Column(Integer, ForeignKey("Listings.id"), nullable=True, index=True)
    message_text = Column(Text)
    sent_at = Column(DateTime, default=datetime.utcnow)
    read_at = Column(DateTime, nullable=True)

    sender = relationship("Users", foreign_keys=[sender_id], back_populates="sent_messages")
    receiver = relationship("Users", foreign_keys=[receiver_id], back_populates="received_messages")
    listing = relationship("Listings")
