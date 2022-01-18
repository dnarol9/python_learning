status = int(input("Give us a status code: "))
if status == 200:
	print("OK")
elif status == 201:
	print("Created")
elif status == 301:
	print("Moved Permanently")
elif status == 302:
	print("Found")
else:
	print("This status is unknown to us")
