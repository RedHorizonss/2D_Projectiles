#Main projectile python package
from numpy import sign

def update_state(t, x, v, a, dt):
    #Update each parameter for the next time step which is dt
    
    #Calculates distance moved through SUVAT
    distance_moved = v*dt + (1/2)*a*(dt**2)
    x += distance_moved
    
    #Calulates new velocity and time due to the movement
    v += a*dt
    t += dt
    return t, x, v

def calculate_acceleration_y(v, k, mass, gravity):
    #Calculates acceleration at each time step (based on the velocity at that time)
    
    #F = ma calculates the force of gravity acting on y currently
    force_gravity = mass*gravity
    
    #F=-kv^2 calculates the air resistance
    force_air = -sign(v)*k*v**2
    
    #a = F/m calculates acceleration with total force (gravity and air resistance)
    total_force = force_gravity + force_air
    a = total_force/mass
    
    return a

def calculate_acceleration_x(v, k, mass):
    #F=-kv^2 calculates the air resistance
    force = -sign(v)*k*v**2
    
    #a = F/m calculates acceleration with force
    a = force/mass
    
    return a

def flying_mass(initial_vx, initial_vy, mass, k=0.035):
    #Models a flying mass from a set co-ordinate
    
    #Initialising values for x and y (the initial velocity is given to us above)
    gravity = -9.81
    
    #Distance for x and y
    x = 0
    y = 0
    
    #Velocity of x and y
    vy = initial_vy
    vx = initial_vx
    
    #Initializes time and time step (dt) thats being used
    t = 0.0
    dt = 0.1

    #Empty lists which are being updated through the code used to plot the changes
    y_coord = []
    x_coord = []
    x_velocity = []
    y_velocity = []
    time = []

    #Keep looping until y hits the floor (system is not set up for further)
    while y >= 0:
        
        #Set up of acceleration with initial numbers
        y_accel = calculate_acceleration_y(vy, k, mass, gravity)
        x_accel = calculate_acceleration_x(vx, k, mass)
        
        #Appending values to list and then updating
        x_coord.append(x)
        y_coord.append(y)
        x_velocity.append(vx)
        y_velocity.append(vy)
        time.append(t)

        # Update the state for time, distance and velocity for x and y
        t, x, vx = update_state(t, x, vx, x_accel, dt)
        t, y, vy = update_state(t, y, vy, y_accel, dt)
    
    return time, x_coord, y_coord, x_velocity, y_velocity

t, x, y, vx, vy = flying_mass(10., 10., mass=1., k=0.035)