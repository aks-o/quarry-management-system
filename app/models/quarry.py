from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Enum, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base_class import Base
import enum

class QuarryStatus(str, enum.Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    MAINTENANCE = "maintenance"

class Quarry(Base):
    __tablename__ = "quarries"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True, nullable=False)
    location = Column(String(200))
    status = Column(Enum(QuarryStatus), default=QuarryStatus.ACTIVE)
    area = Column(Float)  # in square meters
    capacity = Column(Float)  # in tons
    description = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    manager_id = Column(Integer, ForeignKey("users.id"))
    manager = relationship("User", back_populates="managed_quarries")
    materials = relationship("Material", back_populates="quarry")
    equipment = relationship("Equipment", back_populates="quarry")
    production_records = relationship("ProductionRecord", back_populates="quarry")
