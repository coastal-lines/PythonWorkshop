import math
'''
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as ex:
        print(ex)
    except TypeError as ex:
        print(ex)
    except:
        print('Unknow error')
    finally:
        print('Method was closed')

divide(2, 0)
'''

class InvalidTr(Exception):
    """My error"""

def calc_square(ab, ac, bc):
    if ab <=0 or ac <= 0 or bc <= 0:
        raise InvalidTr('One of arguments less than 0')


    p = (ab + ac + bc) / 2
    s = math.sqrt(p * (p- ab) * (p - ac) * (p - bc))

    return s

square = calc_square(10, 10, 10)
print(square)