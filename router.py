# router.py
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Dealer, Car, Customer, Sale
from schemas import (
    DealerCreate, DealerUpdate, DealerResponse,
    CarCreate, CarUpdate, CarResponse, CarListResponse,
    CustomerCreate, CustomerUpdate, CustomerResponse,
    SaleCreate, SaleUpdate, SaleResponse, SaleListResponse
)
from session import get_db

router = APIRouter()

# Dealer routes
@router.post("/dealers/", response_model=DealerResponse)
def create_dealer(dealer: DealerCreate, db: Session = Depends(get_db)):
    """
    Create a new dealer.

    Parameters:
        dealer (schemas.DealerCreate): The details of the dealer to be created.
        db (Session, optional): The database session dependency. Defaults to Depends(get_db()).

    Returns:
        schemas.DealerResponse: The details of the created dealer.
    """
    db_dealer = Dealer(**dealer.dict())
    db.add(db_dealer)
    db.commit()
    db.refresh(db_dealer)
    return db_dealer

@router.get("/dealers/", response_model=List[DealerResponse])
def get_all_dealers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Get a list of all dealers.

    Parameters:
        skip (int, optional): Number of dealers to skip. Defaults to 0.
        limit (int, optional): Maximum number of dealers to return. Defaults to 10.
        db (Session, optional): The database session dependency. Defaults to Depends(get_db()).

    Returns:
        List[schemas.DealerResponse]: List of dealers.
    """
    dealers = db.query(Dealer).offset(skip).limit(limit).all()
    return dealers

@router.get("/dealers/{dealer_id}", response_model=DealerResponse)
def read_dealer(dealer_id: int, db: Session = Depends(get_db)):
    """
    Get a dealer by ID.

    Parameters:
        dealer_id (int): The ID of the dealer to retrieve.
        db (Session, optional): The database session dependency. Defaults to Depends(get_db()).

    Returns:
        schemas.DealerResponse: Details of the requested dealer.
    """
    dealer = db.query(Dealer).filter(Dealer.id == dealer_id).first()
    if dealer is None:
        raise HTTPException(status_code=404, detail="Dealer not found")
    return dealer

@router.put("/dealers/{dealer_id}", response_model=DealerResponse)
def update_dealer(dealer_id: int, dealer: DealerUpdate, db: Session = Depends(get_db)):
    """
    Update a dealer by ID.

    Parameters:
        dealer_id (int): The ID of the dealer to update.
        dealer (schemas.DealerUpdate): The updated details of the dealer.
        db (Session, optional): The database session dependency. Defaults to Depends(get_db()).

    Returns:
        schemas.DealerResponse: Details of the updated dealer.
    """
    db_dealer = db.query(Dealer).filter(Dealer.id == dealer_id).first()
    if db_dealer is None:
        raise HTTPException(status_code=404, detail="Dealer not found")

    for key, value in dealer.dict().items():
        setattr(db_dealer, key, value)

    db.commit()
    db.refresh(db_dealer)
    return db_dealer

@router.delete("/dealers/{dealer_id}", response_model=DealerResponse)
def delete_dealer(dealer_id: int, db: Session = Depends(get_db)):
    """
    Delete a dealer by ID.

    Parameters:
        dealer_id (int): The ID of the dealer to delete.
        db (Session, optional): The database session dependency. Defaults to Depends(get_db()).

    Returns:
        schemas.DealerResponse: Details of the deleted dealer.
    """
    dealer = db.query(Dealer).filter(Dealer.id == dealer_id).first()
    if dealer is None:
        raise HTTPException(status_code=404, detail="Dealer not found")
    
    db.delete(dealer)
    db.commit()
    return dealer

# Car routes
@router.post("/cars/", response_model=CarResponse)
def create_car(car: CarCreate, db: Session = Depends(get_db)):
    """
    Create a new car.

    Parameters:
        car (schemas.CarCreate): The details of the car to be created.
        db (Session, optional): The database session dependency. Defaults to Depends(get_db()).

    Returns:
        schemas.CarResponse: The details of the created car.
    """
    db_car = Car(**car.dict())
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car

@router.get("/cars/", response_model=List[CarResponse])
def get_all_cars(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Get a list of all cars.

    Parameters:
        skip (int, optional): Number of cars to skip. Defaults to 0.
        limit (int, optional): Maximum number of cars to return. Defaults to 10.
        db (Session, optional): The database session dependency. Defaults to Depends(get_db()).

    Returns:
        List[schemas.CarResponse]: List of cars.
    """
    cars = db.query(Car).offset(skip).limit(limit).all()
    return cars

@router.get("/cars/{car_id}", response_model=CarResponse)
def read_car(car_id: int, db: Session = Depends(get_db)):
    """
    Get a car by ID.

    Parameters:
        car_id (int): The ID of the car to retrieve.
        db (Session, optional): The database session dependency. Defaults to Depends(get_db()).

    Returns:
        schemas.CarResponse: Details of the requested car.
    """
    car = db.query(Car).filter(Car.id == car_id).first()
    if car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return car

@router.put("/cars/{car_id}", response_model=CarResponse)
def update_car(car_id: int, car: CarUpdate, db: Session = Depends(get_db)):
    """
    Update a car by ID.

    Parameters:
        car_id (int): The ID of the car to update.
        car (schemas.CarUpdate): The updated details of the car.
        db (Session, optional): The database session dependency. Defaults to Depends(get_db()).

    Returns:
        schemas.CarResponse: Details of the updated car.
    """
    db_car = db.query(Car).filter(Car.id == car_id).first()
    if db_car is None:
        raise HTTPException(status_code=404, detail="Car not found")

    for key, value in car.dict().items():
        setattr(db_car, key, value)

    db.commit()
    db.refresh(db_car)
    return db_car

@router.delete("/cars/{car_id}", response_model=CarListResponse)
def delete_car(car_id: int, db: Session = Depends(get_db)):
    """
    Delete a car by ID.

    Parameters:
        car_id (int): The ID of the car to delete.
        db (Session, optional): The database session dependency. Defaults to Depends(get_db()).

    Returns:
        schemas.CarListResponse: Details of the deleted car.
    """
    car = db.query(Car).filter(Car.id == car_id).first()
    if car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    
    db.delete(car)
    db.commit()
    return car

# Customer routes
@router.post("/customers/", response_model=CustomerResponse)
def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    """
    Create a new customer.

    Parameters:
        customer (schemas.CustomerCreate): The details of the customer to be created.
        db (Session, optional): The database session dependency. Defaults to Depends(get_db()).

    Returns:
        schemas.CustomerResponse: The details of the created customer.
    """
    db_customer = Customer(**customer.dict())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

@router.get("/customers/", response_model=List[CustomerResponse])
def get_all_customers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Get a list of all customers.

    Parameters:
        skip (int, optional): Number of customers to skip. Defaults to 0.
        limit (int, optional): Maximum number of customers to return. Defaults to 10.
        db (Session, optional): The database session dependency. Defaults to Depends(get_db()).

    Returns:
        List[schemas.CustomerResponse]: List of customers.
    """
    customers = db.query(Customer).offset(skip).limit(limit).all()
    return customers

@router.get("/customers/{customer_id}", response_model=CustomerResponse)
def read_customer(customer_id: int, db: Session = Depends(get_db)):
    """
    Get a customer by ID.

    Parameters:
        customer_id (int): The ID of the customer to retrieve.
        db (Session, optional): The database session dependency. Defaults to Depends(get_db()).

    Returns:
        schemas.CustomerResponse: Details of the requested customer.
    """
    customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

@router.put("/customers/{customer_id}", response_model=CustomerResponse)
def update_customer(customer_id: int, customer: CustomerUpdate, db: Session = Depends(get_db)):
    """
    Update a customer by ID.

    Parameters:
        customer_id (int): The ID of the customer to update.
        customer (schemas.CustomerUpdate): The updated details of the customer.
        db (Session, optional): The database session dependency. Defaults to Depends(get_db()).

    Returns:
        schemas.CustomerResponse: Details of the updated customer.
    """
    db_customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")

    for key, value in customer.dict().items():
        setattr(db_customer, key, value)

    db.commit()
    db.refresh(db_customer)
    return db_customer

@router.delete("/customers/{customer_id}", response_model=CustomerResponse)
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    """
    Delete a customer by ID.

    Parameters:
        customer_id (int): The ID of the customer to delete.
        db (Session, optional): The database session dependency. Defaults to Depends(get_db()).

    Returns:
        schemas.CustomerResponse: Details of the deleted customer.
    """
    customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    
    db.delete(customer)
    db.commit()
    return customer

# Sale routes
@router.post("/sales/", response_model=SaleResponse)
def create_sale(sale: SaleCreate, db: Session = Depends(get_db)):
    """
    Create a new sale.

    Parameters:
        sale (schemas.SaleCreate): The details of the sale to be created.
        db (Session, optional): The database session dependency. Defaults to Depends(get_db()).

    Returns:
        schemas.SaleResponse: The details of the created sale.
    """
    db_sale = Sale(**sale.dict())
    db.add(db_sale)
    db.commit()
    db.refresh(db_sale)
    return db_sale

@router.get("/sales/", response_model=List[SaleResponse])
def get_all_sales(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Get a list of all sales.

    Parameters:
        skip (int, optional): Number of sales to skip. Defaults to 0.
        limit (int, optional): Maximum number of sales to return. Defaults to 10.
        db (Session, optional): The database session dependency. Defaults to Depends(get_db()).

    Returns:
        List[schemas.SaleResponse]: List of sales.
    """
    sales = db.query(Sale).offset(skip).limit(limit).all()
    return sales

@router.get("/sales/{sale_id}", response_model=SaleResponse)
def read_sale(sale_id: int, db: Session = Depends(get_db)):
    """
    Get a sale by ID.

    Parameters:
        sale_id (int): The ID of the sale to retrieve.
        db (Session, optional): The database session dependency. Defaults to Depends(get_db()).

    Returns:
        schemas.SaleResponse: Details of the requested sale.
    """
    sale = db.query(Sale).filter(Sale.id == sale_id).first()
    if sale is None:
        raise HTTPException(status_code=404, detail="Sale not found")
    return sale

@router.put("/sales/{sale_id}", response_model=SaleResponse)
def update_sale(sale_id: int, sale: SaleUpdate, db: Session = Depends(get_db)):
    """
    Update a sale by ID.

    Parameters:
        sale_id (int): The ID of the sale to update.
        sale (schemas.SaleUpdate): The updated details of the sale.
        db (Session, optional): The database session dependency. Defaults to Depends(get_db()).

    Returns:
        schemas.SaleResponse: Details of the updated sale.
    """
    db_sale = db.query(Sale).filter(Sale.id == sale_id).first()
    if db_sale is None:
        raise HTTPException(status_code=404, detail="Sale not found")

    for key, value in sale.dict().items():
        setattr(db_sale, key, value)

    db.commit()
    db.refresh(db_sale)
    return db_sale

@router.delete("/sales/{sale_id}", response_model=SaleListResponse)
def delete_sale(sale_id: int, db: Session = Depends(get_db)):
    """
    Delete a sale by ID.

    Parameters:
        sale_id (int): The ID of the sale to delete.
        db (Session, optional): The database session dependency. Defaults to Depends(get_db()).

    Returns:
        schemas.SaleListResponse: Details of the deleted sale.
    """
    sale = db.query(Sale).filter(Sale.id == sale_id).first()
    if sale is None:
        raise HTTPException(status_code=404, detail="Sale not found")
    
    db.delete(sale)
    db.commit()
    return sale
