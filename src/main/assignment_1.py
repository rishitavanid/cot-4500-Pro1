import math

# Function to approximate a number 'x' to 'n' decimal places
def approximation_algorithm(x, n):
    return round(x, n)

# Bisection Method
def bisection_method(func, a, b, tol):
    while (b - a) / 2.0 > tol:
        midpoint = (a + b) / 2.0
        if func(midpoint) == 0:
            return midpoint
        elif func(a) * func(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint
    return (a + b) / 2.0

# Fixed Point Iteration
def fixed_point_iteration(func, x0, tol, max_iter):
    for i in range(max_iter):
        x1 = func(x0)
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1
    raise ValueError("Failed to converge")

# Newton-Raphson Method
def newton_raphson(func, func_deriv, x0, tol, max_iter):
    for i in range(max_iter):
        x1 = x0 - func(x0) / func_deriv(x0)
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1
    raise ValueError("Failed to converge")

if __name__ == "__main__":
    # Example function: f(x) = x^2 - 4
    def example_func(x):
        return x**2 - 4

    # Derivative: f'(x) = 2x
    def example_func_deriv(x):
        return 2*x

    # Bisection method
    print("Bisection Method:", bisection_method(example_func, 0, 3, 0.001))

    # Fixed Point Iteration: Use Babylonian iteration for sqrt(4)
    print("Fixed Point Iteration:",
          fixed_point_iteration(lambda x: 0.5 * (x + 4/x), 2, 0.001, 100))

    # Newton-Raphson method
    print("Newton-Raphson Method:",
          newton_raphson(example_func, example_func_deriv, 2, 0.001, 100))
