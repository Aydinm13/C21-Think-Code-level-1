print("Hi")
name = input ("What is your name?")

print("It's nice to meet you,",name)

som = input ("Do you want to play a game?")

if som == "yes":
    num1 = input ("Please insert the fisrt number: ")
    num2 = input ("Please insert the second number: ")
    num1= int(num1)
    num2= int(num2)
    operation = input ("Please insert your desired operation among: + - * / :")
    if operation == "+":
        result = num1 + num2
    if operation == "-":
        result = num1 - num2
    if operation == "*":
        result = num1 * num2
    if operation == "/":
        result = num1 / num2
    print(result)  
else:
    print("Okay, have a nice day")

