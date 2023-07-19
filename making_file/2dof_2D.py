import gjk
import math
import time
import numpy as np
from matplotlib import pyplot as plt, patches

# color

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE  = (  0,   0, 255)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)

# information of test environment

robot_link1 = 150
robot_link2 = 100
robot_thickness = 20
# obstacle : create a random circle
obstacle = ((np.random.randint(-100, 100), np.random.randint(-100, 100)), np.random.randint(10, 50))


# calculate collision 
def run():
    start = time.time()

    # 기존 txt 파일 내용 삭제

    file_path = "/home/jeongil/collision/making_file/result/2dof_2D_collision_data.txt"
    with open(file_path, "w") as file:          
        file.write(f"")
    file_path = "/home/jeongil/collision/making_file/result/2dof_2D_graph_data.txt"
    with open(file_path, "w") as file:          
        file.write(f"")
    file_path = "/home/jeongil/collision/making_file/result/2dof_2D_input.txt"
    with open(file_path, "w") as file:          
        file.write(f"")


    for q1_rad in range(0, 360):
        for q2_rad in range(0, 360):
            
            q1 = math.radians(q1_rad) 
            q2 = math.radians(q2_rad) 

            link_1 = (
                (robot_thickness*math.sin(q1),-robot_thickness*math.cos(q1)),
                (-robot_thickness*math.sin(q1),robot_thickness*math.cos(q1)),
                (-robot_thickness*math.sin(q1)+robot_link1*math.cos(q1),robot_thickness*math.cos(q1)+robot_link1*math.sin(q1)),
                (robot_thickness*math.sin(q1)+robot_link1*math.cos(q1),-robot_thickness*math.cos(q1)+robot_link1*math.sin(q1))
                )

            link_2 = (
                (robot_link1*math.cos(q1)+robot_thickness*math.sin(q2),robot_link1*math.sin(q1)-robot_thickness*math.cos(q2)),
                (robot_link1*math.cos(q1)-robot_thickness*math.sin(q2),robot_link1*math.sin(q1)+robot_thickness*math.cos(q2)),
                (robot_link1*math.cos(q1)-robot_thickness*math.sin(q2)+robot_link2*math.cos(q2),robot_link1*math.sin(q1)+robot_thickness*math.cos(q2)+robot_link2*math.sin(q2)),
                (robot_link1*math.cos(q1)+robot_thickness*math.sin(q2)+robot_link2*math.cos(q2),robot_link1*math.sin(q1)-robot_thickness*math.cos(q2)+robot_link2*math.sin(q2))
                )
            
            # collision check

            collide_1 = gjk.collidePolyCircle(link_1, obstacle)
            polygon(link_1)
            circle(obstacle)
            collide_2 = gjk.collidePolyCircle(link_2, obstacle)
            polygon(link_2)
            circle(obstacle)

            # save result in txt file and  recalculate

            file_path = "/home/jeongil/collision/making_file/result/2dof_2D_collision_data.txt"
            if (collide_1 or collide_2):
                with open(file_path, "a") as file:
                    file.write(f"collision  q1 : {q1_rad}   q2 : {q2_rad}\n")
                
            file_path = "/home/jeongil/collision/making_file/result/2dof_2D_graph_data.txt"
            with open(file_path, "a") as file:          
                file.write(f"{q1_rad}, {q2_rad}, {'0' if (collide_1 or collide_2) else '1'}\n")

    file_path = "/home/jeongil/collision/making_file/result/2dof_2D_input.txt"
    with open(file_path, "a") as file:          
        file.write(f"robot_link1 : {robot_link1}\nrobot_link2 : {robot_link2}\nrobot_thickness : {robot_thickness}\nobstacle : {obstacle}")

    end = time.time()

    #check time and print, save in txt file
    print(f"{end - start :.5f} sec")

    file_path = "/home/jeongil/collision/making_file/result/2dof_2D_collision_data.txt"
    with open(file_path, "a") as file:
        file.write(f"\ncalculate time is : {end - start :.5f} sec")

# make a C_space graph and save
def C_space():

    file_path = "/home/jeongil/collision/making_file/result/2dof_2D_graph_data.txt"

    x_values = []
    y_values = []
    z_values = []

    with open(file_path, "r") as file:
        for line in file:
            data = line.strip().split(",")
            x = float(data[0])
            y = float(data[1])
            z = float(data[2])
            x_values.append(x)
            y_values.append(y)
            z_values.append(z)

    x_unique = np.sort(np.unique(x_values))
    y_unique = np.sort(np.unique(y_values))
    z_array = np.zeros((len(y_unique), len(x_unique)))

    for x, y, z in zip(x_values, y_values, z_values):
        x_index = np.where(x_unique == x)[0][0]
        y_index = np.where(y_unique == y)[0][0]
        z_array[y_index, x_index] = z

    plt.imshow(z_array, cmap='Pastel1', origin='upper', extent=[x_unique[0], x_unique[-1], y_unique[0], y_unique[-1]])

    plt.xlabel("joint 1 angle(q1, degrees)")
    plt.ylabel("joint 2 angle(q2, degrees)")
    plt.title("C-space")

    plt.savefig('/home/jeongil/collision/making_file/result/2dof_2D_C-space.png')
    plt.show()


def pairs(points):
    for i, j in enumerate(range(-1, len(points) - 1)):
        yield (points[i], points[j])

def circles(cs, color=BLACK, camera=(0, 0)):
    for c in cs:
        circle(c, color, camera)

def circle(c, color=BLACK, camera=(0, 0)):
    ()

def polygon(points, color=BLACK, camera=(0, 0)):
    for a, b in pairs(points):
        line(a, b, color, camera)

def line(start, end, color=BLACK, camera=(0, 0)):
    ()

def add(p1, p2):
    return p1[0] + p2[0], p1[1] + p2[1]




# run code 
if __name__ == '__main__':
    run()
    C_space()

