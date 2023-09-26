'''
Elizabeth McAllister
CSC110
Project -1
This program has four functions that calculate the area of various shapes
'''

def rectangle_area(base,height):
    '''
    This functions returns the area of a rectangle
    Args:
        base: length of the base of the rectangle as a float
        height: length of the height of the rectangle as a float
    Returns: 
        The area of the rectangle as a float
    '''
    area = base * height
    return area
print(rectangle_area(2.444444,10))


def triangle_area(a,b,c):
    '''
    This functions returns the area of a triangle using Heron's formula
    Args:
        a: length of side a of the triangle as a float
        b: length of side b of the triangle as a float
        c: length of side c of the triangle as a float
        s: the semiperimeter as a float
    Returns: 
        The area of the triangle as a float
    '''
    s = (a + b + c)/2 # calculates the semiperimeter to be used in the area
    area = (s * (s - a) * (s - b) * (s - c))**(1/2)
    return area
print(triangle_area(6,3,5))

def trapezoid_area(base_1,base_2,height):
    '''
    This functions returns the area of a trapezoid
    Args:
        base_1: length of the base_1 of the trapezoid as a float
        base_2: length of the base_2 of the trapezoid as a float
        height: length of the height of the trapezoid as a float
    Returns: 
        The area of the trapezoid as a float
    '''
    area = (1/2) * (base_1 + base_2) * height
    return area
print(trapezoid_area(3,4,5))

def circle_area(radius):
    '''
    This functions returns the area of a circle
    Args:
        radius: length of the radius of the circle as a float
    Returns: 
        The area of the rectangle as a float rounded to the second decimal place
    '''
    area = 3.1415 * (radius)**2
    return round(area,2)
print(circle_area(4))