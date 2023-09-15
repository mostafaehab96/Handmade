from faker import Faker
from models.user import User
from models.product import Product
from models.order import Order
from models.review import Review
from models.category import Category
from models.cart import Cart
from models import storage
import random


fake = Faker()



def create_users():
    for _ in range(15):
        user = User(
            name=fake.name(),
            email=fake.email(),
            password=fake.password(),
            address=fake.address(),
            postal_code="44511",
            about=fake.text(),
            cart=Cart()
        )
        user.save()


def create_products():
    with open("test_data/test_images.txt", "r") as file:
        images = file.readlines()
    users = storage.all("User")
    count = 0
    for user in users:
        r = random.randint(1, 5)
        for _ in range(r):
            user.products.append(Product(
                name=fake.color_name(),
                description=fake.text(),
                image=images[count],
                price=float(random.randint(10, 100))
            ))
            count += 1
    storage.save()


def create_orders():
    users = storage.all("User")
    for _ in range(100):
        user = random.choice(users)
        order = Order(
            address=fake.address(),
            total_price=float(random.randint(10, 100)),
            user_id=user.id,
        )
        storage.new(order)


def create_reviews():
    users = storage.all("User")
    products = storage.all("Product")

    for _ in range(100):
        user = random.choice(users)
        product = random.choice(products)
        review = Review(
            text=fake.text(),
            user_id=user.id,
            product_id=product.id,
            rating=random.randint(1, 5)
        )

        review.save()
    storage.save()


def create_order_products():
    orders = storage.all("Order")
    products = storage.all("Product")
    for order in orders:
        # select random k
        k = random.randint(1, 3)
        # select random products
        purchased_products = random.sample(products, k)
        order.total_price = sum([product.price for product in purchased_products])
        order.products.extend(purchased_products)
        order.save()
    storage.save()


def create_categories():
    categories = [
        "Jewelry",
        "Clothing",
        "Home Decor",
        "Beauty and Personal Care",
        "Accessories",
        "Stationery",
        "Toys and Games",
        "Kitchen and Dining",
        "Pet Supplies",
        "Holiday and Seasonal",
        "Craft Supplies",
        "Gifts for Special Occasions"
    ]
    for category in categories:
        new = Category(name=category)
        new.save()


def create_product_categories():
    products = storage.all("Product")
    categories = storage.all("Category")

    for product in products:
        k = random.randint(1, 3)
        selected_categories = random.sample(categories, k)
        product.categories.extend(selected_categories)

    storage.save()


if __name__ == "__main__":
    storage.drop()
    storage.reload()
    create_users()
    create_products()
    create_orders()
    create_reviews()
    create_order_products()
    create_categories()
    create_product_categories()
    storage.close()
