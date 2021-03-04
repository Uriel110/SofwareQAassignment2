def main():
    cont = input("Would you like to start? Enter y or n: ")
    if cont != 'y' and cont != 'n':
            cont = input('Invalid input, please enter y or n: ')
    while cont == "y":
        menu()
        cont = input("Would you like to continue? Enter y or n: ")
        if cont != 'y' and cont != 'n':
            cont = input('Invalid input, please enter y or n: ')
    if cont == 'n':
        print("Goodbye!")
        return   
    

def menu():
    print("Welcome to the menu!")
    print("1. Body Mass Index Calculator")
    print("2. Retirement Goal Calculator")
    selection = input("Enter your selction: ")

    if selection == '1':
        print("Normally this would start calcualtor for bmi")

    elif selection == '2':
        print ("normally this would start calculator for retirement")


main()