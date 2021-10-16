#Package to plot python
import matplotlib.pyplot as plt

def plot_xy(x, y):

    fig, ax1 = plt.subplots()
    
    ax1.plot(x, y)
    ax1.set_ylabel("y position (m)")
    ax1.set_xlabel("x position (m)")
    plt.show()
    
