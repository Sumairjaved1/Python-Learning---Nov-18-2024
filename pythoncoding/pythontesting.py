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