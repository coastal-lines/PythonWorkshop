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