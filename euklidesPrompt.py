def nwd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)

a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))

print(f"NWD({a}, {b}) = {nwd(a, b)}")
