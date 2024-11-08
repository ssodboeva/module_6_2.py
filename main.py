class Vehicle:
    __COLOR_VARIANTS = ['красный', 'черный', 'белый', 'голубой']

    def __init__ (self, owner, __model, __engine_power,__color):
        self.owner = owner
        self.__model =__model
        self.__engine_power = __engine_power
        self.__color = __color

    def get_model (self):
        return f"Модель: {self.__model}"

    def get_horsepower (self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color (self):
        return f"Цвет: {self.__color}"

    def print_info (self):
        print (self.get_model())
        print (self.get_horsepower())
        print (self.get_color())
        print (f'Владелец: {self.owner}')

    def set_color (self, new_color):
        if new_color.lower () in self.__COLOR_VARIANTS:
           self.__color = new_color.capitalize()
        else:
            print (f"Нельзя сменить цвет на {new_color}")


class Sedan (Vehicle):
    __PASSENGERS_LIMIT = 5

vehicle1 = Sedan('Иван', 'Toyota Mark II', 'черный', 500)
vehicle1.print_info()
vehicle1.set_color('розовый')
vehicle1.set_color('КРАСНЫЙ')
vehicle1.owner = 'Катя'
vehicle1.print_info()
