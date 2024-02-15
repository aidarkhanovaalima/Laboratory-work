#EX1
def perimeter_of_square(a):
return a * 4 

a = float(input("Введите длину стороны квадрата: "))
print("Периметр квадрата равен:", perimeter_of_square(a))

#EX2
def area_of_square(a):
return a * a

a = float(input("Введите длину стороны квадрата: "))
print("Площадь квадрата равен:", area_of_square(a))

#EX3
def perimeter_of_rectangle(a, b):
return (a+b) * 2
# def area_of_rectangle(a, b):
#     return a * b

# a = float(input("Введите длину прямоугольника: "))
# b = float(input("Введите ширину прямоугольника: "))

# area = area_of_rectangle(a, b)
# perimeter = perimeter_of_rectangle(a, b)

# print("Площадь прямоугольника равна:", area)
# print("Периметр прямоугольника равен:", perimeter)

#EX4
# def length_of_circle(diameter):
#     pi = 3.14
#     return pi * diameter

# d = float(input("Введите диаметр окружности: "))
# length = length_of_circle(d)

# print("Длина окружности равна:", length)

#EX5
# def volume_of_cube(a):
#     return a * a * a

# def surface_area_of_cube(a):
#     return 6 * a * a

# a = float(input("Введите длину ребра куба: "))
# volume = volume_of_cube(a)
# surface_area = surface_area_of_cube(a)

# print("Объем куба равен:", volume)
# print("Площадь поверхности куба равна:", surface_area)

#EX6
# def volume_of_rectangular_prism(a, b, c):
#     return a * b * c

# def surface_area_of_rectangular_prism(a, b, c):
#     return 2 * (a * b + b * c + a * c)

# a = float(input("Введите длину ребра a: "))
# b = float(input("Введите длину ребра b: "))
# c = float(input("Введите длину ребра c: "))

# volume = volume_of_rectangular_prism(a, b, c)
# surface_area = surface_area_of_rectangular_prism(a, b, c)

# print("Объем прямоугольного параллелепипеда равен:", volume)
# print("Площадь поверхности прямоугольного параллелепипеда равна:", surface_area)

#EX7
# def circumference_of_circle(radius):
#     pi = 3.14
#     return 2 * pi * radius

# def area_of_circle(radius):
#     pi = 3.14
#     return pi * radius ** 2

# R = float(input("Введите радиус круга: "))

# circumference = circumference_of_circle(R)
# area = area_of_circle(R)

# print("Длина окружности равна:", circumference)
# print("Площадь круга равна:", area)

#E8
# def average(a, b):
#     return (a + b) / 2

# a = float(input("Введите первое число a: "))
# b = float(input("Введите второе число b: "))

# result = average(a, b)
# print("Среднее арифметическое чисел", a, "и", b, "равно:", result)

#EX9
# import math

# def geometric_mean(a, b):
#     return math.sqrt(a * b)

# a = float(input("Введите первое число a: "))
# b = float(input("Введите второе число b: "))

# result = geometric_mean(a, b)
# print("Среднее геометрическое чисел", a, "и", b, "равно:", result)

# #EX10
# def calculate_operations(a, b):
#     sum_result = a + b
#     diff_result = a - b
#     prod_result = a * b
    
#     if b != 0:
#         div_square_result = (a**2) / (b**2)
#     else:
#         div_square_result = float('inf') if num1 > 0 else float('-inf')  
#     return sum_result, diff_result, prod_result, div_square_result

# a = float(input("Введите первое число: "))
# b = float(input("Введите второе число: "))


# sum_result, diff_result, prod_result, div_square_result = calculate_operations(a, b)

# print("Сумма:", sum_result)
# print("Разность:", diff_result)
# print("Произведение:", prod_result)
# print("Частное их квадратов:", div_square_result)

#EX11
# def calculate_operations(a, b):
#     sum_result = abs(a) + abs(b)
#     diff_result = abs(a) - abs(b)
#     prod_result = abs(a) * abs(b)
    
#     if b != 0:
#         div_result = abs(a) / abs(b)
#     else:
#         div_result = float('inf') if num1 > 0 else float('-inf')  
#     return sum_result, diff_result, prod_result, div_result


# a = float(input("Введите первое число: "))
# b = float(input("Введите второе число: "))

# sum_result, diff_result, prod_result, div_result = calculate_operations(a, b)

# print("Сумма модулей:", sum_result)
# print("Разность модулей:", diff_result)
# print("Произведение модулей:", prod_result)
# print("Частное модулей:", div_result)

#EX12
# import math

# def calculate_hypotenuse_and_perimeter(a, b):
    
#     hypotenuse = math.sqrt(a*a + b*b)
#     perimeter = a + b + hypotenuse
#     return hypotenuse, perimeter

# a = float(input("Введите длину катета a: "))
# b = float(input("Введите длину катета b: "))

# hypotenuse, perimeter = calculate_hypotenuse_and_perimeter(a, b)

# print("Гипотенуза треугольника:", hypotenuse)
# print("Периметр треугольника:", perimeter)

#EX13

# def calculate_areas(R1, R2):
#     pi = 3.14
#     S1 = pi * R1**2
#     S2 = pi * R2**2
#     S3 = pi * (R1**2 - R2**2)
    
#     return S1, S2, S3


# R1 = float(input("Введите радиус R1 (больший радиус): "))
# R2 = float(input("Введите радиус R2 (меньший радиус): "))

# if R1 > R2:
   
#     S1, S2, S3 = calculate_areas(R1, R2)

#     print("Площадь круга S1:", S1)
#     print("Площадь круга S2:", S2)
#     print("Площадь кольца S3:", S3)
# else:
#     print("Ошибка: R1 должно быть больше R2.")

#EX14
# def calculate_radius_and_area(L):
#     pi = 3.14
#     R = L / (2 * pi)
#     S = pi * R**2
#     return R, S

# L = float(input("Введите длину окружности L: "))

# R, S = calculate_radius_and_area(L)

# print("Радиус круга:", R)
# print("Площадь круга:", S)

# #EX15
# import math

# def calculate_diameter_and_circumference(S):
#     pi = 3.14
#     R = math.sqrt(S / pi)
#     D = 2 * R
#     L = 2 * pi * R
#     return D, L

# S = float(input("Введите площадь круга S: "))

# D, L = calculate_diameter_and_circumference(S)

# print("Диаметр круга:", D)
# print("Длина окружности:", L)

# #EX16
# def distance_between_points(x1, x2):
#     return abs(x2 - x1)

# x1 = float(input("Введите координату x1: "))
# x2 = float(input("Введите координату x2: "))

# distance = distance_between_points(x1, x2)
# print("Расстояние между точками:", distance)

# #EX17
# def calculate_lengths_and_sum(A, B, C):
#     length_AC = abs(C - A)
#     length_BC = abs(C - B)
#     sum_lengths = length_AC + length_BC
#     return length_AC, length_BC, sum_lengths

# A = float(input("Введите координату точки A: "))
# B = float(input("Введите координату точки B: "))
# C = float(input("Введите координату точки C: "))

# length_AC, length_BC, sum_lengths = calculate_lengths_and_sum(A, B, C)

# print("Длина отрезка AC:", length_AC)
# print("Длина отрезка BC:", length_BC)
# print("Сумма длин отрезков AC и BC:", sum_lengths)

#EX18
# def calculate_product_of_lengths(A, B, C):
  
#     length_AC = abs(C - A)
#     length_BC = abs(B - C)
#     product_of_lengths = length_AC * length_BC
#     return product_of_lengths

# A = float(input("Введите координату точки A: "))
# B = float(input("Введите координату точки B: "))
# C = float(input("Введите координату точки C (между A и B): "))
# product = calculate_product_of_lengths(A, B, C)

# print("Произведение длин отрезков AC и BC:", product)

# #EX19
# def calculate_perimeter_and_area(x1, y1, x2, y2):
#     base = abs(x2 - x1)
#     height = abs(y2 - y1)
#     perimeter = 2 * (base + height)
#     area = base * height
#     return perimeter, area

# x1 = float(input("Введите x1: "))
# y1 = float(input("Введите y1: "))
# x2 = float(input("Введите x2: "))
# y2 = float(input("Введите y2: "))

# perimeter, area = calculate_perimeter_and_area(x1, y1, x2, y2)

# print("Периметр прямоугольника:", perimeter)
# print("Площадь прямоугольника:", area)

#EX20
import math

def calculate_distance(x1, y1, x2, y2):
    
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return distance

x1 = float(input("Введите x1: "))
y1 = float(input("Введите y1: "))
x2 = float(input("Введите x2: "))
y2 = float(input("Введите y2: "))

distance = calculate_distance(x1, y1, x2, y2)

print("Расстояние между точками:", distance)