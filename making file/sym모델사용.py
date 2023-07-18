import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

# 로봇팔의 관절 각도 데이터
joint_angles = np.array([[0.2, 0.5],
                        [0.3, 0.4],
                        [0.1, 0.7],
                        [0.4, 0.3]])

# 충돌 여부 데이터 (1: 충돌 있음, 0: 충돌 없음)
collision_labels = np.array([1, 0, 1, 0])

# 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(joint_angles, collision_labels, test_size=0.2)

# SVM 모델 학습
svm_model = SVC()
svm_model.fit(X_train, y_train)

# 테스트 데이터에 대한 예측
predictions = svm_model.predict(X_test)

# 예측 결과 출력
for i in range(len(X_test)):
    print("입력 관절 각도:", X_test[i])
    print("실제 충돌 여부:", y_test[i])
    print("예측된 충돌 여부:", predictions[i])
    print()