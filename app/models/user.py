from sqlalchemy import Boolean, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base_class import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String, index=True)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationships
    managed_quarries = relationship("Quarry", back_populates="manager")
    maintenance_records = relationship("MaintenanceRecord", back_populates="technician")
    production_records = relationship("ProductionRecord", back_populates="operator")

    def __repr__(self):
        return f"<User {self.email}>"

class UserCreate(Base):
    email: str
    password: str
    full_name: str
    is_superuser: bool = False

class UserUpdate(Base):
    email: str = None
    password: str = None
    full_name: str = None
    is_active: bool = None

class UserInDB(User):
    hashed_password: str
