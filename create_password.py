import random


def _main():
    passwd = _create_password(50, 49)
    print(passwd)


# This function is really hard to understand and probably unnecessarily
# complicated.
def _create_password(passwd_length=10, num_special_chars=2):
    special_chars = ["!", "@", "#", "%", "*"]
    if num_special_chars > passwd_length:
        # This is a place where you want to raise an exception. It's not a good
        # idea to print() for a number of reasons:
        #
        #   - The program may have no stdout/stderr attached at all
        #   - The output may get mixed with legitimate output (at least, always
        #     write errors to stderr)
        #   - The caller has no way of knowing that something bad happened,
        #     users will have empty password set
        #   - ...
        print("Number of special chars cant be greater than number of password length")
    all_chars = []
    for i in range(passwd_length):
        # So you don't use any alphabet chars, just numbers and special chars?
        all_chars.append(random.randint(0, 9))
    rand_chars = []
    for i in range(num_special_chars):
        rand_chars.append(random.choice(special_chars))
    positions = []
    while len(positions) < num_special_chars:
        pos = random.randint(0, len(all_chars)-1)
        if pos not in positions:
            positions.append(pos)
    for i in range(len(positions)):
        all_chars[positions[i]] = rand_chars[i]
    passwd = ""
    for i in range(len(all_chars)):
        passwd += str(all_chars[i])
    return passwd


if __name__ == "__main__":
    _main()
