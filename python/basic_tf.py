import numpy as np
import matplotlib.pyplot as plt
import control

# Create transfer function
s = control.tf('s')
tf1 = 1/(1+s)

# Simulate step response
T = np.linspace(0,10,100)
X0 = 0
T, yout = control.step_response(tf1, T, X0)

# Plot
fig,ax = plt.subplots(1,1,sharex=True)
ax.plot(T,yout)
ax.grid()

plt.show()