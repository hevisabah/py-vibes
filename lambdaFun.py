my_list = [1, 2]
my_list.append(3)
print(my_list)

print(my_list[0])

my_list[0] = 0
print(my_list)

add_n = lambda lst, n: [x + n for x in lst]

new_list = add_n(my_list, 5)
print(new_list)
