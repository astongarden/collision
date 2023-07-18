import pybullet as p
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

# PyBullet 시뮬레이션 초기화
p.connect(p.DIRECT)
p.setGravity(0, 0, -9.81)
plane_id = p.createCollisionShape(p.GEOM_PLANE)
plane = p.createMultiBody(0, plane_id)

# 로봇팔 모델링
robot = p.loadURDF("robot.urdf", [0, 0, 0], useFixedBase=True)

# 데이터 수집
joint_angles = []
collision_labels = []

for _ in range(1000):
    # 무작위로 관절 각도 생성
    joint_angle_1 = np.random.uniform(-np.pi, np.pi)
    joint_angle_2 = np.random.uniform(-np.pi, np.pi)
    joint_angles.append([joint_angle_1, joint_angle_2])

    # 로봇팔 위치 업데이트
    p.resetJointState(robot, 0, joint_angle_1)
    p.resetJointState(robot, 1, joint_angle_2)
    p.stepSimulation()

    # 충돌 여부 확인
    contacts = p.getContactPoints(robot, plane)
    collision_labels.append(int(len(contacts) > 0))

# 데이터 분할
joint_angles = np.array(joint_angles)
collision_labels = np.array(collision_labels)
X_train, X_test, y_train, y_test = train_test_split(joint_angles, collision_labels, test_size=0.2)

# MLP 모델 학습
mlp_model = MLPClassifier(hidden_layer_sizes=(100, 100))  # 은닉층 크기는 예시로 (100, 100) 설정
mlp_model.fit(X_train, y_train)

# 테스트 데이터에 대한 예측
predictions = mlp_model.predict(X_test)

# 예측 결과 출력
for i in range(len(X_test)):
    print("입력 관절 각도:", X_test[i])
    print("실제 충돌 여부:", y_test[i])
    print("예측된 충돌 여부:", predictions[i])
    print()

# 시뮬레이션 종료
p.disconnect()