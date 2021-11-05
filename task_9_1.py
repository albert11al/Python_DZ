import time
class TrafficLight:
    # Конструктор
    # Атрибут объекта
    def __int__(self, yellow):
        self.__color = yellow
    # Методы
    def running(self):
        def out_red(text):
            print("\033[31m {}".format(text))
        def out_yellow(text):
            print("\033[33m {}".format(text))
        def out_green(text):
            print("\033[32m {}".format(text))
        out_red("RED")
        time.sleep(7)
        out_yellow("YELLOW")
        time.sleep(2)
        out_green("GREEN")
        time.sleep(10)
# Объекты
lights = TrafficLight()
lights.running()




