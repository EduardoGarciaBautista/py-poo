class Car:
    def __init__(self, model, mark, color):
        self.model = model
        self.mark = mark
        self.color = color
        self._state = 'inactive'
        self._engine = Engine(cylinders=4)

    def speed_up(self, speed_up_type='slow'):
        if speed_up_type == 'slow':
            self._engine.inject_gas(10)
        else:
            self._engine.inject_gas(3)
        self._state = 'moving'


class Engine:
    def __init__(self, cylinders, type_car='gas'):
        self.type_car = type
        self.cylinders = cylinders
        self._temperature = 0

    def inject_gas(self, count):
        pass
