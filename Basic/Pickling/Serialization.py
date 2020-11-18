import pickle

class Character():

    def __init__(self, count, count2):
        self.count = count
        self.count2 = count2

    def print_count(self):
        print(self.count)
        print(self.count2)

    def __setstate__(self, state):
        self.count = state.get('count', '999')
        self.count2 = state.get('count2', '999')

#c = Character(123)
#c.print_count()

#with open(r'C:\Repos\MyGit\PythonWorkshop\Basic\Pickling\serialization_file.data', 'w+b') as f:
 #   pickle.dump(c, f)

with open(r'C:\Repos\MyGit\PythonWorkshop\Basic\Pickling\serialization_file.data', 'rb') as f:
    c2 = pickle.load(f)

c2.print_count()