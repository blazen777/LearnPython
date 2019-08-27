class Product:
    def __init__(self, name, price, stock=0, discount=0, max_discount=20):
        self.name = name.strip()
        if len(self.name) < 2:
            raise ValueError('Название товара должно состоять из двух иболее символов')
        self.price = abs(float(price))
        self.stock = abs(int(stock))
        self.dicount = abs(float(discount))
        self.max_discount = abs(float(max_discount))

        if self.max_discount > 99:
            raise ValueError('Слишком большая максимальная скидка')
        
        if self.dicount > self.max_discount:
            raise ValueError('Такого не может быть в природе')
            self.dicount = self.max_discount
    
    def discounted(self):
        return self.price - self.price * self.dicount / 100
    
    def sell(self, items_count=1):
        if items_count > self.stock:
            raise ValueError('Недостаточно товара на складе')
        # Взаимодействие с учетной/бух системой
        self.stock -= items_count
    
    def __repr__(self):
        return f'<Product name: {self.name}, price:{self.price}, stock:{self.stock}>'


tv_s210 = Product('BQ_S210', 12500, 55)
tv_s210.sell(5)
print(tv_s210)