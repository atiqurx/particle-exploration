ime, indexes in mapped_indexes.items():
    for idx in indexes:

        particle_id = particle_entries[idx]
        particle = spheres[particle_id] 

        x = df.loc[idx, 'X']
        y = df.loc[idx, 'Y']
        z = df.loc[idx, 'Z']
        u = df.loc[idx, 'U']
        v = df.loc[idx, 'V']
        w = df.loc[idx, 'W']
        event_type = df.loc[