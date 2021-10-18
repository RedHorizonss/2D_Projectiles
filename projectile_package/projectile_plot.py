#Package to plot python
import matplotlib.pyplot as plt

def plot_xy(x, y, vx, vy, t):

    fig, (ax1, ax2, ax3) = plt.subplots(3,1, figsize = (10,10))
    
    #Plots The trajectory 
    ax1.plot(x, y)
    ax1.set_title("Trajectory of projectile")
    ax1.set_ylabel("y position (m)")
    ax1.set_xlabel("x position (m)")
    
    #Plots The change in velocity for x and y
    ax2.plot(t, vx)
    ax2.set_title("Change in Velocity for x")
    ax2.set_ylabel("Velocity of x (m/s)")
    ax2.set_xlabel("Time (s)")
    
    ax3.plot(t, vy)
    ax3.set_title("Change in Velocity for y")
    ax3.set_ylabel("Velocity of y (m/s)")
    ax3.set_xlabel("Time (s)")
    plt.show()

    
