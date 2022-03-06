from hasToPay import hasToPay


if __name__ == '__main__':
    path = input("\nPlease enter path to txt file\n")
    try:
        with open(path, 'r') as file:
            for line in file:
                name, amount = hasToPay(line)
                print("The amount to pay {} is: {} USD".format(name, amount))
    except FileNotFoundError:
        print('\nIncorrect file name')