def equilateral(sides):
    """
    PARAM: sides - list with all 3 sides of the triangle
    RETURN: True if the triangle is an equilateral triangle, otherwise False
    """
     # Unpacking the sides into variables a, b, c
    a, b, c = sides


    # Checking if the triangle is scalene by ensuring:
    # 1. all sides are equal and greater than 0
    # 2. All sides are greater than 0
    # 3. The sum of any two sides is greater than the third side (triangle inequality theorem)
    return (a == b and c == b and c == a) and (a > 0 and b > 0 and c > 0) and (a + b >= c and b + c >= a and a + c >= b)


def isosceles(sides):
    """
    PARAM: sides - list with all 3 sides of the triangle
    RETURN: True if the triangle is an isosceles triangle, otherwise False
    """
    # Unpacking the sides into variables a, b, c
    a, b, c = sides
    
    # Checking if the triangle is scalene by ensuring:
    # 1. at least two sides are equal to identify an isosceles triangle
    # 2. All sides are greater than 0
    # 3. The sum of any two sides is greater than the third side (triangle inequality theorem)
    return (a + b >= c and b + c >= a and a + c >= b) and (a > 0 and b > 0 and c > 0) and (a == c or b == a or c == b)

    
def scalene(sides):
    """
    PARAM: sides - list with all 3 sides of the triangle
    RETURN: True if the triangle is a scalene triangle, otherwise False
    """
    # Unpacking the sides into variables a, b, c
    a, b, c = sides
    
    # Checking if the triangle is scalene by ensuring:
    # 1. All sides have different lengths
    # 2. All sides are greater than 0
    # 3. The sum of any two sides is greater than the third side (triangle inequality theorem)
    return (a != b and c != b and a != c) and (a > 0 and b > 0 and c > 0) and (a + b >= c and b + c >= a and a + c >= b)