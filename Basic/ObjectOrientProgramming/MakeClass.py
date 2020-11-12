class MyClass():
    value1 = 100
    value2 = 200

    def __init__(self, some_var=0):
        self.some_var = some_var

myClass = MyClass()

print(myClass.some_var)
print(MyClass.value2)