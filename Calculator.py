import math
def calc_choice():
    print("Welcome to the Calculator! Here are your options:")
    print("""
    A - Normal calculator
    B - Geometric calculator
    """)
    calc_choice = input("What would you like to do? ")
    if calc_choice == "A" or calc_choice == "a":
        calc()
    elif calc_choice == "B" or calc_choice == "b":
        geometry_calc()
def calc():
    operator = input("Enter an operator (+ - * ** /) ")
    try:
        num1 = float(input("Enter first number "))
        num2 = float(input("Enter second number "))
    except ValueError:
       print("I said a number dummy")
       exit()
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "**":
        result = num1 ** num2

    elif operator == "/":
        try:
            result = num1 / num2
        except ZeroDivisionError:
            print("Don't do that.")
            exit()
    else:
        result = "operator not recognised"


    if result == type(float):
        print(round(result),2)
    else:
        print(result)
def geometry_calc():
    print("Welcome to the Geometry Calculator! Here are your options:")
    print("""
    A - Area/Perimeter
    B - Volume/Surface Area
    C - Hypotenuse
    """)
    geometry_calc = input("What would you like to do? ")
    if geometry_calc == "A" or geometry_calc == "a":
        a_or_p_calc()
    elif geometry_calc == "B" or geometry_calc == "b":
        v_or_sa_calc()
    elif geometry_calc == "C" or geometry_calc == "c":
        hypotenuse_calc()
def a_or_p_calc():
    print("Welcome to the area and perimeter calculator! Here are your options:")
    print(""" 
    A - Circle 
    B - Square 
    C - Rectangle 
    D - Triangle (area only)
    """)
    a_or_p_calc = input("What would you like to do? ")
    if a_or_p_calc == "A" or a_or_p_calc == "a":
        measurement_circle = input("Enter preferred unit of measurement: ")
        radius = float(input("Enter radius "))
        area_circle = float(round(math.pi * radius ** 2, 2))
        perimeter = float(round(math.pi * radius * 2, 2))
        print(f"The area of the circle is {area_circle}{measurement_circle}²")
        print(f"The perimeter of the circle is {perimeter}{measurement_circle}")
    elif a_or_p_calc == "B" or a_or_p_calc == "b":
        measurement_square = input("Enter preferred unit of measurement: ")
        side_length = input("Enter side length: ")
        area_square = float(round(side_length ** 2, 2))
        perimeter_square = float(round(side_length * 4, 2))
        print(f"The area of the square is {area_square}{measurement_square}²")
        print(f"The perimeter of the square is {perimeter_square}{measurement_square}")
    elif a_or_p_calc == "C" or a_or_p_calc == "c":
        measurement_rectangle = input("Enter preferred unit of measurement: ")
        length_rectangle = float(input("Enter length of rectangle: "))
        width_rectangle = float(input("Enter width of rectangle: "))
        area_rectangle = float(round(length_rectangle * width_rectangle, 2))
        perimeter_rectangle = float(round(length_rectangle * 2 + width_rectangle * 2, 2))
        print(f"The area of the rectangle is {area_rectangle}{measurement_rectangle}²")
        print(f"The perimeter of the rectangle is {perimeter_rectangle}{measurement_rectangle}")
    elif a_or_p_calc == "D" or a_or_p_calc == "d":
        measurement_triangle = input("Enter preferred unit of measurement: ")
        base_triangle = float(input("Enter length of base of triangle: "))
        height_triangle = float(input("Enter perpendicular height of triangle: "))
        area_triangle = float(round((base_triangle * height_triangle)/2, 2))
        print(f"The area of the triangle is {area_triangle}{measurement_triangle}²")
def v_or_sa_calc():
    print("Welcome to the volume and surface area calculator! Here are your options:")
    print("""
    A - Cube
    B - Rectangular prism
    C - Sphere
    """)
    volume_calc = input("What would you like to do? ")
    if volume_calc == "A" or volume_calc == "a":
        cube_measurement = input("Enter preferred unit of measurement: ")
        cube_length = float(input("Enter side length of cube: "))
        cube_volume = float(round(cube_length ** 3, 2))
        cube_surface_area = float(round(6 * cube_length ** 2, 2))
        print(f"The volume of the cube is {cube_volume}{cube_measurement}³")
        print(f"The surface area of the cube is {cube_surface_area}{cube_measurement}²")
    elif volume_calc == "B" or volume_calc == "b":
        rectangular_prism_measurement = input("Enter preferred unit of measurement: ")
        rectangular_prism_length = float(input("Enter length of rectangular prism: "))
        rectangular_prism_width = float(input("Enter width of rectangular prism: "))
        rectangular_prism_height = float(input("Enter height of rectangular prism: "))
        rectangular_prism_volume = float(round(rectangular_prism_length * rectangular_prism_width * rectangular_prism_height, 2))
        rectangular_prism_surface_area = float(round(rectangular_prism_length * 2 + rectangular_prism_width * 2 + rectangular_prism_height * 2, 2))
        print(f"The volume of the rectangular prism is {rectangular_prism_volume}{rectangular_prism_measurement}³")
        print(f"The surface area of the rectangular prism is {rectangular_prism_surface_area}{rectangular_prism_measurement}²")
    elif volume_calc == "C" or volume_calc == "c":
        sphere_measurement = input("Enter preferred unit of measurement: ")
        sphere_radius = input("Enter radius of sphere: ")
        sphere_volume = float(round((4/3) * math.pi * sphere_radius ** 3, 2))
        sphere_surface_area = float(round(4 * math.pi * sphere_radius * sphere_radius, 2))
        print(f"The volume of the sphere is {sphere_volume}{sphere_measurement}³")
        print(f"The surface area of the sphere is {sphere_surface_area}{sphere_measurement}²")
def hypotenuse_calc():
    hypotenuse_measurement = input("Enter preferred unit of measurement: ")
    hypotenuse_height = float(input("Enter height of triangle: "))
    hypotenuse_base = float(input("Enter length of base of triangle: "))
    hypotenuse = float(round((hypotenuse_base ** 2 + hypotenuse_height ** 2) ** 0.5, 2))
    print(f"The length of the hypotenuse is {hypotenuse}{hypotenuse_measurement}")

calc_choice()
