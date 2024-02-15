import pandas as pd
from vpython import canvas, sphere, rate, vector, color, curve, box

# importing dataset 
df = pd.read_csv("sample_0_ptrac.csv")
total_iterations = len(df)
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


class Particle:
    def __init__(self, id, type, x, y, z, u, v, w, time, sphere):
        self.id = id
        self.type = type
        self.x = x
        self.y = y
        self.z = z
        self.u = u
        self.v = v 
        self.w = w
        self.time = time
        self.sphere = None

particles = {}
spheres = {}
particle_counter = 0  
current_trail = curve(color=color.green, radius=0.3)

# setting paticle id
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

    # Handle different event types
    if event_type == 1000 or event_type == 2000:  # Source & new particle spawn
        particle_counter += 1  
        particle_id = particle_counter 
        spheres[particle_id] = sphere(visible = False, radius=1, color=color.yellow if event_type == 1000 else color.red)

    particles[index] = Particle(particle_id, event_type, x, y, z, u, v, w, time, spheres[particle_id])
    

# Group the DataFrame by the "Time" column
grouped_df = df.groupby('Time')
sorted_groups = {time: group.sort_values(by='Time') for time, group in grouped_df}
mapped_indexes = {time: group.index.tolist() for time, group in sorted_groups.items()} # Map indexes to sorted time values


for time, indexes in mapped_indexes.items():
    for idx in indexes:

        particle = particles[idx] 

        x = particle.x
        y = particle.y
        z = particle.z
        u = particle.u
        v = particle.v
        w = particle.w
        event_type = particle.type
        
        # Update position based on directional cosines
        scale = 15
        pos = vector(x, y, z) + vector(u, v, w) * scale

        particle.sphere.visible = True
        

        if event_type == 5000:  # Termination
            # particle.sphere.visible = False  
            current_trail.clear()

        current_trail.append(pos)

        rate(10)


        

