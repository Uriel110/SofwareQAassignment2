def main():
    cont = input("Would you like to start? Enter y or n: ")
    while cont != 'y' and cont != 'n':
        cont = input('Invalid input, please enter y or n: ')
    while cont == "y":
        menu()
        cont = input("Would you like to continue? Enter y or n: ")
        while cont != 'y' and cont != 'n':
            cont = input('Invalid input, please enter y or n: ')
    if cont == 'n':
        print("Goodbye!")
        return   
    

def menu():
    print("Welcome to the menu!")
    print("1. Body Mass Index Calculator")
    print("2. Retirement Goal Calculator")
    selection = input("Enter your selction: ")
    while selection != '1' and selection != '2':
        selection = input('Invalid Selection. Try again: ')

    if selection == '1':
        BMI()

    elif selection == '2':
        print ("normally this would start calculator for retirement")


def BMI():
    while True:
        try:
            weight = float(input("Please enter your weight in lbs: "))
            break
        except:
            print("Please enter a whole number or decimal.")
    print("Please enter feet then inches.")
    while True:
        try:
            feet = float(input("Feet: "))
            break
        except:
            print("Please enter a whole number.")
    while True:
        try:
            inches = float(input("Inches: "))
            break
        except:
            print("Pleae enter a whole number.")
    height = (feet*12)+inches
    metric_weight = weight * 0.45
    metric_height = height * 0.025
    height_squared = metric_height**2
    BMI = metric_weight / height_squared
    if BMI <= 18.5:
        print("Your BMI is ",BMI,"and you are classified as Underweight.")
    elif BMI >18.5 and BMI <= 24.9:
        print("Your BMI is ",BMI,"and you are classified as Normal Weight.")
    elif BMI > 24.9 and BMI <=29.9:
        print("Your BMI is ",BMI,"and you are classified as Overweight.")
    elif BMI >29.9:
        print("Your BMI is ",BMI,"and you are classified as Obese.")


main()