import pandas as pd
from vpython import canvas, sphere, rate, vector, color, curve, box, text

# importing dataset 
df = pd.read_csv("sample_0_ptrac.csv")

# canvas
scene = canvas(title="Particle Path Visualization", width=1000, height=600)

# 3D Box
side =80.0
thk = 0.5
s2 = 2*side - thk
s3 = 2*side + thk

wallR = box(pos=vector(side, 0, 0), size=vector(thk, s2, s3), color=color.red)
wallL = box(pos=vector(-side, 0, 0), size=vector(thk, s2, s3), color=color.red)
wallB = box(pos=vector(0, -side, 0), size=vector(s3, thk, s3), color=color.blue)
wallT = box(pos=vector(0, side, 0), size=vector(s3, thk, s3), color=color.blue)
wallBK = box(pos=vector(0, 0, -side), size=vector(s2, s2, thk), color=color.gray(0.7))

# Initialize variables for particle tracking
particle_counter = 0  
particle_dict = {}  # Dictionary to store particles with their IDs
particle_records = []  # List to store particle records


# Initialize the particle trail
current_trail = curve(color=color.green, radius=0.3)

# Iterate over the dataset
for index, row in df.iterrows():
    # Extract data from the row
    x = row['X']
    y = row['Y']
    z = row['Z']
    u = row['U']  # cosine of x-axis direction
    v = row['V']  # cosine of y-axis direction
    w = row['W']  # cosine of z-axis direction
    time = row['Time']  
    event_type = row['Type']  # get the event type of particle

    # Update position based on directional cosines
    scale = 15

    # Handle different event types
    if event_type == 1000 or event_type == 2000:  # Source & new particle spawn
        particle_counter += 1  
        particle_id = particle_counter  
        particle_dict[particle_id] = sphere(pos=vector(x, y, z), radius=1, color=color.yellow if event_type == 1000 else color.red)  
        current_trail = curve(color=color.green, radius=0.3)  
        
    elif event_type == 3000:  # Surface crossed
        pass

    elif event_type == 4000:  # Collision
        pass 

    elif event_type == 5000:  # Termination
        for particle_id, particle in particle_dict.items():
            if particle is not None:
                particle.visible = False  
        # particle_dict = {}  # Clear the particle dictionary
        current_trail.clear()  # Clear the trail
        
    particle_records.append({'ID': particle_id, 'Type': event_type, 'X': x, 'Y': y, 'Z': z, 'Time': time})  

    # Update particle position
    if particle_id in particle_dict:
        particle = particle_dict[particle_id]
        particle.pos = vector(x, y, z) + vector(u, v, w) * scale
        current_trail.append(particle.pos)

        # print(particle_dict[particle_id])
        print(particle_records[-1]["Time"])
    
    rate(10)

print("End")

