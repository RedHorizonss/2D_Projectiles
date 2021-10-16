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
    
    #Initialising values for x and y (the initial velocity is given to us above)
    gravity = -9.81
    #distance for x and y
    x = 0
    y = 0
    #velocity of x and y
    vy = initial_vy
    vx = initial_vx
    #initial time and time step thats being used
    t = 0.0
    dt = 0.1

    #Empty lists which are being updated through the code
    y_coord = []
    x_coord = []
    x_velocity = []
    y_velocity = []
    time = []

    #Keep looping until y hits the floor (system is not set up for further)
    while y_coord[-1] > 0:
        
        #Set up of acceleration with initial numbers
        y_accel = calculate_acceleration_y(vy, k, mass, gravity)
        x_accel = calculate_acceleration_x(vx, k, mass)

        #Appending values to list and then updating
        
        #Distance
        x_coord.append(x)
        y_coord.append(y)
        #Velocity
        x_velocity.append(vx)
        y_velocity.append(vy)
        #Time
        time.append(t)

        # Update the state for time, distance and velocity for x and y
        t, x_dist, xv = update_state(t, x, vx, x_accel, dt)
        t, y_dist, yv = update_state(t, y, vy, y_accel, dt)
    
    return t, x, y, vx, vy
    