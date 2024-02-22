teps = 10
        step_vector = (pos - particle.pos) / steps
        for _ in range(steps):
            particle.pos += step_vector
            rate(30)