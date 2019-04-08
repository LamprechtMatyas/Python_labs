import sys


def _main():
    num = len(sys.argv)
    print(_sum_input(num))


# I think you misunderstood the assignment: this should have been just:
#
#    def sum_given_args(*args):
#        return sum(args)
#
# and used as
#
#    sum_given_args(1, 2, .33, 5)
#
# This has nothing to do with sys.argv :). Those are called command-line
# arguments and have nothing to do with function arguments in Python.
def _sum_input(num: int):
    suma = 0
    for i in range(1, num):
        suma += int(sys.argv[i])
    return suma


if __name__ == "__main__":
    _main()
