import asyncio
from app.core.config import settings
from app.crud import user as crud_user
from app.schemas.user import UserCreate
from app.db.session import get_db

async def create_first_superuser():
    db = get_db()
    async with db as session:
        user = await crud_user.get_by_email(session, email=settings.FIRST_SUPERUSER_EMAIL)
        if not user:
            user_in = UserCreate(
                email=settings.FIRST_SUPERUSER_EMAIL,
                password=settings.FIRST_SUPERUSER_PASSWORD,
                full_name="Initial Admin",
                is_superuser=True,
            )
            await crud_user.create(session, obj_in=user_in)
            print("✅ Created initial superuser")
        else:
            print("ℹ️  Superuser already exists")

if __name__ == "__main__":
    asyncio.run(create_first_superuser())
