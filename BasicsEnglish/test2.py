# def decorator(func):
#
#     def wrapper(*args, **kwargs):
#         print('this is your information')
#         main = func(*args, **kwargs)
#         print('see you next time')
#
#         return main
#     return wrapper()
#
#
# @decorator
# def info():
#     print('x')
#
#
#

def timer(f):
    def wrapper(*args, **kwargs):
        print('Start')
        main = f(*args, **kwargs)
        print('End')
        return main

    return wrapper


@timer
def adder(a, b):
    print(a + b)


adder(1, 2)





