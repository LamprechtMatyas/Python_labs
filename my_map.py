def _main():
    print(_my_map([5, 2, 7], _times_five))
    print(_my_map(["one", "two", "three"], _reverse_string))


def _my_map(arguments, fnc):
    new_list = []
    for item in arguments:
        new_list.append(fnc(item))
    return new_list


def _times_five(a):
    return a * 5


def _reverse_string(string):
    return string[::-1]


if __name__ == "__main__":
    _main()
