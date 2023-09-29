# Handmade E-Commerce Website

Welcome to the Handmade E-Commerce Website project! This is a simple platform designed for buying and selling handmade
products. This README will guide you through the project structure, how to run the application, and provide a brief
overview of its functionality.

## Table of Contents

- [Story](#Story)
- [Project Overview](#project-overview)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Contributing](#contributing)
- [License](#license)

## Story

I always thought about something that can connect talents to the world and to each other. Seeing a lot of talented and
passionate people around me loose their passion and abandon their talent because they saw it has no use in the real
world was breaking my heart. In other hand I saw a lot of people that really appreciate talents and are passionate about
art and handmade products. So I thought why not to connect those two people together and also connect other talents with
each other! That's why I made Handmade website, it doesn't have user and seller paradigm, all are just users, user can
buy and can sell, that's how I wanted to connect people to each other.

## Project Overview

Handmade is a web-based platform that allows users to explore and purchase unique, handmade products created by talented
artisans. This project is built using Flask, a Python web framework, and leverages a relational database to manage user
accounts, product listings, shopping carts, reviews, and product categories.

**Key features** of the Handmade E-Commerce Website include:

- User registration and authentication
- Product listing and browsing by category
- Shopping cart management
- Product reviews and ratings
- Secure payment processing (not implemented yet in this example)
- Product categories (not implemented yet in this example)
- Admin panel for managing products and categories (not implemented yet in this example)

## Project Structure

The project is organized into the following directories and files:

- **models**: Contains the database models, including User, Product, Cart, Review, and Category.

    - **engine**: Houses the `DBStorage` class, responsible for handling database operations.

- **test_data**: Includes a `test_data.py` script for generating and populating test data into the database.

- **web_flask**: This directory contains the core of the web application.

    - **main.py**: Defines main Flask routes and serves as the entry point for the application.

    - **forms.py**: Contains FlaskForm classes for defining web forms used in the application.
    - **views**: Contains all files that defines other routes and register it with blueprint

## Some Files Structure

### Models

| File                                                                                        | Description                                                         |
|---------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| [__init__.py](https://github.com/mostafaehab96/Handmade/blob/master/models/__init__.py)     | Package initialization file contains singleton storage instance     |
| [base_model.py](https://github.com/mostafaehab96/Handmade/blob/master/models/base_model.py) | Contians BaseModel class that is the parent of all other classes    |
| [cart.py](https://github.com/mostafaehab96/Handmade/blob/master/models/cart.py)             | Contains Cart class and products_cart secondary table               |
| [category.py](https://github.com/mostafaehab96/Handmade/blob/master/models/category.py)     | Contains Category class                                             |
| [order.py](https://github.com/mostafaehab96/Handmade/blob/master/models/order.py)           | Contains Order class and orders_products secondary table            |
| [product.py](https://github.com/mostafaehab96/Handmade/blob/master/models/product.py)       | Contains Product class and products_categories secondary table      |
| [review.py](https://github.com/mostafaehab96/Handmade/blob/master/models/review.py)         | Contains Review class                                               |
| [user.py](https://github.com/mostafaehab96/Handmade/blob/master/models/user.py)             | Contains User class                                                 |
| [engine](https://github.com/mostafaehab96/Handmade/blob/master/models/engine)               | This is a directory that holds files that handles storage behaviors |

### Web Flask

| File                                                                                             | Description                                                                       |
|--------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| [__init__.py](https://github.com/mostafaehab96/Handmade/blob/master/web_flask/views/__init__.py) | Package initialization file the defines the blueprint and imports all other files |
| [account.py](https://github.com/mostafaehab96/Handmade/blob/master/web_flask/views/account.py)   | Contains routes that handles account functionality                                |
| [cart.py](https://github.com/mostafaehab96/Handmade/blob/master/web_flask/views/cart.py)         | Contains routes that handles all cart functionality                               |
| [login.py](https://github.com/mostafaehab96/Handmade/blob/master/web_flask/views/login.py)       | Contains routes that handles login,logout and signup                              |
| [orders.py](https://github.com/mostafaehab96/Handmade/blob/master/web_flask/views/orders.py)     | Contains routes that handles all order functionality                              |
| [products.py](https://github.com/mostafaehab96/Handmade/blob/master/web_flask/views/products.py) | Contains routes that handles all product and reviews functionality                |

## Contribution

My dear friend [Islam Gamel](https://github.com/IslamMGM) helped me in all frontend! He made all html, css files and
styling with js and pagination without using any external library.


