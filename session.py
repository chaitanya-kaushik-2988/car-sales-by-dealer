from db import SessionLocal

def get_db():
    """
    Generator function to obtain a database session using SessionLocal.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
