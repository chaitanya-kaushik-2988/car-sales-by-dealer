# schemas.py
from datetime import date
from pydantic import BaseModel
from typing import List, Optional


class DealerBase(BaseModel):
    """
    Base schema for a dealer.

    Attributes:
        name (str): The name of the dealer.
        location (str): The location of the dealer.
        contact_info (Optional[str]): Optional contact information for the dealer.
    """
    name: str
    location: str
    contact_info: Optional[str]


class DealerCreate(DealerBase):
    """
    Schema for creating a new dealer, inherits from DealerBase.
    """
    pass


class DealerUpdate(DealerBase):
    """
    Schema for updating an existing dealer, inherits from DealerBase.
    """
    pass


class DealerResponse(BaseModel):
    """
    Response schema for a dealer, includes related cars and sales.

    Attributes:
        id (int): The unique identifier for the dealer.
        name (str): The name of the dealer.
        location (str): The location of the dealer.
        contact_info (Optional[str]): Optional contact information for the dealer.
        cars (List["CarListResponse"]): List of related cars.
        sales (List["SaleResponse"]): List of related sales.
    """
    id: int
    name: str
    location: str
    contact_info: Optional[str]
    cars: List["CarListResponse"] = []
    sales: List["SaleResponse"] = []


class DealerListResponse(BaseModel):
    """
    Response schema for a list of dealers.

    Attributes:
        id (int): The unique identifier for the dealer.
        name (str): The name of the dealer.
        location (str): The location of the dealer.
        contact_info (Optional[str]): Optional contact information for the dealer.
    """
    id: int
    name: str
    location: str
    contact_info: Optional[str]


class CarBase(BaseModel):
    """
    Base schema for a car.

    Attributes:
        make (str): The make of the car.
        model (str): The model of the car.
        year (int): The year of the car.
        color (str): The color of the car.
        vin (str): The Vehicle Identification Number (VIN) of the car.
        price (float): The price of the car.
    """
    make: str
    model: str
    year: int
    color: str
    vin: str
    price: float


class CarCreate(CarBase):
    """
    Schema for creating a new car, inherits from CarBase.

    Attributes:
        dealer_id (int): The identifier of the dealer associated with the car.
    """
    dealer_id: int


class CarUpdate(CarBase):
    """
    Schema for updating an existing car, inherits from CarBase.
    """
    pass


class CarResponse(BaseModel):
    """
    Response schema for a car, includes information about its dealer.

    Attributes:
        id (int): The unique identifier for the car.
        make (str): The make of the car.
        model (str): The model of the car.
        year (int): The year of the car.
        color (str): The color of the car.
        vin (str): The Vehicle Identification Number (VIN) of the car.
        price (float): The price of the car.
        dealer (Optional[DealerResponse]): Information about the car's dealer.
    """
    id: int
    make: str
    model: str
    year: int
    color: str
    vin: str
    price: float
    dealer: Optional[DealerResponse]


class CarListResponse(BaseModel):
    """
    Response schema for a list of cars.

    Attributes:
        id (int): The unique identifier for the car.
        make (str): The make of the car.
        model (str): The model of the car.
        year (int): The year of the car.
        color (str): The color of the car.
        vin (str): The Vehicle Identification Number (VIN) of the car.
        price (float): The price of the car.
    """
    id: int
    make: str
    model: str
    year: int
    color: str
    vin: str
    price: float


class CustomerBase(BaseModel):
    """
    Base schema for a customer.

    Attributes:
        first_name (str): The first name of the customer.
        last_name (str): The last name of the customer.
        contact_info (Optional[str]): Optional contact information for the customer.
        address (Optional[str]): Optional address of the customer.
    """
    first_name: str
    last_name: str
    contact_info: Optional[str]
    address: Optional[str]


class CustomerCreate(CustomerBase):
    """
    Schema for creating a new customer, inherits from CustomerBase.
    """
    pass


class CustomerUpdate(CustomerBase):
    """
    Schema for updating an existing customer, inherits from CustomerBase.
    """
    pass


class CustomerResponse(BaseModel):
    """
    Response schema for a customer, includes information about its sales.

    Attributes:
        id (int): The unique identifier for the customer.
        first_name (str): The first name of the customer.
        last_name (str): The last name of the customer.
        contact_info (Optional[str]): Optional contact information for the customer.
        address (Optional[str]): Optional address of the customer.
        sales (List["SaleResponse"]): List of sales associated with the customer.
    """
    id: int
    first_name: str
    last_name: str
    contact_info: Optional[str]
    address: Optional[str]
    sales: List["SaleResponse"] = []


class CustomerListResponse(BaseModel):
    """
    Response schema for a list of customers.

    Attributes:
        id (int): The unique identifier for the customer.
        first_name (str): The first name of the customer.
        last_name (str): The last name of the customer.
        contact_info (Optional[str]): Optional contact information for the customer.
        address (Optional[str]): Optional address of the customer.
    """
    id: int
    first_name: str
    last_name: str
    contact_info: Optional[str]
    address: Optional[str]


class SaleBase(BaseModel):
    """
    Base schema for a sale.

    Attributes:
        sale_date (date): The date of the sale.
        sale_amount (float): The amount of the sale.
        payment_method (str): The payment method used for the sale.
    """
    sale_date: date
    sale_amount: float
    payment_method: str


class SaleCreate(SaleBase):
    """
    Schema for creating a new sale, inherits from SaleBase.

    Attributes:
        dealer_id (int): The identifier of the dealer associated with the sale.
        car_id (int): The identifier of the car associated with the sale.
        customer_id (int): The identifier of the customer associated with the sale.
    """
    dealer_id: int
    car_id: int
    customer_id: int


class SaleUpdate(SaleBase):
    """
    Schema for updating an existing sale, inherits from SaleBase.
    """
    pass


class SaleResponse(BaseModel):
    """
    Response schema for a sale, includes information about its dealer, car, and customer.

    Attributes:
        id (int): The unique identifier for the sale.
        sale_date (date): The date of the sale.
        sale_amount (float): The amount of the sale.
        payment_method (str): The payment method used for the sale.
        dealer (Optional[DealerListResponse]): Information about the sale's dealer.
        car (Optional[CarListResponse]): Information about the sale's car.
        customer (Optional[CustomerListResponse]): Information about the sale's customer.
    """
    id: int
    sale_date: date
    sale_amount: float
    payment_method: str
    dealer: Optional[DealerListResponse]
    car: Optional[CarListResponse]
    customer: Optional[CustomerListResponse]


class SaleListResponse(BaseModel):
    """
    Response schema for a list of sales.

    Attributes:
        id (int): The unique identifier for the sale.
        sale_date (date): The date of the sale.
        sale_amount (float): The amount of the sale.
        payment_method (str): The payment method used for the sale.
    """
    id: int
    sale_date: date
    sale_amount: float
    payment_method: str
