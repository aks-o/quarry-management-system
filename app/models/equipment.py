from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.db.base_class import Base
import enum

class EquipmentStatus(str, enum.Enum):
    OPERATIONAL = "operational"
    MAINTENANCE = "maintenance"
    DECOMMISSIONED = "decommissioned"

class EquipmentType(str, enum.Enum):
    EXCAVATOR = "excavator"
    DUMP_TRUCK = "dump_truck"
    CRUSHER = "crusher"
    LOADER = "loader"
    DRILL = "drill"

class Equipment(Base):
    __tablename__ = "equipment"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True, nullable=False)
    equipment_type = Column(Enum(EquipmentType), nullable=False)
    model = Column(String(100))
    serial_number = Column(String(100), unique=True)
    status = Column(Enum(EquipmentStatus), default=EquipmentStatus.OPERATIONAL)
    purchase_date = Column(DateTime)
    last_maintenance = Column(DateTime)
    next_maintenance = Column(DateTime)
    quarry_id = Column(Integer, ForeignKey("quarries.id"))
    
    # Relationships
    quarry = relationship("Quarry", back_populates="equipment")
    maintenance_records = relationship("MaintenanceRecord", back_populates="equipment")
