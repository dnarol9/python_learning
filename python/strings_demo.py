s = "I love Python"
print(s)
s = "Here os a line \ split in two lines"
print(s)
print("="*50)
s = "Here is a line \n split in two lines"
print(s)
print("="*50)
s = """ This is a
multiline string so you can
write many lines """
print(s)
print("="*50)
s= "Hello" "World"
print(s)
print("="*50)
print(len(s))
print("="*50)
s = "kushal das"
print(s.title())
print("="*50)
z = s.upper()
print(z)
print("="*50)
z.lower()
print(z)
print("="*50)
s = "I am A pRoGraMMer"
s.swapcase()
print(s)
print("="*50)
s = "jdwb 2323bjb"
print(s.isalnum())
s = "jdwb2323bjb"
print(s.isalnum())
s = "SankarshanSir"
print(s.isalpha())
s = "Sankarshan Sir"
print(s.isalpha())
print("="*50)
s = "1234"
print(s.isdigit())
s = "Fedora9 is coming"
print(s.islower())
s = "Fedora9 Is Coming"
print(s.istitle())
s = "INDIA"
print(s.isupper())
print("="*50)
s = "we all love pyhton"
print(s.split(" "))
x = "Nishant:is:waiting"
print(x.split(":"))
print("-".join("GNU/Linux is great".split(" ")))
print("="*50)
s = "  abc\n "
print(s.strip())
s = "www.foss.in"
print(s.lstrip("cwsd."))
print(s.rstrip("cnwdi."))
print("ACAB".rjust(10, "-"))
print("ACAB".ljust(10, "-"))
print("="*50)
s = "faulty for a reason"
print(s.find("for"))
print(s.find("abcd"))
print(s.startswith("fa"))
print(s.endswith("reason"))
print("="*50)
s= input("Please enter a string: ")
z = s [::-1]
if s ==z:
    print("the string is a oalindrome")
else:
    print(" the string is not a palindrome")
print("="*50)
s = input("Enter a line: ")
print("The number of words in the line are %d" % (len(s.split(" "))))
print("="*50)
for ch in "Python":
 print(ch)