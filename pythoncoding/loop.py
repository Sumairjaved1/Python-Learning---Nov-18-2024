# name = "Sumair"
# for i in name:
#     print("Sumair", end=",")

#/////////////////////////////

# name = "Sumair"
# for i in name:
#     print(i)

#/////////////////////////////

# name = "Sumair"
# for i in name:
#     print(i)
#     if i == "u":
#         print("This is something special")

#////////////////////////////////

# colors= ["Red", "Green", "Blue"]
# for i in colors:
#     print(i)
#     for j in i:
#         print(j)

#////////////////////////////////

# for k in range(5):
#     print(k+2)

#////////////////////////////////

# for k in range(5, 15, 3):
#     print(k)

#////////////////////////////////
#While loops

# i = 0

# while i <= 5:
#     print(i)
#     i = i + 1
# print("Done with the loop")

#///////////////////////////////////////
# i = 0
# while i < 10:
#     i = int(input("Enter You Number:"))
#     print(i)
# print("Done with the loop")


#///////////////////////////////////////

# count = 5

# while count > 0:
#     print(count)
#     count = count-1
# else:
#     print("Hello")

#///////////////////////////////////////

# for i in range(12):
#     if i == 5:
#         break
#     print("5 X ", i+1, "=", 5*i)
   
# print("loop left")

#///////////////////////////////////////


# for i in range(12):
#     if i == 5:
#         print("Skip the iteration")
#         continue
#     print("5 X ", i+1, "=", 5*i)


#///////////////////////////////////////
#nested loop
# for x in range(3):
#     for x in range(1, 10):
#         print(x, end="")
#     print()

#///////////////////////////////////////
# rows = int(input("Enter rows: "))
# col = int(input("Enter cols: "))
# symbol = input("Enter a symbol to use")

# for x in range(rows):
#     for y in range(col):
#         print(symbol, end="")

#     print()
          
# ////////////////////////////////////////////////

# n = 5

# for i in range(n):
#     for j in range(i + 1):
#         print("#", end=" ")
#     print()  

#/////////////////////////////////
# n = 5
# for i in range(n):
#     for j in range(i,n):
#         print("", end=" ")
#     for j in range(i+1):
#         print("#", end=" ")
#     print()
#/////////////////////////////////
# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print("", end=" ")
#     for j in range(i,n):
#         print("#", end="")
#     print()
# /////////////////////////////////////////////////

#NESTED LOOP

#////////////////////////////////////////////////////////////
# n=5
# for i in range(n):
#     for j in range(n):
#         print("#", end='')
#     print()
#////////////////////////////////////////
# n=5
# for i in range(n):
#     for j in range(i+1):
#         print("#", end='')
#     print()
#////////////////////////////////////
# n = 5
# for i in range(n):
#     for j in range(i, n):
#         print("#", end=" ")
#     print()
#///////////////////////////////////////
# n = 5
# for i in range(n):
#     # Print leading spaces
#     for j in range(n - i - 1):
#         print(" ", end="")
    
#     # Print hashes
#     for j in range(i + 1):
#         print("#", end="")
    
#     # Move to the next line
#     print()

    