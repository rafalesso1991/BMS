from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

# Create DB in memory
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost:5435/bookstore"#"DMS://user:pass@URL:port/db"

# Create DB Engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create DB Session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create Base SQLAlchemy Model
Base = declarative_base()

# Function that returns DB Session
def get_db():
    db = SessionLocal()
    """
    Context Manager for accessing a db session.
    -
    Yields:
        SessionLocal: A SQLAlchemy db session object
    -
    Usage:
        Use this function to obtain a db session.
        The session is yielded within a `with` block.
        Once the block exits, the session is automatically closed,
        ensuring proper connection management and resource cleanup.
    """
    try:
        yield db
    finally:
        db.close()
