# from typing import Annotated
#
#
# def sums(a: Annotated[int, (0, 10)], b: int):
#     return a + b

def timer(f):
    def wrapper(*args, **kwargs):
        print('Start')
        main = f(*args, **kwargs)
        print('End')
        return main
    return wrapper()
