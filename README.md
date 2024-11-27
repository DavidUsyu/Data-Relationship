# E-Commerce Django Project

## Description
This project implements a basic E-Commerce system in Django with two models:
1. **Customer**: Represents a customer with `name` and `email`.
2. **Order**: Represents an order placed by a customer, including `order_date` and `total_amount`.

## Setup Instructions

### Prerequisites
- Python 3.x
- Django 4.x
- Git

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd <repository_folder>
2.Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
````
3.Install dependencies:
```bash 
pip install -r requirements.txt
````
4.Apply migrations:
```bash
python manage.py migrate
````
5.Run the development server:
```bash
python manage.py runserver
