import numpy as np



def load_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            angle1, angle2, collision = line.strip().split(',')
            data.append([float(angle1), float(angle2), int(collision)])
    return np.array(data)


