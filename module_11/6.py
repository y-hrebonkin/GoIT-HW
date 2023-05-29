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
        if value is None:
            return self.coordinates.x, self.coordinates.y
        else:
            return self.coordinates.x * value, self.coordinates.y * value

    def __str__(self):
        return f"Vector({self.coordinates.x},{self.coordinates.y})"

# У цьому коді метод __call__ в класі Vector перевіряє, чи переданий параметр value є None. 
# Якщо так, то повертається кортеж з координатами вектора. Якщо ж value має значення, 
# то повертається кортеж з новими координатами вектора, які отримані шляхом множення кожної координати на value.