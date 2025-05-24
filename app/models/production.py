from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base_class import Base

class ProductionRecord(Base):
    __tablename__ = "production_records"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, server_default=func.now(), index=True)
    quantity = Column(Float, nullable=False)  # in tons
    quarry_id = Column(Integer, ForeignKey("quarries.id"), nullable=False)
    material_id = Column(Integer, ForeignKey("materials.id"), nullable=False)
    equipment_id = Column(Integer, ForeignKey("equipment.id"))
    operator_id = Column(Integer, ForeignKey("users.id"))
    notes = Column(String(500))
    
    # Relationships
    quarry = relationship("Quarry", back_populates="production_records")
    material = relationship("Material")
    equipment = relationship("Equipment")
    operator = relationship("User")
