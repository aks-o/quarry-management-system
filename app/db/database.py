from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from sqlalchemy.ext.declarative import declarative_base
from app.core.config import settings

# Create async engine
engine = create_async_engine(
    settings.SQLALCHEMY_DATABASE_URL,
    echo=True,
    future=True,
    pool_pre_ping=True,
    poolclass=NullPool
)

# Create async session factory
async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False, autoflush=False
)

# Dependency to get DB session
async def get_db() -> AsyncSession:
    """
    Dependency function that yields db sessions
    """
    async with async_session() as session:
        yield session
        await session.close()

# Function to create all tables
async def create_tables():
    from app.models.base import Base
    from app.models.user import User
    from app.models.quarry import Quarry
    from app.models.material import Material
    from app.models.equipment import Equipment
    from app.models.production import ProductionRecord
    from app.models.inventory import Inventory
    from app.models.maintenance import MaintenanceRecord
    
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
