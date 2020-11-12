class Date:
    def __init__(self, month, day, year):
        self.month = month
        self.day = day
        self.year = year
        
    def display(self):
        return f"{self.month}-{self.day}-{self.year}"
    
    @classmethod
    def millenium_c(cls, month, day):
        return cls(month, day, 2000)
    
    @staticmethod
    def millenium_s(month, day):
        return Date(month, day, 2000)

class DateTime(Date):
    def display(self):
         return f"{self.month}-{self.day}-{self.year} - 00:00:00PM"

dt1 = DateTime(10, 10, 1990)
dt2 = DateTime.millenium_c(10, 10)#через cls передается, что мы конструируем именно DateTime класс
dt3 = DateTime.millenium_s(10, 10)

print(dt1.display())
print(dt2.display())
print(dt3.display())