#### property ####
class Circle:
    def __init__(self, radius, x, y) -> None:
        self.__radius = radius
        self._x = x  # Changed from self.x to self._x
        self._y = y  # Changed from self.y to self._y
        
    @property
    def x(self):
        print("get x value")
        return self._x 
    
    @x.setter
    def x(self, value):
        try:
            self._x = float(value)
            print("Validated!")
        except ValueError:
            raise ValueError('"x" must be a number') from None

    @x.deleter
    def x(self):
        del self._x
    
    @property
    def radius(self):
        print("Get Radius")
        return self.__radius

    @radius.setter
    def radius(self, value):
        print('Set radius')
        self.__radius = value

    @radius.deleter
    def radius(self):
        print('Delete radius')
        del self.__radius

### magic methods ####



class Point():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __lt__(self, other) -> bool:
        return self.x < other.x and self.y < other.y
    def __gt__(self, other) -> bool:
       return self.x > other.x and self.y > other.y
    def __ge__(self, other) -> bool:
        return self.x >= other.x and self.y >= other.y
    def __ne__(self, other) -> bool:
        return self.x != other.x or self.y != other.y
    def __eq__(self, other) -> bool:
        return self.x == other.x or self.y == other.y

    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"
    
    def __str__(self) -> str:
        return f"{self.x}, {self.y}"
