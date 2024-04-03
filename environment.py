from vpython import canvas, box, vector, color, rate, arrow

# Define the extracted values from the input file (seed_0.inp)
cell_number = 20
material_number = 1
surface_numbers = [1, 2, 3, 4, 5, 6]
surface_parameters = {
    1: 100,  # px 100
    2: -100,  # px -100
    3: 100,  # py 100
    4: -100,  # py -100
    5: 37,  # pz 37
    6: 87  # pz 87
}
soil_dimensions = {
    'x': surface_parameters[1] - surface_parameters[2],
    'y': surface_parameters[3] - surface_parameters[4],
    'z': surface_parameters[5] - surface_parameters[6]
}

# Create a canvas
scene = canvas(width=800, height=600)
scene.background = color.black

# Create a box to represent the soil volume
soil_volume = box(pos=vector(0, 0, 0),
                   size=vector(soil_dimensions['x'], soil_dimensions['y'], soil_dimensions['z']),
                   color=color.green)

# Create x, y, and z axes
x_axis = arrow(pos=vector(0, 0, 0), axis=vector(200, 0, 0), shaftwidth=1, color=color.red)
y_axis = arrow(pos=vector(0, 0, 0), axis=vector(0, 200, 0), shaftwidth=1, color=color.green)
z_axis = arrow(pos=vector(0, 0, 0), axis=vector(0, 0, 200), shaftwidth=1, color=color.blue)

while True:
    rate(30)
