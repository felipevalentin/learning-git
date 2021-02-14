n = int(input())
if n < 1:
    print("Inválido")
elif n == 1:
    print("Não primo")
elif n == 2:
    print("Primo")
elif n == 3:
    print("Primo")
elif n % 2 == 0:
    print("Não primo")
else:
    for i in range(3, int(n**(1/2))+1, 2):
        if n % i == 0:
            print("Não primo")
            break
    else:
        print("Primo")
