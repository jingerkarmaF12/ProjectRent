from sqlalchemy import Column, String, Float, Integer, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from database_management import Base
from datetime import datetime


class Users(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True, index=True)
    phone_number = Column(String)
    password_hash = Column(String)
    university = Column(String)
    study_program = Column(String)
    age = Column(Integer)
    gender = Column(String, nullable=True)
    bio = Column(Text, nullable=True)
    profile_picture_url = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    listings = relationship("Listings", back_populates="creator")
    applications = relationship("Applications", back_populates="applicant")
    favorites = relationship("Favorites", back_populates="user")
    sent_messages = relationship("Messages", foreign_keys="Messages.sender_id", back_populates="sender")
    received_messages = relationship("Messages", foreign_keys="Messages.receiver_id", back_populates="receiver")
    reports = relationship("Reports", back_populates="reporter")
