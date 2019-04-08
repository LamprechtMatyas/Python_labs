def _main():
    print(list(_my_range(10)))
    print(list(_my_range(2, 28)))
    print(list(_my_range(3, 50, 6)))


# 0 is not a good value to tell if `start` was present or not:
# list(_my_range(10, 0, -1))
# []
# >>> list(range(10, 0, -1))
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
def _my_range(limit, start=0, step=1):
    if start != 0:
        change = start
        start = limit
        limit = change
    n = start
    while (step < 0 or n < limit) and (step > 0 or n > limit):
        yield n
        n += step


if __name__ == "__main__":
    _main()
