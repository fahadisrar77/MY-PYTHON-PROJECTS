#VOTING ELIGIBILITY CHECKER

print("HELLO! YOU CAN CHECK FOR VOTE ELIGIBILITY HERE!")
print("=" * 50)

# user input
age = int(input("What is your age?\n: "))
citizen = input("Are you a citizen of Pakistan? YES or NO\n: ").strip().lower()
id_card = input("Do you have a valid ID card? YES or NO\n: ").strip().lower()
postal_code = int(input("Enter postal code of your city?\n: "))

print("=" * 50)

# conditions
if age >= 18 and citizen == "yes" and id_card == "yes":
    print("--> YOU ARE ELIGIBLE TO VOTE!\n")
else:
    if age < 18:
        print("--> SORRY: You must be at least 18 to vote!\n")
    elif citizen != "yes":
        print("--> SORRY: You must be a citizen of Pakistan to vote!\n")
    elif id_card != "yes":
        print("--> SORRY: You must have a valid ID card to vote!\n")

print("=" * 50)
print("THANKS FOR USING CHECKER!")
