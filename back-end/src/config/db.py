from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
# Create DB in memory
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost:5435/books"#"DMS://username:password@URL:port/database"
# Create DB Engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)
# Create DB Session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Create Base SQLAlchemy Model
Base = declarative_base()
# Function that returns DB Session
def get_db():
    db = SessionLocal() 
    try:
        yield db
    finally:
        db.close()