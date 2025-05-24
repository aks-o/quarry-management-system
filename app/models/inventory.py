from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base_class import Base

class Inventory(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True, index=True)
    material_id = Column(Integer, ForeignKey("materials.id"), unique=True)
    quantity = Column(Float, default=0.0)  # in tons
    last_updated = Column(DateTime, server_default=func.now(), onupdate=func.now())
    threshold = Column(Float, default=100.0)  # reorder threshold in tons
    
    # Relationships
    material = relationship("Material", back_populates="inventory")
