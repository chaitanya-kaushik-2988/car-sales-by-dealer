from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from db import Base


class Dealer(Base):
    """
    Represents a car dealer.

    Attributes:
        id (int): The unique identifier for the dealer.
        name (str): The name of the dealer.
        location (str): The location of the dealer.
        contact_info (str): The contact information for the dealer.
        cars (relationship): Relationship to the cars associated with this dealer.
        sales (relationship): Relationship to the sales associated with this dealer.
    """
    __tablename__ = "dealers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    location = Column(String)
    contact_info = Column(String)

    cars = relationship("Car", back_populates="dealer")
    sales = relationship("Sale", back_populates="dealer")


class Car(Base):
    """
    Represents a car.

    Attributes:
        id (int): The unique identifier for the car.
        make (str): The make of the car.
        model (str): The model of the car.
        year (int): The year of the car.
        color (str): The color of the car.
        vin (str): The Vehicle Identification Number (VIN) of the car.
        price (float): The price of the car.
        dealer_id (int): The foreign key to associate the car with a dealer.
        dealer (relationship): Relationship to the dealer associated with this car.
        sale (relationship): Relationship to the sale associated with this car.
    """
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True, index=True)
    make = Column(String)
    model = Column(String)
    year = Column(Integer)
    color = Column(String)
    vin = Column(String, unique=True, index=True)
    price = Column(Float)

    dealer_id = Column(Integer, ForeignKey("dealers.id"))
    dealer = relationship("Dealer", back_populates="cars")
    sale = relationship("Sale", uselist=False, back_populates="car")


class Customer(Base):
    """
    Represents a customer.

    Attributes:
        id (int): The unique identifier for the customer.
        first_name (str): The first name of the customer.
        last_name (str): The last name of the customer.
        contact_info (str): The contact information for the customer.
        address (str): The address of the customer.
        sales (relationship): Relationship to the sales associated with this customer.
    """
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    contact_info = Column(String)
    address = Column(String)

    sales = relationship("Sale", back_populates="customer")


class Sale(Base):
    """
    Represents a sale.

    Attributes:
        id (int): The unique identifier for the sale.
        sale_date (Date): The date of the sale.
        sale_amount (float): The amount of the sale.
        payment_method (str): The payment method used for the sale.
        dealer_id (int): The foreign key to associate the sale with a dealer.
        dealer (relationship): Relationship to the dealer associated with this sale.
        car_id (int): The foreign key to associate the sale with a car.
        car (relationship): Relationship to the car associated with this sale.
        customer_id (int): The foreign key to associate the sale with a customer.
        customer (relationship): Relationship to the customer associated with this sale.
    """
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)
    sale_date = Column(Date)
    sale_amount = Column(Float)
    payment_method = Column(String)

    dealer_id = Column(Integer, ForeignKey("dealers.id"))
    dealer = relationship("Dealer", back_populates="sales")

    car_id = Column(Integer, ForeignKey("cars.id"))
    car = relationship("Car", back_populates="sale")

    customer_id = Column(Integer, ForeignKey("customers.id"))
    customer = relationship("Customer", back_populates="sales")
