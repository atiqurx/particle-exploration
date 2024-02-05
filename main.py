import pandas as pd
from vpython import canvas, sphere, rate, vector, color, curve, box

# importing dataset 
df = pd.read_csv("sample_0_ptrac.csv")

scene = canvas(title="Particle Path Visualization", width=1000, height=600)
#scene.autoscale = False

# 3D Box
side = 70.0
thk = 0.5
s2 = 2*side - thk
s3 = 2*side + thk

wallR = box (pos=vector( side, 0, 0), size=vector(thk, s2, s3),  color = color.red)
wallL = box (pos=vector(-side, 0, 0), size=vector(thk, s2, s3),  color = color.red)
wallB = box (pos=vector(0, -side, 0), size=vector(s3, thk, s3),  color = color.blue)
wallT = box (pos=vector(0,  side, 0), size=vector(s3, thk, s3),  color = color.blue)
wallBK = box(pos=vector(0, 0, -side), size=vector(s2, s2, thk), color = color.gray(0.7))

# particle and trail
particle = sphere(radius = 1, color=color.yellow)
particle.mass = 1.0
trail = curve(color=color.green, radius=0.3)

# tracking the visited path
visited_positions = set()

for index, row in df.iterrows():
    x = row['X']
    y = row['Y']
    z = row['Z']

    current_position = vector(x, y, z)
    particle.pos = current_position

    trail.append(particle.pos) 

    rate(10)

print("End")