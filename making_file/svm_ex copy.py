import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np
from sklearn.svm import SVC
import gjk, math
from matplotlib.patches import Rectangle, Circle, Polygon

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE  = (  0,   0, 255)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)

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

def plot_decision_regions(X, y, classifier, test_idx=None, resolution=0.02):

    # 마커와 컬러맵을 설정합니다.
    markers = ('s', 'x', 'o', '^', 'v')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])

    # 결정 경계를 그립니다.
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                           np.arange(x2_min, x2_max, resolution))
    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, Z, alpha=0.3, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())

    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cl, 0],
                    y=X[y == cl, 1],
                    alpha=0.8,
                    c=colors[idx],
                    marker=markers[idx],
                    label=cl,
                    edgecolor='black')

robot_link1 = 150
robot_link2 = 100
robot_thickness = 40
obstacle = ((50, 100), 30)
collision_true = []
collision_false = []
result = []

for i in range(10):
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
        collision = [1]
        collision_true= np.append(q)
        result = np.append(collision)
    else:
        collision = [0]
        collision_false = np.append(q)
        result = np.append(collision)
    
    collision_true = np.reshape(collision_true, (-1, 2))
    collision_false = np.reshape(collision_false, (-1, 2))
    y_xor = result
    collision_result = collision_true + collision_false



# np.random.seed(1)
# X_xor = np.random.randn(10, 2)
# y_xor = np.logical_xor(X_xor[:, 0] > 0,
#                        X_xor[:, 1] > 0)
# y_xor = np.where(y_xor, 1, -1)
if y_xor == 1:
    X, Y = collision_true
    plt.scatter(X, Y, 
                c='b', marker='x',
                label='1')
else:
    X, Y = collision_false
    plt.scatter(X, Y,
                c='r',
                marker='s',
                label='-1')

plt.xlim([-3, 3])
plt.ylim([-3, 3])
plt.legend(loc='best')
plt.tight_layout()
plt.show()

        
svm = SVC(kernel='rbf', random_state=1, gamma=0.10, C=10.0)
svm.fit(collision_result, y_xor)
plot_decision_regions(collision_result, y_xor,
                      classifier=svm)
 
plt.legend(loc='upper left')
plt.tight_layout()
plt.show()



