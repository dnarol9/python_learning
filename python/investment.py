amount = float(input("Enter amount: "))
inrate = float (input("Enter interest rate: "))
period = int(input("Enter period: "))
value = 0
year = 1
while  year <= period:
		value = amount + (inrate * amount)
		print("year %d Rs. %.2f".format(year, value))
		print(year, value)
		amount = value
		year = year + 1
