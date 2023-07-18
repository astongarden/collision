import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import matplotlib.patches as patches

# 로봇 정보
robot_length_1 = 1.0    # 로봇 link1 길이
robot_length_2 = 1.0    # 로봇 link2 길이
robot_thickness = 0.2   # 로봇 link 두께
joint_limits = [[-np.pi, np.pi], [-np.pi, np.pi]]  # 관절 각도 제한

# 로봇팔 관절 각도 입력
joint_angle1 = float(input("Enter joint angle 1(deg): "))
joint_angle2 = float(input("Enter joint angle 2(deg): "))

robot_angles = [joint_angle1, joint_angle2]

# 랜덤 장애물 생성
obstacle_x = np.random.uniform(0, 1)
obstacle_y = np.random.uniform(0, 1)
obstacle_width = np.random.uniform(0.2, 0.5)
obstacle_height = np.random.uniform(0.2, 0.5)


# 워크스페이스 그리기
def plot_workspace(robot_angles):

    robot_angles = np.deg2rad(robot_angles)

    # 로봇팔 위치 계산
    x1 = robot_length_1 * np.cos(robot_angles[0])
    y1 = robot_length_1 * np.sin(robot_angles[0])
    x2 = x1 + robot_length_2 * np.cos(robot_angles[0] + robot_angles[1])
    y2 = y1 + robot_length_2 * np.sin(robot_angles[0] + robot_angles[1])

    # 장애물 그리기
    fig, ax = plt.subplots()
    rect = patches.Rectangle((obstacle_x, obstacle_y), obstacle_width, obstacle_height, edgecolor='black', facecolor='yellow', fill=True)
    ax.add_patch(rect)

    # 그래프 그리기
    plt.plot([0, x1, x2], [0, y1, y2], 'k-')
    plt.plot(0, 0, 'ro', label='1 joint')
    plt.plot(x1, y1, 'go', label='2 joint')
    plt.plot(x2, y2, 'bo', label='End Effector')

    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Workspace')
    plt.legend()
    plt.grid(True)
    plt.axis('equal')
    plt.show()

# 로봇팔 위치 그리기
plot_workspace(robot_angles)

# # C-space 그래프 생성
# def plot_cspace():
#     # 각도 범위
#     theta1 = np.linspace(joint_limits[0][0], joint_limits[0][1], 100)
#     theta2 = np.linspace(joint_limits[1][0], joint_limits[1][1], 100)
#     theta1, theta2 = np.meshgrid(theta1, theta2)

#     # 그래프 그리기
#     plt.contourf(theta1, theta2, np.zeros_like(theta1), cmap='gray')
#     plt.xlabel('Joint 1 Angle')
#     plt.ylabel('Joint 2 Angle')
#     plt.title('C-space')
#     plt.grid(True)
#     plt.show()

# # 충돌 여부 예측
# def predict_collision(robot_angles):
#     # 여기에서는 단순히 무작위로 충돌 여부를 예측하는 것으로 가정
#     return bool(np.random.randint(0, 2))


# # C-space 그래프 그리기
# plot_cspace()