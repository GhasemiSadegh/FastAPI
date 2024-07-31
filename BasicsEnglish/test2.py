# # def decorator(func):
# #
# #     def wrapper(*args, **kwargs):
# #         print('this is your information')
# #         main = func(*args, **kwargs)
# #         print('see you next time')
# #
# #         return main
# #     return wrapper()
# #
# #
# # @decorator
# # def info():
# #     print('x')
# #
# #
# #
#
# def timer(f):
#     def wrapper(*args, **kwargs):
#         print('Start')
#         main = f(*args, **kwargs)
#         print('End')
#         return main
#
#     return wrapper
#
#
# @timer
# def adder(a, b):
#     print(a + b)
#
#
# adder(1, 2)
#
#
#
#
#
#
# def count_up_to(n):
#     count = 1
#     while count <= n:
#         yield count
#         count += 1
#
#
# my_count = count_up_to(10)
#
# print(next(my_count))
# print(next(my_count))
# print(next(my_count))
# print(next(my_count))

from fastapi import FastAPI, Depends

app = FastAPI()


def function():
    x = 1
    return x + 1


@app.get("/items/")
async def vabaste(y: int = Depends(function)):
    return {"result": y + 1}

