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

current_particle = None
current_trail = curve(color=color.green, radius=0.3)

# tracking the visited path
visited_positions = set()

for index, row in df.iterrows():
    x = row['X']
    y = row['Y']
    z = row['Z']
    u = row['U']  # cosine of x-axis direction
    v = row['V']  # cosine of y-axis direction
    w = row['W']  # cosine of z-axis direction
    time = row['Time']  # Time for shaking at the position
    event_type = row['Type'] # get the event type of particle

    # Update position based on directional cosines
    scale = 15

    # Handle different event types
    if event_type == 1000:  # Source (new particle spawn)
        current_particle = sphere(pos=vector(x, y, z), radius=1, color=color.yellow)

    elif event_type == 2000:  # New particle created
        current_particle = sphere(pos=vector(x, y, z), radius=1, color=color.red)

    elif event_type == 3000:  # Surface crossed
        pass

    elif event_type == 4000:  # Collision
        pass 

    elif event_type == 5000:  # Termination
        if current_particle is not None:
            current_particle.visible = False
            current_particle = None
            current_trail.clear()

    # Update particle position
    if current_particle is not None and event_type != 5000:
        current_particle.pos = vector(x, y, z) + vector(u, v, w) * scale
        current_trail.append(current_particle.pos)
    
    
    rate(10)

print("End")

