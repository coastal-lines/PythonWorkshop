from functools import wraps

def log_decorator(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        print(f'Calling func {func}')
        func(*args, **kwargs)
        print(f'Func {func} finished its work')
    return wrap

#def hello():
#    print('Hello world')

#wrapped_by_logger = log_decorator(hello)
#wrapped_by_logger()

@log_decorator
def hello():
    print('Hello world')

hello()