from app.db.database import Base, engine, SessionLocal
from app.models.user import User, Role, UserRole
from app.core.security import get_password_hash

def init_db():
    """Initialize the database with default data."""
    # Create all tables
    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    
    try:
        # Create default roles
        roles = {
            role: Role(name=role) 
            for role in UserRole
        }
        
        # Add roles to database
        for role in roles.values():
            db.add(role)
        
        # Create admin user if not exists
        admin_email = "admin@quarry.com"
        admin_user = db.query(User).filter(User.email == admin_email).first()
        
        if not admin_user:
            admin_user = User(
                email=admin_email,
                hashed_password=get_password_hash("admin123"),
                first_name="Admin",
                last_name="User",
                is_active=True,
                is_verified=True
            )
            admin_user.roles = [roles[UserRole.ADMIN]]
            db.add(admin_user)
        
        db.commit()
        print("✅ Database initialized successfully!")
        
    except Exception as e:
        db.rollback()
        print(f"❌ Error initializing database: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    print("Initializing database...")
    init_db()
