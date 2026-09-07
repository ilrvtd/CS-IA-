class Product:
    def __init__(self,product_ID,name, selling_price, cost):
        self.product_ID = product_ID
        self.name = name
        self.selling_price = selling_price
        self.cost = cost
    def get_profit_per_unit(self):
        self.profit_per_unit = self.selling_price - self.cost
        return self.profit_per_unit
    def get_profit_margin(self):
        self.profit_margin = ((self.selling_price - self.cost)/self.selling_price) * 100
        return self.profit_margin
