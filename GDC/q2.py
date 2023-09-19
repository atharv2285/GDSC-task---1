n = int(input("Enter the number of rows: "))

t = 1

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(t, end=" ")
        t += 1
        if t > 5:
            t = 1
    print()
