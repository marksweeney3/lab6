

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

if __name__ == "__main__":
    main()
