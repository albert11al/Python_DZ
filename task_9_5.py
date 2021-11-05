class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки! {self.title}))")

class Pen(Stationery):
    def draw(self):
        print(f"рисовать ручкой {self.title}")

class Pencil(Stationery):
    def draw(self):
        print(f"рисовать карандашом {self.title}")

class Marker(Stationery):
    def draw(self):
        print(f"рисовать маркером {self.title}")

stat = Stationery('начнем')
pen = Pen("Parker")
pencil = Pencil("Faber-Castell")
marker = Marker("COPIC")

office_supplies = [stat, pen, pencil, marker]

for i in office_supplies:
    i.draw()