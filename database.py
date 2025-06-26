from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# SQLite database engine (file-based)
engine = create_engine("sqlite:///./users.db")

# Session factory bound to the engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for model definitions
Base = declarative_base()

# User model mapped to 'users' table
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)  # Unique user ID
    email = Column(String, unique=True, index=True, nullable=False)  # User email
    password_hash = Column(String, nullable=False)  # Hashed password
    first_name = Column(String, nullable=False)  # First name
    last_name = Column(String, nullable=False)  # Last name
    interests = Column(String)  # Optional user interests

# Create tables in the database
def init_db():
    Base.metadata.create_all(bind=engine)

# Dependency to get a DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()