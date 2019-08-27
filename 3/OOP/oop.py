class Point:
   
    def __init__(self, x=0, y=0):
       self.x = x
       self.y = y

    def coordinates(self):
        print(f'Мои координаты: {self.x};{self.y}')
    
    def __repr__(self):
        """Красивая печать обьекта"""
        return f'<Point: {self.x};{self.y}>'



my_point = Point(10,-234)
print(my_point)

