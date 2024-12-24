first, second, third = int(input()), int(input()), int(input())
if first == second == third:
    print(3)
elif first != second != third:
    print(0)
else first == second or second == third or first == third:
    print(2)