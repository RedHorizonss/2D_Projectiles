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

def calculate_acceleration_y(v, k, mass, gravity=-9.81):
    #Calculates acceleration at each time step (based on the velocity at that time)
    
    force_gravity = mass*gravity #F = ma calculates the force of gravity acting on y currently
    force_air = -sign(v)*k*v**2 #F=-kv^2
    total_force = force_gravity + force_air
    a = total_force/mass #a = F/m calculates acceleration with total force (gravity and air resistance)
    
    return a

def calculate_acceleration_x(v, k, mass):
    force = -sign(v)*k*v**2 #F=-kv^2
    a = force/mass #a = F/m calculates acceleration with force
    
    return a

def flying_mass(initial_vx, initial_vy, mass, k=0.035):
    #Models a flying mass from a set co-ordinate
    
    #Initialising values for x and y (the velocity is given to us above)
    gravity = -9.81 # m/s2
    x = 0
    y = 0
    vy = initial_vy
    vx = initial_vx
    t = 0.0
    dt = 0.1

    # Create empty lists which we will update
    y_coord = []
    x_coord = []
    x_velocity = []
    y_velocity = []
    time = []

    # Keep looping while the object is still falling
    while y_coord[-1] > 0:
        # Evaluate the state of the system - start by calculating the total force on the object
        y_accel = calculate_acceleration_y(vy, k, mass, gravity)
        x_accel = calculate_acceleration_x(vx, k, mass)

        # Append values to list and then update
        x_coord.append(x)
        y_coord.append(y)
        
        x_velocity.append(vx)
        y_velocity.append(vy)
        
        time.append(t)

        # Update the state for time, height and velocity
        t, x_dist, xv = update_state(t, x, vx, x_accel, dt)
        t, y_dist, yv = update_state(t, y, vy, y_accel, dt)
    
    return t, x, y, vx, vy
    