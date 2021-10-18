#Package to plot python
import matplotlib.pyplot as plt

def plot_xy(x, y, vx, vy):

    fig, axs = plt.subplots(1, 2)
    
    #Plots 
    ax1.plot(x, y, title = "Trajectory of projectile")
    ax1.set_ylabel("y position (m)")
    ax1.set_xlabel("x position (m)")
    plt.show()
    
    ax2.plot(t, vx, title = "Change in Velocity for x")
    ax2.set_ylabel("Velocity of x (m/s)")
    ax2.set_xlabel("Time (s)")
    plt.show()
    
    ax3.plot(t, vy, title = "Chnage in Velocity for y")
    ax3.set_ylabel("Velocity of y (m/s)")
    ax3.set_xlabel("Time (s)")
    plt.show()
    
    
