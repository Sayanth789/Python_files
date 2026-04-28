from sympy import symbols, solve 

x = symbols('x')

equations = input("Enter equation = 0 : ")

expr = eval(equations)


answers = solve(expr, x)

print("solutions:", answers)