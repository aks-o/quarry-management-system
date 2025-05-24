from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class Material(Base):
    __tablename__ = "materials"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True, nullable=False)
    description = Column(String(500))
    density = Column(Float)  # kg/m³
    quarry_id = Column(Integer, ForeignKey("quarries.id"))
    
    # Relationships
    quarry = relationship("Quarry", back_populates="materials")
    inventory = relationship("Inventory", back_populates="material", uselist=False)
