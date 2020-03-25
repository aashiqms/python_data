# Create a program that can compute the areas of three shapes, triangles, rectangles and circles, when their dimensions are given.

# An endless loop should ask for which shape you want the area be calculated. An empty string as input will exit the loop. If the user gives a string that is none of the given shapes, the message “unknown shape!” should be printed. Then it will ask for dimensions for that particular shape. When all the necessary dimensions are given, it prints the area, and starts the loop all over again. Use format specifier f for the area.

# What happens if you give incorrect dimensions, like giving string “aa” as radius? You don’t have to check for errors in the input.


def area_of_rectangle(rectangle_width = 1, rectangle_length = 1):
    area_rectangle = rectangle_length * rectangle_width
    return area_rectangle


def area_of_triangle(triangle_base = 1, triangle_height = 1):
    area_triangle = triangle_base * triangle_height
    return area_triangle


def area_of_circle(circle_radius = 1):
    area_circle = 3.1415 * circle_radius * circle_radius
    return area_circle
  
    
user_choice = input('enter the shape for which area to be found "rectangle", "triangle", "circle" ')


if __name__ == "__main__": 
    while(user_choice != ''):
        if user_choice == 'rectangle':
            width = int(input('enter width: '))
            length = int(input('enter length: '))
            let = area_of_rectangle(width, length)
            print('the area of rectangle is {}'.format(let)) 
            user_choice = input('enter the shape for which area to be found "rectangle", "triangle", "circle" ')
        elif user_choice == 'triangle':
            triangle_base = int(input('enter base: '))
            triangle_height = int(input('enter height '))
            let = area_of_triangle(triangle_base, triangle_height)
            print('the area of triangle is {}'.format(let))
            user_choice = input('enter the shape for which area to be found "rectangle", "triangle", "circle" ')       
        elif user_choice == 'circle':
            circle_radius = int(input('enter radius: '))
            let = area_of_circle(circle_radius)
            print('the area of circle is {:.3f}'.format(let))
            user_choice = input('enter the shape for which area to be found "rectangle", "triangle", "circle" ')
        else:
            print('wrong name entered: ')
            user_choice = input('enter the shape for which area to be found "rectangle", "triangle", "circle" ')

    
    

    
    
    

