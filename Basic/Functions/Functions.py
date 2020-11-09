print(abs(-1)) #взятие числа по модулю
print(max(1,2,3,4,5)) #max value
print(min(-5,5))
print(pow(2, 3)) #возведение в степень
print(round(3.344, 1)) #округрлние, где второй аргумент это число знаков ПОСЛЕ запятой
print(sum([2, 5]))
print(hex(42)) #16
print(oct(42)) #8
print(bin(42)) #2

l1_true = all([True, True, True])
l2_true = all([False, True, True])
print(l1_true)
print(l2_true)

#all
print('==========')
pl = [('Anna', 101), ('Marta', 132), ('Igor', 104)]
result = all(score > 100 for _, score in pl)
print(result)

#any если хотя бы один true то будет тру. фалс если вообще все фолс
print('==========')
l1_true = any([True, True, True])
l2_true = any([False, True, True])
print(l1_true)
print(l2_true)

