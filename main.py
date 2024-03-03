import pandas as pd
from vpython import canvas, sphere, rate, vector, color, curve, box, label
import time

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


particle_entries = {} # ids are mapped to indexes
spheres = {} # spheres are mapped to particle ids 
particle_counter = 0  # used for assign particle id
scale = 1.2

# setting paticle id
for index, row in df.iterrows():
    x = row['X']
    y = row['Y']
    z = row['Z']
    event_type = row['Type']  

    # set a particle id for each new particle
    if event_type == 1000 or event_type == 2000: 
        particle_counter += 1  
        particle_id = particle_counter 
        spheres[particle_id] = sphere(visible = False, pos = vector(x,y,z) * scale, radius=1, make_trail=True, trail_radius=0.2, trail_color=color.green, color=color.yellow if event_type == 1000 else color.red)

    particle_entries[index] = particle_id

# Label for coordinates
info_label = label(pos=vector(120, 120, 0), text='', height=16, border=6, font='sans')

# Group the DataFrame by the "Time" column
grouped_df = df.groupby('Time')
sorted_groups = {time: group.sort_values(by='Time') for time, group in grouped_df}
mapped_indexes = {time: group.index.tolist() for time, group in sorted_groups.items()} 

time.sleep(2)

for time, indexes in mapped_indexes.items():
    for idx in indexes:

        particle_id = particle_entries[idx]
        particle = spheres[particle_id] 

        x = df.loc[idx, 'X']
        y = df.loc[idx, 'Y']
        z = df.loc[idx, 'Z']
        u = df.loc[idx, 'U']
        v = df.loc[idx, 'V']
        w = df.loc[idx, 'W']
        event_type = df.loc[idx, 'Type']
        
        # scale the coordiantes
        pos = vector(x, y, z)  * scale

        particle.visible = True

        particle.pos = pos

        if event_type == 5000:  # Termination
            particle.visible = False 
            particle.clear_trail()
        
        # Update label
        info_label.text = f'Index: {idx}\nParticle ID: {particle_id}\nEvent Type: {event_type}\nCoordinates: ({x:.2f}, {y:.2f}, {z:.2f})'

    rate(10)
