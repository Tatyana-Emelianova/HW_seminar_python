n = int(input(" введите n --> "))

indexes = list(map(int,input('Введите значения n индексов через пробел ').split()))

if len(indexes) != n:
    print ("количество индексов не равно n")

if n > 0:
    numbers = [i for i in range(n*-1, n+1)]
else:
    numbers = [i for i in range(n, n*-1+1)]


import math
ind_of_numbers = [numbers[int(indexes[i])] for i in range (0, n)] 
# (ind_of_numbers) - последовательность элементов, которые нужно перемножить
prod_of_numbers = math.prod(ind_of_numbers)


print (numbers)
print (indexes)


for i in range(0,n-1):
    print (ind_of_numbers[i], "* ", end ="")

print (ind_of_numbers[n-1], "=", prod_of_numbers)