import sys
import gjk
import math
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import time

# color

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE  = (  0,   0, 255)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)

# information of robot

l1 = 200
l2 = 200
l3 = 200
l4 = 200
l5 = 200
l6 = 200
tk = 20

def run():
    start = time.time()

    for q1_rad in range(0, 360, 30):
        for q2_rad in range(0, 360, 30):
            for q3_rad in range(0, 360, 30):
                for q4_rad in range(0, 360, 30):
                    for q5_rad in range(0, 360, 30):     
                        for q6_rad in range(0, 360, 30):

            
                            q1 = math.radians(q1_rad) 
                            q2 = math.radians(q2_rad)
                            q3 = math.radians(q3_rad)  
                            q4 = math.radians(q4_rad)  
                            q5 = math.radians(q5_rad)  
                            q6 = math.radians(q6_rad)  

                            link_1 = (
                                (tk*math.sin(q1),-tk*math.cos(q1)),
                                (-tk*math.sin(q1),tk*math.cos(q1)),
                                (l1*math.cos(q1)-tk*math.sin(q1),l1*math.sin(q1)+tk*math.cos(q1)),
                                (l1*math.cos(q1)+tk*math.sin(q1),l1*math.sin(q1)-tk*math.cos(q1))
                                )

                            link_2 = (
                                (l1*math.cos(q1)+tk*math.sin(q2),l1*math.sin(q1)-tk*math.cos(q2)),
                                (l1*math.cos(q1)-tk*math.sin(q2),l1*math.sin(q1)+tk*math.cos(q2)),
                                (l1*math.cos(q1)+l2*math.cos(q2)-tk*math.sin(q2),l1*math.sin(q1)+l2*math.sin(q2)+tk*math.cos(q2)),
                                (l1*math.cos(q1)+l2*math.cos(q2)+tk*math.sin(q2),l1*math.sin(q1)+l2*math.sin(q2)-tk*math.cos(q2))
                                )
                            link_3 = (
                                (l1*math.cos(q1)+l2*math.cos(q2)+tk*math.sin(q3),l1*math.sin(q1)+l2*math.sin(q2)-tk*math.cos(q3)),
                                (l1*math.cos(q1)+l2*math.cos(q2)-tk*math.sin(q3),l1*math.sin(q1)+l2*math.sin(q2)+tk*math.cos(q3)),
                                (l1*math.cos(q1)+l2*math.cos(q2)+l3*math.cos(q3)-tk*math.sin(q3),l1*math.sin(q1)+l2*math.sin(q2)+l3*math.sin(q3)+tk*math.cos(q3)),
                                (l1*math.cos(q1)+l2*math.cos(q2)+l3*math.cos(q3)+tk*math.sin(q3),l1*math.sin(q1)+l2*math.sin(q2)+l3*math.sin(q3)-tk*math.cos(q3))
                                )   
                            link_4 = (
                                (l1*math.cos(q1)+l2*math.cos(q2)+l3*math.cos(q3)+tk*math.sin(q4),l1*math.sin(q1)+l2*math.sin(q2)+l3*math.sin(q3)-tk*math.cos(q4)),
                                (l1*math.cos(q1)+l2*math.cos(q2)+l3*math.cos(q3)-tk*math.sin(q4),l1*math.sin(q1)+l2*math.sin(q2)+l3*math.sin(q3)+tk*math.cos(q4)),
                                (l1*math.cos(q1)+l2*math.cos(q2)+l3*math.cos(q3)+l4*math.cos(q4)-tk*math.sin(q4),l1*math.sin(q1)+l2*math.sin(q2)+l3*math.sin(q3)+l4*math.sin(q4)+tk*math.cos(q4)),
                                (l1*math.cos(q1)+l2*math.cos(q2)+l3*math.cos(q3)+l4*math.cos(q4)+tk*math.sin(q4),l1*math.sin(q1)+l2*math.sin(q2)+l3*math.sin(q3)+l4*math.sin(q4)-tk*math.cos(q4))
                                )   
                            link_5 = (
                                (l1*math.cos(q1)+l2*math.cos(q2)+l3*math.cos(q3)+l4*math.cos(q4)+tk*math.sin(q5),l1*math.sin(q1)+l2*math.sin(q2)+l3*math.sin(q3)+l4*math.sin(q4)-tk*math.cos(q5)),
                                (l1*math.cos(q1)+l2*math.cos(q2)+l3*math.cos(q3)+l4*math.cos(q4)-tk*math.sin(q5),l1*math.sin(q1)+l2*math.sin(q2)+l3*math.sin(q3)+l4*math.sin(q4)+tk*math.cos(q5)),
                                (l1*math.cos(q1)+l2*math.cos(q2)+l3*math.cos(q3)+l4*math.cos(q4)+l5*math.cos(q5)-tk*math.sin(q5),l1*math.sin(q1)+l2*math.sin(q2)+l3*math.sin(q3)+l4*math.sin(q4)+l5*math.sin(q5)+tk*math.cos(q5)),
                                (l1*math.cos(q1)+l2*math.cos(q2)+l3*math.cos(q3)+l4*math.cos(q4)+l5*math.cos(q5)+tk*math.sin(q5),l1*math.sin(q1)+l2*math.sin(q2)+l3*math.sin(q3)+l4*math.sin(q4)+l5*math.sin(q5)-tk*math.cos(q5))
                                )   
                            link_6 = (
                                (l1*math.cos(q1)+l2*math.cos(q2)+l3*math.cos(q3)+l4*math.cos(q4)+l5*math.cos(q5)+tk*math.sin(q6),l1*math.sin(q1)+l2*math.sin(q2)+l3*math.sin(q3)+l4*math.sin(q4)+l5*math.sin(q5)-tk*math.cos(q6)),
                                (l1*math.cos(q1)+l2*math.cos(q2)+l3*math.cos(q3)+l4*math.cos(q4)+l5*math.cos(q5)-tk*math.sin(q6),l1*math.sin(q1)+l2*math.sin(q2)+l3*math.sin(q3)+l4*math.sin(q4)+l5*math.sin(q5)+tk*math.cos(q6)),
                                (l1*math.cos(q1)+l2*math.cos(q2)+l3*math.cos(q3)+l4*math.cos(q4)+l5*math.cos(q5)+l6*math.cos(q6)-tk*math.sin(q6),l1*math.sin(q1)+l2*math.sin(q2)+l3*math.sin(q3)+l4*math.sin(q4)+l5*math.sin(q5)+l6*math.sin(q6)+tk*math.cos(q6)),
                                (l1*math.cos(q1)+l2*math.cos(q2)+l3*math.cos(q3)+l4*math.cos(q4)+l5*math.cos(q5)+l6*math.cos(q6)+tk*math.sin(q6),l1*math.sin(q1)+l2*math.sin(q2)+l3*math.sin(q3)+l4*math.sin(q4)+l5*math.sin(q5)+l6*math.sin(q6)-tk*math.cos(q6))
                                )             



                            obstacle = ((300, 300), 20)

                            collide_1 = gjk.collidePolyCircle(link_1, obstacle)
                            polygon(link_1)
                            circle(obstacle)
                            collide_2 = gjk.collidePolyCircle(link_2, obstacle)
                            polygon(link_2)
                            circle(obstacle)
                            collide_3 = gjk.collidePolyCircle(link_3, obstacle)
                            polygon(link_3)
                            circle(obstacle)
                            collide_4 = gjk.collidePolyCircle(link_4, obstacle)
                            polygon(link_4)
                            circle(obstacle)
                            collide_5 = gjk.collidePolyCircle(link_5, obstacle)
                            polygon(link_5)
                            circle(obstacle)
                            collide_6 = gjk.collidePolyCircle(link_6, obstacle)
                            polygon(link_6)
                            circle(obstacle)

                            # # make graph to see robot arm and obstacle

                            # fig, ax = plt.subplots()

                            # link1_patch = patches.Polygon(link_1, edgecolor='blue', facecolor='blue')
                            # ax.add_patch(link1_patch)
                            
                            # link2_patch = patches.Polygon(link_2, edgecolor='red', facecolor='red')
                            # ax.add_patch(link2_patch)

                            # obstacle_patch = patches.Circle(obstacle[0], obstacle[1], edgecolor='black', facecolor='black')
                            # ax.add_patch(obstacle_patch)

                            # ax.set_xlim(-400, 400)
                            # ax.set_ylim(-400, 400)
                            
                            # plt.show()


                            # # print result

                            # print('True' if (collide_1 or collide_2) else 'fail')

                            # save result to txt file continue

                            file_path = "/home/jeongil/collision/making_file/6dof_2D_result.txt"
                            
                            if (collide_1 or collide_2 or collide_3 or collide_4 or collide_5 or collide_6):

                                with open(file_path, "a") as file:          
                                    file.write(f"q1 : {q1_rad}  ,")
                                    file.write(f"q2 : {q2_rad}  ,")
                                    file.write(f"q3 : {q3_rad}  ,")
                                    file.write(f"q4 : {q4_rad}  ,")
                                    file.write(f"q5 : {q5_rad}  ,")
                                    file.write(f"q6 : {q6_rad}  ,")
                                    file.write(f"collision \n")

    end = time.time()

    #check time and print, save in txt file
    
    print(f"{end - start :.5f} sec")

    file_path = "/home/jeongil/collision/making_file/6dof_2D_result.txt"
    with open(file_path, "a") as file:
        file.write(f"\ncalculation time is : {end - start :.5f} sec")

    



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


