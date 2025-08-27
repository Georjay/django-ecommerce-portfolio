# E-commerce Platform

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)


A full-featured Django-based e-commerce solution with user authentication, product management, shopping cart functionality, and order management system.

## Features

- **User Authentication**: Registration, login, and profile management
- **Product Catalog**: Browse products with categories and search functionality
- **Shopping Cart**: Add, remove, and update items with real-time calculations
- **Order Management**: Complete checkout process with order history
- **Admin Panel**: Django admin interface for managing products and orders
- **Responsive Design**: Mobile-friendly interface built with Bootstrap

## Technologies Used

- **Backend**: Django, Python
- **Frontend**: HTML, CSS, Bootstrap, JavaScript
- **Database**: SQLite (development) / PostgreSQL (production ready)
- **Authentication**: Django's built-in authentication system

## Installation

1. Clone the repository
```bash
git clone https://github.com/Georjay/django-ecommerce-portfolio.git
cd ecommerce-platform
```

2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run migrations
```bash
python manage.py migrate
```

5. Create a superuser
```bash
python manage.py createsuperuser
```

6. Start the development server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` to view the application.

## Usage

- Browse products as a guest user
- Register/login to add items to cart
- Complete purchases through the checkout process
- Access admin panel at `/admin` to manage products and orders

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License.
