import itertools

password = input("Enter the password to crack: ")
charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-={}|\\:;\"<>,.?/"

for length in range(1, 9):
    for attempt in itertools.product(charset, repeat=length):
        guess = "".join(attempt)
        if guess == password:
            print("Password found: %s" % guess)
            break

