n = int(input())
if n <= 1:
    print("Not Prime")
else:
    if any(n % i == 0 for i in range(2, n)):
        print("Not Prime")
    else:
        print("Prime")
