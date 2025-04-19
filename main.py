import random

def random_number():

    random_number =[random.randint(1, 100) for _ in range(10)]

    print("Random numbers:", *random_number)
    random_number.sort()
if __name__ == "__main__":
    random_number()
