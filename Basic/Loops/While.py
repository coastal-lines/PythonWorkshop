x = 0
while x < 10:
    print(x)
    x+=1


print('===========')
x = 0
while x < 10:
    #print(x)
    x+=1
else:
    print('This is end')


print('===========')
for i in range(0, 11):
    print(i)
    if(i > 6):
        break


print('===========')
for i in range(0, 11):
    if i % 2 == 0:
        continue
    else:
        print(i)

print('===========')
