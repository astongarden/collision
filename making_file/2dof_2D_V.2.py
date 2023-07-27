import gjk
import math
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Polygon
import ast
from sklearn.svm import SVC
from matplotlib.colors import ListedColormap

# color
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE  = (  0,   0, 255)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)

# information of test environment
robot_link1 = 150
robot_link2 = 100
robot_thickness = 40
obstacle = ((50, 100), 30)
# obstacle = ((np.random.randint(10, 200),np.random.randint(10, 200)), np.random.randint(10, 50))

collision_true = []
collision_false = []
result = []

# calculate collision with circle obstacle
def run_random_angle():

    for i in range(3):
        q1_rad = (np.random.rand(1)[0] * 360)
        q2_rad = (np.random.rand(1)[0] * 360)
        q = [q1_rad] + [q2_rad]

        q1 = math.radians(q1_rad)
        q2 = math.radians(q2_rad)

        link1_1=np.array(([0, robot_thickness/2], [0,-robot_thickness/2], [robot_link1, -robot_thickness/2], [robot_link1, robot_thickness/2]))
        r1 = np.array(([math.cos(q1), -math.sin(q1)], [math.sin(q1), math.cos(q1)]))
        link1_ro = np.matmul(r1, link1_1.T)
        link_1 = (link1_ro.T)

        link2_1 = np.array(([0, robot_thickness/2], [0, -robot_thickness/2], [robot_link2, -robot_thickness/2], [robot_link2, robot_thickness/2]))
        r2 = np.array(([math.cos(q2), -math.sin(q2)], [math.sin(q2), math.cos(q2)]))
        link2_ro = np.matmul(r2, link2_1.T)
        link2_ro += np.array(([robot_link1], [0]))
        link2_ro2 = np.matmul(r1, link2_ro)
        link_2 = (link2_ro2.T)

        # collision check with circle obstacle
        collide_1 = gjk.collidePolyCircle(link_1, obstacle)
        circle(obstacle)
        collide_2 = gjk.collidePolyCircle(link_2, obstacle)
        circle(obstacle)

        if collide_1 or collide_2:
            collision = 1
            collision_true.append(q)
            result.append(collision)
        else:
            collision = 0
            collision_false.append(q)
            result.append(collision)

        # # show robot link
        # fig, ax = plt.subplots()
        # body = Polygon(link_1)
        # ax.add_patch(body)
        # body = Polygon(link_2)
        # ax.add_patch(body)
        # ax.set_xlim(-300, 300)
        # ax.set_ylim(-300, 300)
        # plt.show()


def make_C_space():
    start = time.time()

    plt.scatter([], [], color='RED', s=10, alpha=0.5, marker='s', label='collision_true')
    plt.scatter([], [], color='BLUE', s=10, alpha=0.5, marker='o', label='collision_false')

    for coordinates in collision_true:
        x, y = coordinates
        plt.scatter(x, y, color='RED', s=10, alpha=0.5, marker='s')
    for coordinates in collision_false:
        x, y = coordinates
        plt.scatter(x, y, color='BLUE', s=10, alpha=0.5, marker='o')

    # plt.xlabel("joint 1 angle(q1, degrees)")
    # plt.ylabel("joint 2 angle(q2, degrees)")
    # plt.title("C-space")
    # plt.legend()
    # end = time.time()
    # print(f"{end - start :.5f} sec")
    # plt.show()

    # svm = SVC(kernel='rbf', random_state=1, gamma=0.10, C=10.0)
    # collision_result = collision_true + collision_false
    # svm.fit(collision_result, result)
    # plot_decision_regions(collision_result, result, classifier=svm)
    # plt.legend(loc='upper left')
    # plt.tight_layout()
    # plt.show()


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

def plot_decision_regions(x, y, classifier, test_idx=None, resolution=0.02):

    # 마커와 컬러맵을 설정합니다.
    markers = ('o', 's', 'x', '^', 'v')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])

    # 결정 경계를 그립니다.
    x1_min, x1_max = x[:][0].min() - 1, x[:][0].max() + 1
    x2_min, x2_max = x[:][1].min() - 1, x[:][1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                           np.arange(x2_min, x2_max, resolution))
    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, Z, alpha=0.3, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())

    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(X=x[y == cl, 0],
                    y=x[y == cl, 1],
                    alpha=0.8,
                    c=colors[idx],
                    marker=markers[idx],
                    label=cl,
                    edgecolor='black')

# run code 
if __name__ == '__main__':

    start = time.time()

    # collision check for N time
    run_random_angle()

    end = time.time()
    # check time
    print(f"{end - start :.5f} sec")

    # make C-space graph
    make_C_space()
