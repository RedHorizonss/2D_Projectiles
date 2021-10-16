#Main projectile python package

def update_state(t, x, v, a, dt=0.1):
    #Update each parameter for the next time step which is dt
        
    distance_moved = v*dt + (1/2)*a*(dt**2) # Calculates distance moved through SUVAT
    x += distance_moved
    #Calulates new velocity and time due to the movement
    v += a*dt
    t += dt
    
    return t, x, v
     
    
