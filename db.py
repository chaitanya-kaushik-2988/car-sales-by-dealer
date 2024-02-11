from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# The URL for the database.
DATABASE_URL = "sqlite:///./car_sales.db"

# Create an engine that connects to the database specified by DATABASE_URL.
engine = create_engine(DATABASE_URL)

# Create a session class that represents a "holding zone" for objects to be
# written to or read from the database.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# A base class for declarative class definitions.
Base = declarative_base()
