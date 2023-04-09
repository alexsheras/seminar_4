n = int(input("Введите кол-во элементов первого набора чисел: "))
m = int(input("Введите кол-во элементов второго набора чисел: "))

list_1 = list()
for i in range(n):
    input_n = int(input("Введите элементы первого набора: "))
    list_1.append(input_n)

list_2 = list()
for i in range(m):
    input_m = int(input("Введите элементы второго набора: "))
    list_2.append(input_m)
    
print(list_1)
print(list_2)

numbers = set(list_1)
numbers2 = set(list_2)
numbers3 = numbers.intersection(numbers2)
sorted_numbers = sorted(numbers3)
print(sorted_numbers)