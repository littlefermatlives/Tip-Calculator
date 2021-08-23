print("Welcome to the tip calculator")
a = float(input("What is your totoal bill? $"))
b = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
c = int(input("How many people to split the bill? "))

total = float(a*b)
total /= 100
total += a
total /= c
total = round(total,2)
print(f"Each person should pay: {total}")
print("Thank You")