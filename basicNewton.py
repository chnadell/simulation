import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy.integrate as integrate

g0 = 9.81 # m/s^2
t0 = 10 # s
y0 = 0 # m
v0 = 0 # m/s

def dydt_freefall(t, y):
    return -g0 * t

# define simulation range
teval= np.arange(start=0, stop=t0, step=1)

# solve system
sol = integrate.solve_ivp(dydt_freefall, [0, t0], [y0], t_eval=teval)

# plot result
plt.plot(sol.t, sol.y[0], marker='.')
plt.show()