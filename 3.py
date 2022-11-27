N = int(input(" для N --> "))
formula = {}
for i in range(1, N+1):
    formula [i]= round((1 + 1/N)**N ,3)

print (formula)