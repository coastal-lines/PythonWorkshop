class Character:
    _instanse = None
    def __new__(cls):
        if not cls._instanse:
            cls._instanse = super().__new__(cls)
        return cls._instanse
    
    def __init__(self):
        self.race = 'Elf'