# Shopify App Oauth

This project includes the implementation of Shopify OAuth flow by using Django REST Framework.

## Getting Started

This project works on **Python 3+** and **Django 3.1.3**. 

In `settings.py` set your apps API credentials:

```
SHOPIFY_PUBLIC_APP_KEY = "YOUR_API_KEY"
SHOPIFY_PUBLIC_APP_SECRET_KEY = "YOUR_API_SECRET_KEY"
```
then run the server

```
python manage.py runserver
```

Please read the realted article for more information:

[Create Shopify App with Python/Django](https://thepylot.dev)
