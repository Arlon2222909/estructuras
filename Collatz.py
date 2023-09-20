n = int(input("Introduzca su ultimo digito de su codigo:"))
m= n+3
l = 0

for i in range (1,n+1):
    i = int(input("ingrese el primer numero:"))
    l= l+i
x = l/n
while n != 1:
    if n % 2 == 0:
        n //= 2
        print(n)
    else:
        n = n*3 + 1
        print,
