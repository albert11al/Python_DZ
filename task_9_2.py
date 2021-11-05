class Road:
    def __init__(self, a, b):
        self._length = a
        self._width = b
    def asphalt_mass(self, weight, thickness):
        print(f'ширина дорожного полотна {self._width}, длина {self._length}, '
              f'масса {weight}, толшина {thickness} '
              f'= {(self._width * self._length * weight * thickness) / 1000}')

asphalt = Road(5000, 20)
asphalt.asphalt_mass(25, 5)
