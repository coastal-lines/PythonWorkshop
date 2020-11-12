class Character():
    MAX_SPEED = 100 #constant

    def __init__(self, race, damage=10):
        self.damage = damage
        self.__race = race #private attribute
        self._health = 100
        self._current_speed = 20

    @property
    def health(self):
        return self._health

    @property
    def cur_speed8(self):
        return self._current_speed

    @cur_speed.setter
    def cur_speed(self, current_speed):
        if current_speed < 0:
            self._current_speed = 0
        elif current_speed > 100:
            self._current_speed = 100
        else:
            self._current_speed = current_speed   