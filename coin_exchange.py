cents = int(input("Enter the number of cents: "))

quarters = cents // 25
dimes = (cents % 25) // 10
nickles = ((cents % 25) % 10) // 5
pennies = ((cents % 25) % 10) % 5


print(str(quarters) + " quarter, " + str(dimes) + " dime, " + str(nickles) + " nickel, " + str(pennies) + " penny")
