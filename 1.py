num = str(float(input("Введите вещественное число: ")))
x = num.split(".") 
a = abs(int(x[0]))
b = int(x[1]) 
sum = 0
while (a != 0): 
    sum = sum + (a % 10)
    a = a // 10
while (b != 0): 
    sum = sum + (b % 10)
    b = b // 10
print("Сумма цифр равна:", sum)
