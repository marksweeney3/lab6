

def encoder(password):
    result = ''
    for i in range(len(password)):
        if password[i] == "7":
            result += "0"
        elif password[i] == "8":
            result += "1"
        elif password[i] == "9":
            result += "2"
        else:
            new_num = int(password[i]) + 3
            result += str(new_num)
    return result

def decoder(var):
    encoded_password = var
    result = ''
    for i in range(len(encoded_password)):
        if encoded_password[i] == "0":
            result += "7"
        elif encoded_password[i] == "1":
            result += "8"
        elif encoded_password[i] == "2":
            result += "9"
        else:
            new_num = int(encoded_password[i]) - 3
            result += str(new_num)
    return result


def main():
    var = ''
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")
        selection = int(input("Please enter an option: "))
        if selection == 3:
            exit()
        elif selection == 1:
            password = input("Please enter your password to code: ")
            print("Your password has been encoded and stored!\n")
            var = encoder(password)
        elif selection == 2:
            print(f"The encoded the password is {var}, and the original password is {decoder(var)}.\n")


if __name__ == "__main__":
    main()