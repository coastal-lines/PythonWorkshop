class Character():

    def __init__(self, race, damage = 100):
        self.race = race
        self.damage = damage

    def __repr__(self):
        return f"Character('{self.race}', {self.damage})"

    def __eq__(self, other):
        if isinstance(other, Character):
            return self.race == other.race and self.damage == other.damage
        return False

c = Character('elf')
print(c)

