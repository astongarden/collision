import numpy as np

data = '/home/jeongil/collision/making_file//2dof_2D_collision_data.txt/'

def load_data(file_path):
    with open(file_path, 'r')as file:
        data = file.readlines()
    return data

X_train = data[:, :2]  # 입력 데이터 (joint1_angle, joint2_angle)
y_train = data[:, 2]   # 레이블 (충돌 여부)


class Perceptron:
    def __init__(self, input_size, learning_rate=0.01, epochs=100):
        self.weights = np.zeros(input_size)
        self.bias = 0
        self.learning_rate = learning_rate
        self.epochs = epochs

    def activation_function(self, x):
        # 활성화 함수로 스텝 함수(step function)를 사용합니다.
        return 1 if x >= 0 else 0

    def predict(self, x):
        # 입력과 가중치의 내적에 편향을 더하여 예측 값을 구합니다.
        z = np.dot(x, self.weights) + self.bias
        return self.activation_function(z)

    def train(self, X, y):
        for _ in range(self.epochs):
            for i in range(len(X)):
                x = X[i]
                y_true = y[i]
                y_pred = self.predict(x)

                # 가중치와 편향을 업데이트합니다.
                self.weights += self.learning_rate * (y_true - y_pred) * x
                self.bias += self.learning_rate * (y_true - y_pred)

perceptron = Perceptron(input_size=2, learning_rate=0.01, epochs=100)
perceptron.train(X_train, y_train)


new_joint1_angle = 120
new_joint2_angle = 30
X_new = np.array([[new_joint1_angle, new_joint2_angle]])
prediction = perceptron.predict(X_new)

if prediction == 1:
    print(f"로봇 조인트 각도 {new_joint1_angle}도, {new_joint2_angle}도에서 충돌이 예상됩니다.")
else:
    print(f"로봇 조인트 각도 {new_joint1_angle}도, {new_joint2_angle}도에서 충돌이 예상되지 않습니다.")
