from . import db


class Options(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    productId = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer)
    amount = db.Column(db.Integer)

    def __init__(self, ProductId, Price, Weight, Amount):
        self.ProductId = ProductId
        self.Price = Price
        self.Weight = Weight
        self.Amount = Amount

    def __repr__(self):
        return '<Option %d: ProductID: %d, Price: %d, Weight: %d, Amount: %d>' % (self.OptionId, self.ProductId, self.Price, self.Weight, self.Amount)