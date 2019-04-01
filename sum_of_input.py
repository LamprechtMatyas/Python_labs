import sys


def _main():
    num = len(sys.argv)
    print(_sum_input(num))


def _sum_input(num: int):
    suma = 0
    for i in range(1, num):
        suma += int(sys.argv[i])
    return suma


if __name__ == "__main__":
    _main()
