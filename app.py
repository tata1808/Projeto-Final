# app.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_required

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///rockstore.db"
db = SQLAlchemy(app)
login_manager = LoginManager(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship("User", backref="orders")
    products = db.relationship("Product", secondary="order_product")

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/products", methods=["GET"])
def get_products():
    products = Product.query.all()
    return jsonify([{"id": p.id, "name": p.name, "price": p.price} for p in products])

@app.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = Product.query.get(product_id)
    if product:
        return jsonify({"id": product.id, "name": product.name, "price": product.price})
    return jsonify({"error": "Product not found"}), 404

@app.route("/orders", methods=["POST"])
@login_required
def create_order():
    data = request.get_json()
    order = Order(user_id=current_user.id, products=data["products"])
    db.session.add(order)
    db.session.commit()
    # TO DO: implement payment gateway and order processing
    return jsonify({"id": order.id, "products": [p.name for p in order.products]}), 201

if __name__ == "__main__":
    app.run(debug=True)