# A function that calculates the derivative:

# Rule: d/dx(x^n) = n * x^n

def derivative(expr):
    expr = expr.strip()

    if expr.startswith('x **'):
       
        try:
          
            m = int(expr.split("**")[1].strip())
        except (IndexError, ValueError):
            raise ValueError("Invalid format. Make sure  the input is like 'x **'3")

    # Handle special case: m == 0 (derivative of constant is 0)
        if m == 0:
            return "The derivative of a constant is: 0"
        # Construction of derivative expression.

        if m - 1 == 0:
            return f"The derivative is: {m}"
        elif m - 1 == 1:
            return f"The derivative is: {m} *  x"
        else:
            return f"The derivative is: {m} * x ** {m - 1}"
        
    # Adding trig: values.
    trig_derivatives = {
        "sin(x)":"cos(x)", 
        "cos(x)":"-sin(x)",
        "tan(x)":"sec(x) ** 2",
        "sec(x)":"sec(x) * tan(x)",
        "csc(x)": "-csc(x) * cot(x)",
        "cot(x)":"-csc(x) ** 2"
    }

    if expr in trig_derivatives:
        return trig_derivatives[expr]
    raise ValueError("Unsupported expression format.")
# Examples:
print(derivative("x ** 3"))
print(derivative("x ** 1")) 
print(derivative("x ** 0"))
print(derivative("sin(x)"))   
print(derivative("cos(x)"))   
print(derivative("tan(x)"))   