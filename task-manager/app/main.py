num = int(input(" Enter the number to get febonacci series : "))

a = 0
b = 1

count = 0 
while count < num:
    print(a, end = " ")
    c = a + b
    a = b
    b = c
    count += 1
