# main.py
from fastapi import FastAPI
from router import router
from db import Base, engine

app = FastAPI()


def create_tables():
    """
    Function to create database tables.
    """
    Base.metadata.create_all(bind=engine)


# Include the router
app.include_router(router)

# Create the tables
create_tables()
