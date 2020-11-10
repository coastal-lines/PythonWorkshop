def get_candy():
    candy = 5
    def increment_candy(): 
        nonlocal candy
        candy += 1
        return candy
    return increment_candy
    
result = get_candy()()
print('Всего {} конфет.'.format(result))