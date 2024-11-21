# is_hot = False
# is_cold = False
# if is_hot:
#     print("Stay Home, Weather is hot")
#     print("Stay Hyderated")
# elif is_cold:
#     print("Weather is Cold")
#     print("Use Warm Clothes")
# else:
#     print("Normal Temprature, Have a nice day")

# print("Enjoy Your day")


#/////////////////////////////////////////////////////////////////////


# House_price = 5000000

# buyer_credit_good = True

# if buyer_credit_good:
#     down_payment = 0.1 * House_price
#     print(f"""House price is ${House_price},
# the buyer having good credit.
# So they need to put down 10%.
# Down payment = {down_payment}"""
# )
# else:
#     down_payment = 0.2 * House_price
#     print(f"""House price is ${House_price}
# buyer not having good credit.
# they need to put down 20%.
# Down payment = {down_payment}""")    


#/////////////////////////////////////////////////////////////////////


# has_high_income = True
# has_good_credit = False

# if has_high_income and has_good_credit:
#     print("Eligible for Loan")
# else:
#     print("You arent eligible for Loan")


# /////////////////////////////////


# has_good_credit = True
# has_criminal_record = True

# if has_good_credit and not has_criminal_record:
#     print("Elible for loan")

# else:
#     print("Applicant in not elible for load")


# /////////////////////////////////

# temperature = 15

# if temperature > 20:
#     print("It's hot day")
# elif temperature < 10:
#     print("It's Cold day")
# else:
#     print("it's a normal day")


#//////////////////////////////////


# name = "sumair"

# if len(name) < 3:
#     print("name must be atleast 3 characters")
# elif len(name) > 50:
#     print("name cannot be more than 50 words")
# else:
#     print("Name Looks Good")

#///////////////////////////////////

# weight = int(input('Weights:'))
# unit = input('(L)lbs or (K)g: ')

# if unit.upper() =="L":
#     converted = weight * 0.45
#     print(f"You are {converted} kilos")

# else:
#     converted = weight / 0.45
#     print(f"You are {converted} pounds")

#///////////////////////////////////

# i = 1
# while i <= 5:
#     print('*' * i)
#     i = i + 1
# print("Done")

#///////////////////////////////////////

# secret_number = 9
# guess_count= 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input('Guess: '))
#     guess_count += 1
#     if guess == secret_number:
#         print('You Won')
#         break
# else:
#     print('You failed')
    

#///////////////////////////////////////

# command = ""
# started = True
# stopped = True

# while command != "quit":
#     command = input("> ").lower()
#     if command == "start":
#         if started:
#             print("Car is already started")
#         else:
#             started = True
#             print("Car started...")
#     elif command == "stop":
#         if stopped:
#             print("Car is already stopp")
#         else:
#             stopped = True
#             print("Car stopped.")
#     elif command == "quit":
#         print("")
#         break
#     elif command == "help":
#         print("""
# start - to start the car
# stop - to stop the car
# quit - to quit
# """)
#     elif command == "quit":
#         break

#     else:
#         print("Type the correct command")


#///////////////////////////////////////

# for item in range(95, 100, 2):
#     print(item)

#///////////////////////////////////////

# prices = [10, 20 , 30]
# total = 0

# for price in prices:
#     total += price
# print(f"Total: {total}")

#///////////////////////////////////////

# for x in range(4):
#     for y in range(4):
#         print(f'({x},{y})')

# #//////////////////////////////////

# numbers = [4, 2, 6, 2, 1]

# for X in numbers:
#     print('x' * X)
    
#///////////////////////////////

# names = ['John', 'SAD', 'ALI', 'BAD', 'John', 'CAY', 'John', 'Bill', 'Sam']
# print(names[2])

#//////////////////////////
# numbers = [3, 6, 4, 23, 7, 20, 5]
# max = numbers[0]
# for number in numbers:
#     if number > max:
#         max = number

# print(max)

#////////////////////////////////

# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# print(matrix[1])

# #////////////////////////////////

# list = [2, 3, 5, 6, 7, 8]
# list.append(20)

# print(list)
#---------------------------
#  list = [2, 3, 5, 6, 7, 8]
#  list.insert(2,20)

#  print(list)
#  #/////////////////////
 
# list = [2,5,2,4,6,7]
# list.remove(5)
# print(list)

# #////////////////////////////////

# list = [2,5,2,4,6,7]
# list.pop(2)
# print(list)


#/////////////////////////////////////////

# list = [2,5,2,4,6,7]
# print(list.index(6))


# #/////////////////////////////////////////

# list = [2,5,2,4,6,7]
# print(9 in list)


#/////////////////////////////////////////

# list = [2,5,2,4,6,7]
# list.sort()
# print(list)
# //////////////////////# //////////////////////
# list = [2,5,2,4,6,7]
# list.reverse()
# print(list)

# //////////////////////# //////////////////////# //////////////////////

# numbers = [2,5,7,8,15,4]
# numbers2 = numbers.copy()
# numbers2.append(10)

# print(numbers2)

# //////////////////////# //////////////////////# //////////////////////

# numbers =[5,6,5,7,6,8,7]
# uniques =[]

# for number in numbers:
#     if number not in uniques:
#         uniques.append(number)

# print(uniques)

#/////////////////////////////////////////////////////////////
#Tupples
# numbers = (5,4,7)
# print(numbers[0])



# coordinates = (4,6,7)
# x , y , z = coordinates

# print(x,z)

#/////////////////////////////////////////////////////////////

# owner = {
#     "Name": "Sumair Javed",
#     "Email": "sumairjaved007@gmail.com",
#     "phone": "124"
# }

# partners = {
#     "Name": "Zubair Javed",
#     "Email": "sumairjaved007@gmail.com",
#     "phone": "124",
#     "Name2": "subair Javed",
#     "Email2": "fumairjaved007@gmail.com",
#     "phone2": "g24"
# }

# customers = {
#     "Name1": "Uzair Javed",
#     "Email1": "sumairjaved007@gmail.com",
#     "phone1": "124",

#     "Name2": "Zzair Javed",
#     "Email2": "sumairjaved007@gmail.com",

#     "Name3": "Szair Javed",    
#     "Email3": "sumairjaved007@gmail.com",
    
#     "Name4": "Rzair Javed",
#     "Email4": "sumairjaved007@gmail.com",
    
#     "Name5": "Gzair Javed",
#     "Email5": "sumairjaved007@gmail.com"

# }

# user = input("Enter the name for details: ")

# if user == "owner":
#     print("The owner of this organization is :")
#     print(owner)

# elif user == "partners":
#     print("The partners of this organization are: ")
#     print(partners)

# elif user == "customers":
#     print("The customers of this organization are :")
#     print(customers)

# else:
#     print("Sorry we don't have this information")

#////////////////////////////////////////////////////////
# import tkinter as tk

# # Create the main window
# root = tk.Tk()
# root.title("Simple Chatbot")
# root.geometry("400x500")  # Set window size

# # # Create a scrolled text box for displaying the conversation
# chat_display = tk.Text(root, wrap=tk.WORD, width=40, height=15, state=tk.DISABLED)
# chat_display.grid(row=0, column=0, padx=10, pady=10)

# user_entry = tk.Entry(root, width=30)
# user_entry.grid(row=1, column=0, padx=10, pady=10)

# # Create a send button that will trigger the on_send function
# send_button = tk.Button(root, text="Send")
# send_button.grid(row=2, column=0, pady=10)

# def greet_user():
#     print("Goodmorning!")
#     print("Nice to meet you Sir")

# def who_user():
#     print("I'm Sumair Javed")
#     print("Data Engineer in Idrak Ai")

# def what_user():
#     print("We're Selling over callwise bots in all over the world")
#     print("These bots are effective and in low cost")
#     print("If you interested in buying those. Please let me know!")

# def exit():
#     print("Ok Sir.")
#     print("Goodbye.")


# while True:  # Infinite loop to keep asking for user input
#     user = input("Type your message: ").lower()

#     if user == "hi" or user == "hello" or user == "salam" or user == "aoa":
#         greet_user()        
#     elif user == "who are you?":
#         who_user()
#     elif user == "what you want?":
#         what_user()
#     elif user == "no need":
#         exit()
#         break
#     else:
#         print("Sorry for Inconvenience.")
        

#////////////////////////////////////////////////////////

# def greet_user(first_name, last_name):
#     print(f'Hi {first_name} {last_name}!')
#     print("Welcome Aboard")

# greet_user(last_name="Ali", first_name="tehseen")

#/////////////////////////////////////////////////////////
# user = input("Enter the number:")
# number = int(user)

# def square(number):
#     return number * number


# result = square(number)
# print(result)

#/////////////////////////////////////////////////////////

# try:
#     age = int(input('Age: '))
#     print(age)
# except:
#     print('Please insert integer value')


#/////////////////////////////////////////////////////////

# from array import array as arr

# values = arr('i',[1,2,3,4,5])

# print(values)

# ................................

# from array import array as arr

# values = arr('i',[1,2,3,4,5])
# # values.reverse()
# print(values)


#/////////////////////////////////////////////////////////

# from array import *

# val = array('i',[2,4,4,8,7,9])

# for i in range(6):
#     print(val[i])

# ///////////////////////////////////////////////////////////////////////


# from array import *

# val = array('u',[a,b,c,d,e,f])

# for i in range(6):
#     print(val[i])


# ///////////////////////////////////////////////////////////////////////

# class  Book:
#     def __init__(self, title, quantity, author, price):
#         self.title = title
#         self.quantity = quantity
#         self.author = author
#         self.price = price

#     def __repr__(self):
#         return f"Book: {self.title}, Quantity: {self.quantity}, author: {self.author}, Price = {self.price}"  


# book1 = Book('Book 1', 12, 'Author 1', 120)
# book2 = Book('Book 2', 18, 'Author 2', 220)
# book3 = Book('Book 3', 28, 'Author 3', 320)


# print(book1)
# print(book2)
# print(book3)

# ///////////////////////////////////////////////////////////////////////

# class Student:
#     name = "Sumair"

# s1 = Student()
# print(s1.name)

# s2 = Student()
# print(s2.name)

#////////////////////////////////////////////////////

# class car:
#     color = "blue"
#     brand = "Mercedes"
#     price = 1920
# car1 = car()

# print(car1.brand)
# print(car1.color)
# print(car1.price)

#////////////////////////////////////////////////////

# class Student:
#     def __init__(self, fullname, age , Bloodgroup):
#         print("Adding a new Student in the list")
        
#         self.name = fullname
#         self.age = age
#         self.Bloodgroup= Bloodgroup

#     college_name = "Punjab College"

# s1 = Student("Ali", 28, "A-")
# s2 = Student("Zubair", 27, "A+")
# s3 = Student("Sumair", 22, "b+")
# s4 = Student("Javed", 24, "C+")
# s5 = Student("karan", 25, "A+")
# s6 = Student("Arjun", 26, "K+")

# print(s1.name)
# print(s1.age)
# print(s1.Bloodgroup)
# print(s1.college_name)
# print()


# print(s2.name)
# print(s3.age)
# print(s3.Bloodgroup)
# print(s4.college_name)
# print()


# print(s3.name)
# print(s3.age)
# print(s3.Bloodgroup)
# print(s3.college_name)
# print()

# print(s4.name)
# print(s4.age)
# print(s4.Bloodgroup)
# print(s4.college_name)
# print()

# print(s5.name)
# print(s5.age)
# print(s5.Bloodgroup)
# print(s5.college_name)
# print()

# print(s6.name)
# print(s6.age)
# print(s6.Bloodgroup)
# print(s6.college_name)

#////////////////////////////////////

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def welcome(self):
#         print("Welcome", self.name)

#     def get_marks(self):
#         print(self.marks)


# s1 = Student("Sumair Javed", 1000)
# s1.welcome()
# s1.get_marks()

#/////////////////////////////////////

# class student():
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("Hi", self.name,", your avg score is:", sum/3)

#     @staticmethod
#     def hello():
#         print("hellow")

# s1 = student("Tony", [99, 98, 85])
# s1.get_avg()
# s1.hello()


#/////////////////////////////////////

# class account:
#     def __init__(self, bal, acc):
#         self.balance = bal
#         self.account_no = acc

#     #debit method
#     def debit(self, amount):
#         self.balance -= amount
#         print("RS. ", amount, "was debited.")
#         print("total balance =", self.get_balance())

#     #debit method
#     def credit(self, amount):
#         self.balance += amount
#         print("RS. ", amount, "was credited.")
#         print("total balance =", self.get_balance())

#     #total balance
#     def get_balance(self):
#         return self.balance

# acc1 = account(1000, 9059809460396890854360)
# acc1.debit(500)
# acc1.credit(30000)
# acc1.credit(30000)
# acc1.debit(500)

#///////////////////////////////

# class Book:
#     def __init__(self, topics, price):
#         self.title = "Information Technology"
#         self.author = "Sumair Javed"
#         self.topics = topics
#         self.price = price
# book1 = Book('Machine learning', '2000')
# book2 = Book('Deep learning', '4000')

# user = input('These are the details of the book: ').lower()

# if user == "machine learning":
#     print(book1.topics)
#     print(book1.title)
#     print(book1.author)
#     print(book1.price)
# else:
#     print(book2.topics)
#     print(book2.title)
#     print(book2.author)
#     print(book2.price)

# #/////////////////////////////////////////////////

# Super Classes(OOP)

# class Book:
#     def __init__(self, title, author, topics, price):
#         self.title = title
#         self.author = author
#         self.topics = topics
#         self.price = price

# class Academic(Book):
#     def __init__(self, title, author, topics, price):
#         super().__init__(title, author, topics, price)
#         self.branch = "kuch bhi"

#     def __repr__(self):
#         return f"Book: {self.title}, Branch : {self.branch}, Author: {self.author}, Topics : {self.topics}, Price: {self.price}"

# novel1 = Academic("Advanced Machine Learning", "Jo b Hai", "deep learning etc", "sasti hai just 50 ki")
# print(novel1)

#///////////////////////////

# #how to swap values:

# a =5
# b= 10

# #print the values before swap

# print("Before swap : a =", a, "b =", b)

# #swapping the values 

# a = a+a 
# b = a-5

# #Printing the swap valuesL

# print("After swap : a =", a , "b =", b)


#////////////////////////////////////////////////////////////////////////////////////////////////////////////

#Take input from the user for their name, age, and favorite color, and print a formatted string using f-strings.


# name = input("Enter your name : ")
# age = int(input("Enter your age: "))
# favorite_color = input("Whats your favorite color: ")


# print(f"Hi, My name is {name}, and i'm {age} years old. And my favorite color is {favorite_color}.")

#////////////////////////////////////////////////////////////////////////////////////////////////////////////

#Write a program to check if a number is even or odd.

# num = int(input("Enter Number: "))

# #Check if the number is even or odd
# if num % 2 ==0:
#     print(f"{num} is and even number.") 
# else:
#     print(f"{num} is and odd number.")

#/////////////////////////////////////////////////////////////////////////////////////////////////////

# Create a simple calculator using if-elif-else that takes two numbers and an operator as input.        

# a = int(input("Enter first value: "))
# b = int(input("Enter second value: "))

# #Input the operation
# operator = input("Enter an operation you want (+,-,/,*):")

# if operator == "+":
#     result = a + b
#     print("Sum =", a+b )
# elif operator == "-":
#     result = a - b
#     print("Subtract =", a-b )
# elif operator == "*":
#     result = a * b
#     print("Multiply =", a*b )
# elif operator == "/":
#     result = a / b
#     print("Divide =", a/b )
# else:
#     print("Please write specific values.")

#/////////////////////////////////////////////////////////////////////////////////////////////////////

#Write a program to print the Fibonacci sequence up to n terms.

# n =int(input("Enter the number of terms in a febonacci sequence : "))
# #intialize the first term
# a, b = 0,1
# #print the febonacci sequence
# print("Febonnaci Sequence:")
# for i in range(n):
#     print(a, end="")
#     a, b = b, a+b


#/////////////////////////////////////////////////////////////////////////////////////////////////////

#Create a multiplication table generator for a number provided by the user.

# a = int(input("Enter your number for multiplication: "))


# print(f"\nMultiplication table for {a}:")
# for i in range(1,11):
#     result = a * i
#     print(f"{a} * {i} = {result}")

#////////////////////////////////////////////////////////////////////////////////////////////////////
#Write a program to find the largest number in a list without using the max() function.

# list = [5,14,7,9]
# # largest = list[0]

# for i in list:
#     if i > largest:
#         largest = i

# print(f"The largest number in list is : {largest}")

#////////////////////////////////////////////////////////////////////////////////////////////////////

#Input: List of numbers
# numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]

# # Initialize a variable to hold the largest number
# largest = numbers[0]

# # Loop through the list to find the largest number
# for num in numbers:
#     if num > largest:
#         largest = num

# print(f"The largest number in the list is: {largest}")

#////////////////////////////////////////////////////////////////////////////////////////////////////

# def factorial(n):
#     # Check if the number is negative, zero, or positive
#     if n < 0:
#         return "Factorial is not defined for negative numbers."
#     elif n == 0 or n == 1:
#         return 1
#     else:
#         result = 1
#         for i in range(1, n + 1):
#             result *= i
#         return result

# # Input from the user
# num = int(input("Enter a number to find its factorial: "))

# # Call the factorial function and print the result
# print(f"The factorial of {num} is: {factorial(num)}")

#///////////////////////////////////////////////

# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade

#     def display_details(self):
#         print(f"Student name : {self.name}")
#         print(f"Student age : {self.age}")
#         print(f"Student grades :{','.join(map(str, self.grade))}")

#     def calculate_average(self):
#         if len(self.grade) == 0:
#             return 0
#         return sum(self.grade) / len(self.grade)
        
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# grades = list(map(int, input("Enter the student's grades (separated by space): ").split()))

# student1 = Student(name,age,grades)
# student1.display_details()
# average= student1.calculate_average()
# print(f"The average grade is {average:.2f}.")
# print()

#//////////////////////////////////////////
class ATM:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: ${amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrew: ${amount}")

    def check_balance(self):
        return f"Balance: ${self.balance}"
    
def atm_operations():
    atm = ATM(20000)

    while True:
        user = input("How can i Help you? (bal/deposit/withdraw/exit)")

        if user == "bal":
            print(atm.check_balance())
        elif user == "deposit":
            amount = int(input("Enter deposited amount: "))
            atm.deposit(amount)
            print(atm.check_balance())
        elif user == "withdraw":
            amount = int(input("Enter withdraw amount: "))
            atm.withdraw(amount)
            print(atm.check_balance())
        elif user == "exit":
            print("Thank You for using our ATM.")
            break
        else:
            print("Invalid Operation.")


atm_operations()




# # Testing ATM system
# atm = ATM(500)

# deposit_value = int(input("How much you want to deposit:"))
# withdraw_deposit = int(input("How much you want to withdraw:"))

# if user == deposit_value:
#     bal = atm + atm.deposit
#     print("amoun")
# elif user == withdraw_deposit:
#     bal = atm - atm.withdraw
# elif user == "bal":
#     bal = atm.check_balance






