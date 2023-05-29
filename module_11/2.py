class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

# Приклад використання
point = Point(5, 10)
print(point.x)  # 5
print(point.y)  # 10

point.x = 8
point.y = 15
print(point.x)  # 8
print(point.y)  # 15
