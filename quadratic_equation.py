def solve_quadratic(a, b, c):
    """
    A function to solve quadratic equation
    :return:
    x value of the quadratic equation as pair of tuples
    eg: print(solve_quadratic(1,-3,2))
        (2.0,1.0)
        print(solve_quadratic(1,2,1))
        (-1.0,-1.0)
    """
# ax2+bx+c=0
    y = (b ** 2) - (4 * a) * c
    top_a = -b + (y ** 0.5)
    top_b = -b - (y ** 0.5)
    bottom = 2 * a
    x_a = top_a / bottom
    x_b = top_b / bottom
    x_answer = (x_a, x_b)
    return x_answer


print(solve_quadratic(1, -3, 2))


solve_quadratic(1, -3, 1)







