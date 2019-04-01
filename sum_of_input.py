import sys

num = len(sys.argv)

suma = 0
for i in range(1, num):
    suma += int(sys.argv[i])

print(suma)
