pl = [('Adam', 12, 24), ('John', 100, 9), ('Nina', 8, 95)]
#print(pl[0].name) #error

from collections import namedtuple
Player = namedtuple('Player', 'name age rating') #похоже на создание класса
pl = [Player('Adam', 12, 24), Player('John', 100, 9), Player('Nina', 8, 95)]
print(pl[0])
print(pl[0].name)