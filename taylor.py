import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import math

from sympy import *

x = symbols('x')

# User Input
func_input = input('f(x) = ')
point = input('Point of Approximation: x = ')
degree = input('Degree: ')

# Converts user input into appropriate types my code can work with
function = sympify(func_input)
a = float(point)
degree = int(degree)

taylor_expansion = float()
taylor_terms = list()
num_terms = 0

# Taylor Expansion Calculation
for i in range(0,degree+1):
    func_deriv = diff(function,x,i)
    term = ((func_deriv.subs(x,a))/(math.factorial(i)))*((x-a)**i)
    taylor_expansion += term
    if term != 0:
        taylor_terms.append(term)
        num_terms += 1
    
print('P(x) = ' + str(nsimplify(taylor_expansion)))

# Making and Displaying Comparison Plot
sum_ = taylor_terms[0]
term_loc = 1

def f(x):
    return function

def p_part(x):
    return sympify(sum_)

def p(x):
    return taylor_expansion

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
x_low = a-10
x_high = a+10
dx = 0.01
size = int((x_high-x_low)/dx)
x_axis = np.arange(x_low, x_high, dx)

f_lam = lambdify(x,f(x))
line2, = ax.plot(x_axis, np.full(size,f_lam(a)), linewidth=2, color='blue')

def init():
    f_lam = lambdify(x,f(x))
    line1, = ax.plot(x_axis, f_lam(x_axis), linewidth=2, color='red')   
    return line1,

def update(i):
    global sum_
    global term_loc
    
    if i == num_terms - 1:
        # resets the animation
        term_loc = 0
        sum_ = taylor_terms[0]  
        f_lam = lambdify(x,f(x))
        line2.set_ydata(np.full(size,f_lam(a)))
        term_loc += 1
        return line2,
        
    sum_ += taylor_terms[term_loc]
    term_loc += 1
    p_lam = lambdify(x,p_part(x))
    line2.set_ydata(p_lam(x_axis))     
        
    return line2,


anime = anim.FuncAnimation(fig, update, num_terms, init_func=init, repeat=True, blit=False, interval=1000)
plt.show()