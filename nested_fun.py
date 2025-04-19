def main_1(message: str,repeat:int):
    for i in range(repeat): 
        print(message)


def main_2():
    message = input("Enter a message: ")
    repeat = int(input("Enter the number of times to repeat the message: "))
    main_1(message, repeat)
    return message, repeat

if __name__ == "__main__":
    main_2()
# This code takes a message and a number as input and prints the message that number of times.











    