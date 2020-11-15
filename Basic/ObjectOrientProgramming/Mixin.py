class Vehicle:
    def __init__(self, position):
        self.position = position

    def travel(self):
        pass

class Car(Vehicle):
    pass

class RadioMixin:
    def __init__(self):
        self.radio = Radio()

    def play_radio(self, station):
        self.radio.play(station)

class Radio:
    def play(self, station):
        print("I'm playing " + station)

#class with mixin
class Car(Vehicle, RadioMixin):
    def __init__(self):
        Vehicle.__init__(self, 0)
        RadioMixin.__init__(self)

ford = Car()
ford.play_radio('Jazz')