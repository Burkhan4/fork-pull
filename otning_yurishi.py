x1 = int(input("Birinchi otning x koordinatasini kiriting (1-8): "))
y1 = int(input("Birinchi otning y koordinatasini kiriting (1-8): "))
x2 = int(input("Ikkinchi otning x koordinatasini kiriting (1-8): "))
y2 = int(input("Ikkinchi otning y koordinatasini kiriting (1-8): "))

dx = abs(x2 - x1)
dy = abs(y2 - y1)
if dx == 2 and dy == 1 or dx == 1 and dy == 2:
    print("True")
else:
    print("False")