# PA3 NEWTON'S METHOD

import numpy as np

# PART 1: numpy Familiarization

# np.poly1d()
# np.polyder()
# np.polyval()
# roots

# f(x) = 2x^3 + 3x^2 + 1
p1 = np.poly1d([2,3,0,1]) 
print('f(x):')
print(p1)

# evaluate function at x=2
e1 = np.polyval(p1,2)
print(f'f(2): {e1}')
print()

# g(x) = x^2 + 1
p2 = np.poly1d([1, 0, 1])
print('g(x):')
print(p2)
print()

# evaluate derivative at x=1
d2 = np.polyder(p2)
print(f"g'(x)': {d2}")
print()
e2 = np.polyval(d2,1)
print(f"g'(1):{e2}")
#r = np.poly1d.roots
#print(r)
#%%
# PART 2: Newton's Method

import numpy as np

# empty list for user input
#f = [1,-4,0,1]
f = []

for i in range(4): # limit on size of polynomial to get root
    x = float(input("Input a number: "))
    f.append(x) # numbers added to list: 1, -4, 0, 1

# create f(x) with input numbers
poly = np.poly1d(f)

x1 = float(input("Input a x1: ")) # have to evaluate with 0.5

def eval_poly(poly,x):
    return np.polyval(poly,x)

#print(eval_poly(poly,1))

def eval_der(poly,x):
    der = np.polyder(poly)
    return np.polyval(der,x)

#print(eval_der(poly,1))


def Newtons(poly, xn, iterat=1):
    f_xn = eval_poly(poly,xn)
    f_xp = eval_der(poly,xn)

    xn_p = xn - f_xn/f_xp
    
    print(f'x_{iterat+1} = {xn_p}')
    
    if abs(xn_p - xn) < 0.001:
    #if abs(xn_p - xn) < 0.001:
        return f_xp
    else:
        return Newtons(poly, xn_p, iterat+1)
        print(xn_p)
        
    
Newtons(poly, x1)

print(np.roots(f))
print(np.roots(poly))