def decorator(func):

    def wrapper(*args, **kwargs):
        print('this is your information')
        main = func(*args, **kwargs)
        print('see you next time')

        return main
    return wrapper()


@decorator
def info():
    print('x')



