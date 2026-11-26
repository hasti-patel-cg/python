# section A


# # que 1
# def show(n):
#     if n == 0:
#         print("Stop")
#         return
#     print(n)
#     show(n - 1)
#     print(n)
# show(2)
# output =  2
#           1
#         Stop
#           1
#          2
         

# # que 2
# def total(n):
#     if n == 0:
#         return 0
#     return n + total(n - 1)
# base-case = if n==0:
#              return 0

# # que 3
# def count(n):
#     if n == 0:
#         return
#     count(n + 1)
# bug = we are not calling the function.

# # que 4
# def answer(n):
#     if n == 0:
#         return 0
#     n + answer(n - 1)
# print(answer(3))
# on 36th line return i will write

# # que 5
# def countdown(n):
#     if n ==0:
#         return "Done!"
#     print(n)
#     return countdown(n-1)
# print(countdown(3))