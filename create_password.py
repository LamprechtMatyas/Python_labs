import random


def _main():
    passwd = _create_password(50, 49)
    print(passwd)


def _create_password(passwd_length=10, num_special_chars=2):
    special_chars = ["!", "@", "#", "%", "*"]
    if num_special_chars > passwd_length:
        print("Number of special chars cant be greater than number of password length")
    all_chars = []
    for i in range(passwd_length):
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
