def greeting():
    '''
    DOCSTRING: Information about this function
    INPUT: no input
    OUTPUT: hello
    '''
    print('hello')

greeting()
help(greeting)

def print_name(name):
    print(name)

print_name('Paul')

def default_name(name='Default'):
    print(name)

default_name()

def get_string(name, age):
    return 'hello' + name + str(age)

print('get_string:' + get_string('John', 45))
