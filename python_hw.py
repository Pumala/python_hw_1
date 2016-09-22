# Hello, you!
name = raw_input("What is your name? ")

print "Hello, %s!" % name

# HELLO, YOU!
name = raw_input("WHAT IS YOUR NAME? ")

print "HELLO, %s!" % name.upper()
print "YOUR NAME HAS %d LETTERS IN IT! AWESOME!" % len(name)

# Madlib
print "Please fill in the blanks below:"

name = raw_input("What is name? ")
adjective = raw_input("What is adjective? ")

print "%s has a %s laugh." % (name, adjective)

# Day of the Week
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
"Saturday"]

day = int(raw_input("Day (0-6)? "))
print days[day]
# print find_day(day)

# Work or Sleep in?
def work_or_sleep(day):
    if day == 1 or day == 2 or day == 3 or day == 4 or day == 5:
        return "Go to work"
    elif day == 6 or day == 0:
        return "Sleep in"
    # else:
        # return "That wasn't an option."

print work_or_sleep(int(raw_input("Day (0-6)? ")))

# Celsius to Fahrenheit
def convert_c_to_f(degree):
    return degree * 1.8 + 32

degree = float(raw_input("Temperature in C? "))

print str(convert_c_to_f(degree)) + " F"

# Tip Calculator
def get_tip(bill, rating):
    if rating == "good":
        percent = bill * .20
        amount = bill + percent
        return (percent, amount)
    elif rating == "fair":
        percent = bill * .15
        amount = bill + percent
        return (percent, amount)
    elif rating == "bad":
        percent = bill * .10
        amount = bill + percent
        return (percent, amount)
    else:
        return "That's not an option."

bill = float(raw_input("Total bill amount? "))
rating = raw_input("Level of service? ")

tip_amt = get_tip(bill, rating)[0]
total_bill = get_tip(bill, rating)[1]

print "Tip amount: $%.2f" % tip_amt
print "Total amount: $%.2f" % total_bill

# Tip Calculator 2
def tip_machine(bill, rating):
    if rating == "good":
        percent = bill * .20
        amount = bill + percent
        return (percent, amount)
    elif rating == "fair":
        percent = bill * .15
        amount = bill + percent
        return (percent, amount)
    elif rating == "bad":
        percent = bill * .10
        amount = bill + percent
        return (percent, amount)
    else:
        return "That's not an option."

bill = float(raw_input("Total bill amount? "))
rating = raw_input("Level of service? ")
split = float(raw_input("Split how many ways? "))

tip_total = tip_machine(bill, rating)[0]
bill_total = tip_machine(bill, rating)[1]

print "Tip amount: $%.2f" % tip_total
print "Total amount: $%.2f" % bill_total
print "Amount per person: $%1.2f" % (bill_total / split)
