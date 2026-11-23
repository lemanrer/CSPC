"""
PW2 Lab B Part 2 -- three routes to a minimum.

Compare gradient descent, Newton, and SLSQP on two functions:
  2A: f(x) = (x-3)**2 + 1          (easy, one minimum at x=3)
  2B: g(x) = x**4 - 3*x**2 + x + 5 (harder, several stationary points)
Run:  python warmup.py
"""
import numpy as np
from scipy.optimize import newton, minimize

# ---------- 2A: easy convex function ----------
def f(x):   return (x-3)**2 + 1
def df(x):  return 2*(x-3)
def d2f(x): return 2.0

# TODO 2A: minimise f three ways from x0=0 and print each result:
#   (1) gradient descent by hand (loop x = x - lr*df(x) until the step is tiny)
x = 0.0
lr = 0.1
tol = 1e-10
for i in range(10000):
    x_new = x - lr * df(x)
    if abs(x_new - x) < tol:
        x = x_new
        break
    x = x_new
print("2A - Gradient Descent")
print("Minimum x =", x)
print("Minimum f(x) =", f(x))

#   (2) scipy.optimize.newton(df, x0, fprime=d2f)
x_newton = newton(df, x0=0, fprime=d2f)
print("\n2A - Newton's Method")
print("Minimum x =", x_newton)
print("Minimum f(x) =", f(x_newton))

#   (3) scipy.optimize.minimize(f, x0, method="SLSQP")
result = minimize(f, x0=[0], method="SLSQP")
print("\n2A - SLSQP")
print("Minimum x =", result.x[0])
print("Minimum f(x) =", result.fun)
# ---------- 2B: harder landscape ----------
def g(x):   return x**4 - 3*x**2 + x + 5
def dg(x):  return 4*x**3 - 6*x + 1
def d2g(x): return 12*x**2 - 6


# TODO 2B: run the same three methods on g, from x0=0 AND from x0=2.
#   For Newton (which solves dg(x)=0), also check the sign of d2g at the answer:
#   d2g > 0 means a minimum, d2g < 0 means a maximum.
#   In your README note: do the methods agree? did Newton find a minimum or
#   another stationary point? how did the starting point change the result?
# ---------- 2B: harder landscape ----------

def g(x):
    return x**4 - 3*x**2 + x + 5
def dg(x):
    return 4*x**3 - 6*x + 1
def d2g(x):
    return 12*x**2 - 6

for x0 in [0.0, 2.0]:

    print(f"\n{'='*35}")
    print(f"2B - Starting point x0 = {x0}")
    print(f"{'='*35}")

    x = x0
    lr = 0.01
    tol = 1e-10

    for i in range(100000):
        x_new = x - lr * dg(x)

        if abs(x_new - x) < tol:
            x = x_new
            break

        x = x_new
    print("\nGradient Descent")
    print("Minimum x =", x)
    print("Minimum g(x) =", g(x))
    print("Iterations =", i + 1)
    
    x_newton = newton(
        dg,
        x0=x0,
        fprime=d2g
    )

    print("\nNewton's Method")
    print("Stationary point x =", x_newton)
    print("g(x) =", g(x_newton))
    print("Second derivative =", d2g(x_newton))

    if d2g(x_newton) > 0:
        print("Classification: local minimum")
    elif d2g(x_newton) < 0:
        print("Classification: local maximum")
    else:
        print("Classification: inconclusive")

    result = minimize(
        g,
        x0=[x0],
        method="SLSQP"
    )
    print("\nSLSQP")
    print("Minimum x =", result.x[0])
    print("Minimum g(x) =", result.fun)
    print("Success =", result.success)