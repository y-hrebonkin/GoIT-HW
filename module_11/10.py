class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if isinstance(x, (int, float)):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if isinstance(y, (int, float)):
            self.__y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"


class Vector:
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates

    def __setitem__(self, index, value):
        if index == 0:
            self.coordinates.x = value
        if index == 1:
            self.coordinates.y = value

    def __getitem__(self, index):
        if index == 0:
            return self.coordinates.x
        if index == 1:
            return self.coordinates.y

    def __call__(self, value=None):
        if value:
            self.coordinates.x = self.coordinates.x * value
            self.coordinates.y = self.coordinates.y * value
        return self.coordinates.x, self.coordinates.y

    def __add__(self, vector):
        new_x = self.coordinates.x + vector.coordinates.x
        new_y = self.coordinates.y + vector.coordinates.y
        return Vector(Point(new_x, new_y))

    def __sub__(self, vector):
        new_x = self.coordinates.x - vector.coordinates.x
        new_y = self.coordinates.y - vector.coordinates.y
        return Vector(Point(new_x, new_y))

    def __mul__(self, vector):
        scalar_product = self.coordinates.x * vector.coordinates.x + self.coordinates.y * vector.coordinates.y
        return scalar_product

    def len(self):
        length = (self.coordinates.x ** 2 + self.coordinates.y ** 2) ** 0.5
        return length

    def __str__(self):
        return f"Vector({self.coordinates.x}, {self.coordinates.y})"

    def __eq__(self, other):
        return self.len() == other.len()

    def __ne__(self, other):
        return self.len() != other.len()

    def __lt__(self, other):
        return self.len() < other.len()

    def __gt__(self, other):
        return self.len() > other.len()

    def __le__(self, other):
        return self.len() <= other.len()

    def __ge__(self, other):
        return self.len() >= other.len()

# У цьому коді методи порівняння (__eq__, __ne__, __lt__, __gt__, __le__, __ge__)
# були реалізовані для класу Vector, використовуючи метод len() для порівняння векторів за їх довжиною.