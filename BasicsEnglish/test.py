def printer(func):
    def tazeenkonande(*args, **kwargs):
        print('Start')
        main = func(*args, **kwargs)
        print('End')
        return main

    return tazeenkonande()


@printer
def x():
    print('I am x.')


@printer
def y():
    print('I am y.')


@printer
def z():
    print('I am z.')