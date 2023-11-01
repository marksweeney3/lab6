
# Gayathri Gunda
# Mark Sweeney

def encode(password):
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


def decode(password):
    orginal_password = ""
    for digit in password:
        if digit.isdigit():
            original_password += str((int(digit) - 3) % 10)
    return original_password

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
            var = encode(password)
        elif selection == 2:
            decoded_password = decode(var)
            print(f'The encoded password is {var}, and the original password is {decoded_password}.')


if __name__ == "__main__":
    main()
