import cmath
import math

print("""
This is a simple Quadratic equation calculator.
Use it and enjoy!!
""")
a = input("What is the coefficient of x^2 term? ")
b = input("What is the coefficient of x term? ")
c = input("What is the coefficient of constant term? ")
a = float(a)
b = float(b)
c = float(c)
D = ((b ** 2) - 4 * a * c)
D = float(D)
if D >= 0:
    sol1 = (-b - math.sqrt(D)) / (2 * a)
    sol2 = (-b + math.sqrt(D)) / (2 * a)

    print('The solutions are {0} and {1}'.format(sol1, sol2))
elif D < 0:
    sol1 = (-b - cmath.sqrt(D)) / (2 * a)
    sol2 = (-b + cmath.sqrt(D)) / (2 * a)

    print('The roots or zeros are {0} and {1}'.format(sol1, sol2))
else:
    print("Sorry I don't understand!!")
