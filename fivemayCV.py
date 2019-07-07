#5-may-2019
'''print("Enter your details to make your CV.")
name = input("Enter your name:")
email = input("Enter your email:")
address = input("Enter your address:")
phoneno = input("Enter your phone number:")
qualification = input("Enter your qualification:")
skill = input("Enter your skill:")
print("\nName =",name + "\nEmail =",email+"\nAddress =" ,address+"\nPhone Number =",
      phoneno + "\nQualification =" ,qualification+"\nSkill= " ,skill)'''
#if-else
'''event_venue=input("Where is event?")
if event_venue == "Home":
    print("I am busy can not go!")
    print("Hamdah!")
else:
    print("I will go!")'''
#elif
'''event_venue=input("Where is event?")
if event_venue == "Home":
    print("I am busy can not go!")
    print("Hamdah!")
elif event_venue == "School":
    print("Ok Ok")
elif event_venue == "Garden":
    print("wow lets go")
else:
    print("I will go!")
print("After Else")'''
#comparision operators
'''> , < , == , != , >= , <='''
#even-odd program
#in pyton string can not perform % operation with number and number cant be concatinated with string
'''number = int(input("Enter a number to check whether it is even or odd:"))
if number % 2 == 0:
    print(str(number) + " is an even number")
else:
    print(str(number) + " is an odd number")'''
#calculator
number1 = int(input("Enter first number :"))
number2 = int(input("Enter second number :"))
operator = input("Enter operator :")
if operator == "+":
    answer = number1 + number2
    print(answer)
elif operator == "-":
    answer = number1 - number2
    print(answer)
elif operator == "*":
    answer = number1 * number2
    print(answer)
elif operator == "/":
    answer = number1 / number2
    print(answer)
elif operator == "%":
    answer = number1 % number2
    print(answer)
else:
    print("You have entered wrong operator.")
