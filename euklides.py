def nwd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)

print(nwd(48, 18))  # NWD to 6
