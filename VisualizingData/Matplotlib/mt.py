import numpy as np 
import matplotlib.pyplot as plt
x = np.arange(0,100)
y = x*2
z = x**2
#Creating Plot
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.set_title("Y = 2x")
ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")
ax.plot(x,y)

#Creating Plot inside plot
fig2 = plt.figure()
ax2 = fig2.add_axes([0,0,1,1])
ax3 = fig2.add_axes([0.23,0.43,.19,.19])
ax3.set_xlim(20,40)
ax3.set_ylim(400,2000)

ax2.set_title("Y = X^2")
ax2.set_xlabel("xX axis")
ax2.set_ylabel("yY axis")


ax2.plot(x,z)
ax3.plot(x,z)

#Creating Subplot and designing, changing value of nrows and ncols results different kinds of subplots
fig,axes = plt.subplots(nrows=1, ncols=2, figsize=(8,2))
axes[0].plot(x,y,color="teal",lw=2, ls="-.")
axes[1].plot(x,z,color="blue",lw=2 , ls="--")