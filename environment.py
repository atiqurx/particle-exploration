from vpython import canvas, box, vector, color, rate, arrow

# Define the extracted values from the input file (seed_0.inp)

surface_parameters = {
    # surface volume
    1: 100,  # px 100
    2: -100,  # px -100
    3: 100,  # py 100
    4: -100,  # py -100
    5: 37,  # pz 37
    6: 87,  # pz 87
    # detectors
    103: 21.05, # Det 1 outer plane active region
    104: 8.35, # Det 1 inner plane active region
    105: 6.35, # Det 2 plane on Det 1 side active region
    106: -6.35,  # Det 2 plane on Det 3 side active region
    107: -8.35,  # Det 3 inside plane active region
    108: -21.05,  # Det 3 outer plane active region
    109: 6.35, # Det 1,2,3 back plane of active region
    113: -6.35, # Det 1,2,3 front plane of active region
    116: 7.62, # Det 1,2,3 top plane of active region
    119: -7.62, # Det 1,2,3 bottom plane of active region
    # sheilding
    65: 5, # bottom surface of shielding. from MINS field scale scan, bottom is 5cm below neutron target
    66: -15, # top surface of shielding 

    611: 40, # Detector side surface of Pb   
    612: 35, # Generator side surface of Pb     
    613: 30.5, # Side surface of Pb      
    614: -30.5, # Side surface of Pb 
    621: 30, # Generator side surface of Front Fe1      
    622: 27.5, # Side surface of Front Fe1, Fe2, BA1    
    623: -27.5, # Side surface of Front Fe1, Fe2, BA1 
    631: 20, # Generator side surface of BA1             
    641: 15, # Generator side surface of Front Fe2  / Detector side surface Side Fe_BA

}
soil_dimensions = {
    'x': surface_parameters[1] - surface_parameters[2],
    'y': surface_parameters[3] - surface_parameters[4],
    'z': surface_parameters[5] - surface_parameters[6]
}

# Create a canvas
scene = canvas(width=800, height=600)
scene.background = color.white

# Create a box to represent the soil volume
soil_volume = box(pos=vector(0, 0, 0),
                   size=vector(soil_dimensions['x'], soil_dimensions['y'], soil_dimensions['z']),
                   color=color.blue)


# DETECTORS
detector_1_dimensions = {
    'x': surface_parameters[109] - surface_parameters[113],
    'y': surface_parameters[103] - surface_parameters[104],
    'z': surface_parameters[116] - surface_parameters[119]
}

detector_1 = box(pos=vector(65 ,  20, 60), # need to check if the position is correct
                   size=vector(detector_1_dimensions['x'], detector_1_dimensions['y'], detector_1_dimensions['z']),
                   color=color.cyan)

detector_2_dimensions = {
    'x': surface_parameters[109] - surface_parameters[113],
    'y': surface_parameters[105] - surface_parameters[106],
    'z': surface_parameters[116] - surface_parameters[119]
}

detector_2 = box(pos=vector(65 , 0 , 60), # need to check if the position is correct
                   size=vector(detector_2_dimensions['x'], detector_2_dimensions['y'], detector_2_dimensions['z']),
                   color=color.cyan)

detector_3_dimensions = {
    'x': surface_parameters[109] - surface_parameters[113],
    'y': surface_parameters[107] - surface_parameters[108],
    'z': surface_parameters[116] - surface_parameters[119]
}

detector_3 = box(pos=vector(65 , -20 , 60), # need to check if the position is correct
                   size=vector(detector_3_dimensions['x'], detector_3_dimensions['y'], detector_3_dimensions['z']),
                   color=color.cyan)

# SHIELDING
pb_dimensions = {
    'x': surface_parameters[611] - surface_parameters[612],
    'y': surface_parameters[613] - surface_parameters[614],
    'z': surface_parameters[65] - surface_parameters[66]
}

pb = box(pos=vector(40 , 0 , 60), # need to check if the position is correct
                   size=vector(pb_dimensions['x'], pb_dimensions['y'], pb_dimensions['z']),
                   color=color.gray(0.5))

fe1_dimensions = {
    'x': surface_parameters[612] - surface_parameters[621],
    'y': surface_parameters[622] - surface_parameters[623],
    'z': surface_parameters[65] - surface_parameters[66]
}

fe1 = box(pos=vector(35, 0 , 60), # need to check if the position is correct
                   size=vector(fe1_dimensions['x'], fe1_dimensions['y'], fe1_dimensions['z']),
                   color=color.red)

ba1_dimensions = {
    'x': surface_parameters[621] - surface_parameters[631],
    'y': surface_parameters[622] - surface_parameters[623],
    'z': surface_parameters[65] - surface_parameters[66]
}

ba1 = box(pos=vector(27.5, 0 , 60), # need to check if the position is correct
                   size=vector(ba1_dimensions['x'], ba1_dimensions['y'], ba1_dimensions['z']),
                   color=color.green)

fe2_dimensions = {
    'x': surface_parameters[631] - surface_parameters[641],
    'y': surface_parameters[622] - surface_parameters[623],
    'z': surface_parameters[65] - surface_parameters[66]
}

fe2 = box(pos=vector(20, 0 , 60), # need to check if the position is correct
                   size=vector(fe2_dimensions['x'], fe2_dimensions['y'], fe2_dimensions['z']),
                   color=color.red)

# Create x, y, and z axes
x_axis = arrow(pos=vector(0, 0, 0), axis=vector(500, 0, 0), shaftwidth=1, color=color.red)
y_axis = arrow(pos=vector(0, 0, 0), axis=vector(0, 500, 0), shaftwidth=1, color=color.green)
z_axis = arrow(pos=vector(0, 0, 0), axis=vector(0, 0, 500), shaftwidth=1, color=color.blue)

while True:
    rate(30)
