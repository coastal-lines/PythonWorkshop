#list

int_list = [1,2,3]
mixed_list=["1", 2, 3.0]

print(len(int_list))
print(mixed_list[1])
print(int_list[1:])

names1 = ["John", "Sandra"]
names2 = ["Boris", "Anna"]
names = names1 + names2
print(names)

names1[0] = "Paul"
print(names1)

names.append("Miranda")
print(names)

popped = names.pop()
print(popped)
names.pop(0)
print(names)

list_sort = ["a", "d", "z", "1", "10"]
print(list_sort)
list_sort.sort()
print(list_sort)

len_sort_list = ["1", "1000", "100"]
print(len_sort_list)
len_sort_list.sort(key=len)
print(len_sort_list)

reverse_list = [9,8,7,6,5]
print(reverse_list)
reverse_list.reverse()
print(reverse_list)

reverse_list.sort(reverse=True)
print(reverse_list)


reverse_list = [9,8,7,6,5]
reverse_list.insert(0, 999)
print(reverse_list)
print(reverse_list.index(999))
print(reverse_list.count(999)) #search number count

copy_list = reverse_list.copy()
