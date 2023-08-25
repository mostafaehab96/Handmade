from faker import Faker
from models.user import User
from models.product import Product
from models.order import Order
from models.review import Review
from models import storage
import random
from models import db, app

fake = Faker()

with open("test_images.txt", "r") as file:
    images = file.readlines()


def create_users():
    for _ in range(30):
        user = User(
            name=fake.name(),
            email=fake.email(),
            address=fake.address(),
            postal_code="44511",
            about=fake.text(),
        )
        user.save()


def create_products():
    users = User.query.all()
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
    users = User.query.all()
    for _ in range(100):
        user = random.choice(users)
        order = Order(
            address=fake.address(),
            total_price=float(random.randint(10, 100)),
            user_id=user.id,
        )
        storage.new(order)

    db.session.commit()


def create_reviews():
    users = User.query.all()
    products = Product.query.all()

    for _ in range(50):
        user = random.choice(users)
        product = random.choice(products)
        review = Review(
            text=fake.text(),
            user_id=user.id,
            product_id=product.id
        )

        review.save()


def create_order_products():
    orders = Order.query.all()
    products = Product.query.all()
    for order in orders:
        # select random k
        k = random.randint(1, 3)
        # select random products
        purchased_products = random.sample(products, k)
        order.total_price = sum([product.price for product in purchased_products])
        order.products.extend(purchased_products)

    db.session.commit()


if __name__ == "__main__":
    with app.app_context():
        db.drop_all()
        db.create_all()
        create_users()
        create_products()
        create_orders()
        create_reviews()
        create_order_products()
        storage.close()
