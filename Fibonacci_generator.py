def _main():
    generator = _fibo_gen(10)
    print(next(generator))
    print(next(generator))
    generator2 = _fib()
    for i in range(20):
        print(next(generator2))


def _fibo_gen(n):
    new = 1
    old = 0
    for i in range(n):
        suma = new + old
        old = new
        new = suma
        yield suma


def _fib():
    new = 1
    old = 0
    while True:
        suma = new + old
        old = new
        new = suma
        yield suma


if __name__ == "__main__":
    _main()