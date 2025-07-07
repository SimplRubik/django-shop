# Django Shop

This is an online shop web application built with Django.


- Product catalog with categories
- Product detail pages with image slider
- Add products to cart
- Update quantities in cart
- Checkout process with order creation
- Order history for logged-in users
- User registration and login (including Google login via Django Allauth)
- Search products by name or description
- User reviews for products
- Responsive design with Bootstrap

---


- Python 3.13
- Django 5.2
- SQLite (development database)
- Bootstrap 5.3
- Django Allauth (for social login)

---


## ⚙️ How to Run

Here’s how you can set up and run this project from scratch:

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
# source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser

# Start the development server
python manage.py runserver

## To Do

- Add payment gateway
- Add more filters for products
- Improve UI design
