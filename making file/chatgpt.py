import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# 두 개의 독립 변수 생성
X = np.random.rand(100, 2)  # 100개의 랜덤한 좌표 생성

# 충돌 여부를 나타내는 종속 변수 생성
y = np.zeros(100)  # 초기값은 충돌 없음

# 독립 변수의 일부를 수정하여 충돌을 발생시킴
X[10:20, 0] = np.random.rand(10) * 0.4 + 0.3
X[30:40, 1] = np.random.rand(10) * 0.4 + 0.3
y[10:20] = 1  # 충돌 발생
y[30:40] = 1  # 충돌 발생


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

accuracy = knn.score(X_test, y_test)
print("Accuracy:", accuracy)