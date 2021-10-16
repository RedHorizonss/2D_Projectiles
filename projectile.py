#Main projectile python package

def update_state(t, x, v, a, dt=0.1):
    #Update each parameter for the next time step which is dt
        
    distance_moved = v*dt + (1/2)*a*(dt**2) # Calculates distance moved through SUVAT
    x += distance_moved
    #Calulates new velocity and time due to the movement
    v += a*dt
    t += dt
    
    return t, x, v

from numpy import sign

def calculate_acceleration_y(v, k=0.0, mass, gravity=-9.81):
    #Calculates acceleration at each time step (based on the velocity at that time)
    
    force_gravity = mass*gravity #F = ma calculates the force of gravity acting on y currently
    force_air = -sign(v)*k*v**2 #F=-kv^2
    total_force = force_gravity + force_air
    a = total_force/mass #a = F/m calculates acceleration with total force (gravity and air resistance)
    
    return a

def calculate_acceleration_x(v, k=0.0, mass):
    force = -sign(v)*k*v**2 #F=-kv^2
    a = force/mass #a = F/m calculates acceleration with force
    
