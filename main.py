import time
print("Welcome to the birthday month guesser!")

name = input("What is your first name?\n ").lower()
print("Hello, " + name + "!!!")
time.sleep(2)
input("What is your favorite color?\n ")
input("What is your favorite animal?\n ")
input("What is your favorite season?\n ")
input("What year were you born?\n ")
input("Was there snow on the ground when you were born?\n ")
time.sleep(2)
print("Thinking...")
time.sleep(3)
print("I will now guess your birthday month!")
print("Thinking...")
time.sleep(3)
print("Thinking harder...")
time.sleep(3)
print("Your birthday month is...")
time.sleep(5)
if name =="aayla":
  print("November!!!")
elif name =="erica":
  print("May!!!")
elif name =="flynn":
  print("May!!!")
