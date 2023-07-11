import numpy as np

# 퍼셉트론 클래스 정의
class Perceptron():
    def __init__(self, input_size):
        self.wights = np.zeros(input_size)
        self.bias = 0

    def predict(self, inputs):
        summation = np.dot(inputs, self.wights) + self.bias
        return np.where(summation > 0, 1, -1)
        #  return 1 if summation > 0 else 0

    def train(self, inputs, label, learning_rate):
        prediction = self.predict(inputs)
        self.wights += learning_rate * (label - prediction) * inputs
        self.bias += learning_rate * (label - prediction)

# 퍼셉트론 모델 학습
def train_collision_detection():
    # 학습 데이터
    data = np.loadtxt('/home/jeongil/fastron_python/fastron/데이터파일', delimiter = ",", dtype = np.float32)    # ','로 데이터 구분
    inputs = data[:, 0:-1]      # 로봇 팔 입력 각도(파일의 앞에서 2개 데이터)
    labels = data[:, [-1]]      # 충돌 여부(정답)(파일의 뒤에서 1개 데이터)
    
    # 퍼셉트론 모델 생성
    perceptron = Perceptron(input_size=2)

    # 학습 파라미터 설정
    learning_rate = 0.1
    epochs = 15

    # 퍼셉트론 모델 학습
    for i in range(epochs):
        for inputs, label in zip(inputs, labels):
            perceptron.train(inputs, label, learning_rate)

    return perceptron

# 퍼셉트론 모델 테스트
def test_collision_detection(perceptron):
    # 테스트 데이터
    data = np.loadtxt('/home/jeongil/fastron_python/fastron/테스트파일', delimiter = ",", dtype = np.float32)    # ','로 데이터 구분
    inputs = data[:,]     


    # 퍼셉트론 모델을 통한 충돌 감지 테스트
    for test_input in test_inputs:
        prediction = perceptron.predict(test_input)
        if prediction == 1:
            print("collision O")
        else:
            print("collision X")

# 충돌 감지 퍼셉트론 모델 학습 및 테스트
perceptron = train_collision_detection()
test_collision_detection(perceptron)
