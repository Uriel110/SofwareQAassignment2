def main():
    while True:
        menu()
        cont = input("Would you like to continue? Enter y or n: ")
        if cont != 'y' and cont != 'n':
            cont = input('Invalid input, please enter y or n: ')
        if cont == 'n':
            print("Goodbye!")
            break  
    

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
        retirement()

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

def retirement():
    print("Please enter your age, salary, percentage salary saved, and savings goal.")
    while True:
        try:
            age = int(input("Please enter your age: "))
            break
        except:
            print("Please enter a whole number.")
    while True:
        try:
            salary = float(input("Please enter your salary: "))
            break
        except:
            print("Please enter a whole number or a decimal.")
    while True:
        try:
            percent = float(input("Please enter your percentage salary saved: "))
            break
        except:
            print("Please enter a whole number or decimal.")
    while True:
        try:
            goal = float(input("Please enter your savings goal: "))
            break
        except:
            print("Please enter a whole number or a decimal.")
    spy = (salary * percent)*1.35
    yearstilgoal = goal//spy
    yearsremain = goal%spy
    if yearsremain == 0:
        agegoal = age + yearstilgoal
    elif yearsremain > 0:
        agegoal = age + yearstilgoal + 1
    if agegoal >= 100:
        print("You will be ",int(agegoal)," so you will not meet your goal.")
    elif agegoal < 100:
        print("You will be ",int(agegoal)," so you will meet your goal.")

main()