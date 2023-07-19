import matplotlib.pyplot as plt
import time


start = time.time()

# 텍스트 파일 경로
file_path = "/home/jeongil/collision/making_file/2dof_2D_graph_data.txt"

# 데이터를 저장할 리스트
x_values = []
y_values = []
z_values = []

# 파일에서 데이터 읽어오기
with open(file_path, "r") as file:
    for line in file:
        # 각 줄의 데이터를 분리하여 x, y, z로 나눔
        data = line.strip().split(",")
        x = float(data[0])
        y = float(data[1])
        z = float(data[2])
        x_values.append(x)
        y_values.append(y)
        z_values.append(z)

# 그래프 그리기
plt.figure()

# z 값에 따라 점 색상 설정하여 그래프 그리기
for x, y, z in zip(x_values, y_values, z_values):
    if z == 0:
        plt.plot(x, y, 'ob')
    else:
        plt.plot(x, y, 'or')

# 축 라벨 설정
plt.xlabel("q1")
plt.ylabel("q2")

# 그래프 보이기
plt.title("C-space")
plt.grid(False)

end = time.time()
print(f"{end - start :.5f} sec")

plt.show()


