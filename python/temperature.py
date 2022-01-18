fahrenheit = 0.0
while fahrenheit <= 250:
	celsius = (fahrenheit -32.0) / 1.8 # Here we calculate the Celsius value
	print("fahrenheit %5.1f celcius %7.2f" % (fahrenheit, celsius))
	fahrenheit = fahrenheit + 25
