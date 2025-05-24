import asyncio
from app.db.database import get_db, create_tables
from app.models.user import User
from app.schemas.user import UserCreate
from app.crud.user import create_user, get_user_by_email

async def test_user_creation():
    # Create tables
    await create_tables()
    
    # Test user data
    user_data = UserCreate(
        email="test@example.com",
        full_name="Test User",
        password="testpassword123"
    )
    
    # Create user
    async for db in get_db():
        user = await create_user(db, user_data)
        print(f"Created user: {user}")
        
        # Retrieve user
        db_user = await get_user_by_email(db, email=user_data.email)
        print(f"Retrieved user: {db_user}")

if __name__ == "__main__":
    asyncio.run(test_user_creation())
