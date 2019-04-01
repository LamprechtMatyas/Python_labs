import sys


def _main():
    input_string = sys.argv[1]
    isPalindrome = True

    for i in range((len(input_string) + 1)//2):
        if input_string[i] != input_string[len(input_string) - 1 - i]:
            isPalindrome = False
            break

    if isPalindrome:
        print("This is palindrome")
    else:
        print("This is not palindrome")


if __name__ == "__main__":
    _main()

