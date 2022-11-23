#initialisation
money = input("Money: ")
choice = input("Choice(A,B,C): ")

if money == "2":
    if choice == "A":
        print("Coffee dispensed")
    else:
        if choice == "B":
            output = "Tea"
        elif choice == "C":
            output = "Hot Chocolate"
        else:
            print("No selection")
            exit()
        milk = input("Want milk? ")
        if milk == "Yes":
            output += " and milk"
        print(output + " dispensed")
else:
    print("Invalid money")
end = input("Press G to grab your Drink ")
