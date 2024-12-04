# Here are some simple recursive algorithms in Python, where the function calls itself to solve a problem. Recursive algorithms typically have two components:

#     Base Case: This is the condition that stops the recursion.
#     Recursive Case: This part breaks the problem into smaller subproblems, which are solved by the recursive call.

# 1. Factorial Calculation:
#     The factorial of a number n is the product of all positive integers less than or equal to n. For example, 5! = 5 * 4 * 3 * 2 * 1.

# def iterative_factorial(n):
#     fact = 1
#     for i in range(2, n+1):
#         fact *= i
#     return fact
# factorial = iterative_factorial(7)
# print(factorial)

#///////////////////////////////////////////////////////////
#recurren Factorial 

# def rec_factorial(n):
#     if n == 1:
#         return n
#     else:
#         temp = rec_factorial(n-1)
#         temp = temp * n
#     return temp

# recurrentfactorial = rec_factorial(5)
# print(recurrentfactorial)

#//////////////////////////////////////////////////////////////

#2. Fibonacci Sequence
#The Fibonacci sequence is defined by F(0) = 0, F(1) = 1, and F(n) = F(n-1) + F(n-2) for n > 1.

# def fibonacci(n):
#     # Base case: F(0) = 0, F(1) = 1
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

# # Example usage
# print(fibonacci(12))  

#/////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////

#permutation

# def permute(string, pocket=""):
#     if len(string) == 0:
#         print(pocket)
#     else:
#         for i in range(len(string)):
#             letter = string[i]
#             front = string[0:i]
#             back = string[i+1:]
#             together = front + back
#             permute(together, letter + pocket)

# print(permute("ABC", ""))