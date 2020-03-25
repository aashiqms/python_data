def main_function():
    for x in range(0, 10):
        x = triple(x)
        print('cubes are {}'.format(x))

    for x in range(0, 10):
        x = square(x)
        print('squares are {}'.format(x))


def triple(a):
    cube = a * a * a
    return cube


def square(b):
    squares = b * b
    return squares

main_function()

