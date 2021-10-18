#Package to plot python
import matplotlib.pyplot as plt

def plot_xy(x, y):

    fig, axs = plt.subplots(1, 2)
    
    #Plots 
    ax1.plot(x, y, title = "Trajectory of projectile")
    ax1.set_ylabel("y position (m)")
    ax1.set_xlabel("x position (m)")
    plt.show()
    
    ax2.plot(vx,t)
    ax2.set_ylabel("Velocity of x (m/s)")
    ax2.set_xlabel("Time (s)")
    plt.show()
    
    
