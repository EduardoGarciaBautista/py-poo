class WashingMachine:

    def __init__(self):
        pass

    def wash(self, temperature='hot'):
        self._fill_tank(temperature)
        self._add_soap()
        self._wash()
        self._centrifuge()

    def _fill_tank(self, temperature):
        print(f'Filling tank with watter at {temperature}°')

    def _add_soap(self):
        print('Adding soap')

    def _wash(self):
        print('Washing')

    def _centrifuge(self):
        print('Centrifuge')


if __name__ == '__main__':
    washer = WashingMachine()
    washer.wash()