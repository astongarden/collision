import numpy as np
import matplotlib.pyplot as plt

# 예시 데이터
x_values = [1, 1, 1, 2, 2, 2, 3, 3, 3]
y_values = [1, 2, 3, 1, 2, 3, 1, 2, 3]
z_values = [3, 5, 2, 4, 6, 8, 1, 7, 9]

# 데이터를 2D 배열로 변환
x_unique = np.sort(np.unique(x_values))
y_unique = np.sort(np.unique(y_values))
z_array = np.zeros((len(y_unique), len(x_unique)))

for x, y, z in zip(x_values, y_values, z_values):
    x_index = np.where(x_unique == x)[0][0]
    y_index = np.where(y_unique == y)[0][0]
    z_array[y_index, x_index] = z

# 히트맵 그리기
plt.imshow(z_array, cmap='hot', origin='lower', extent=[x_unique[0], x_unique[-1], y_unique[0], y_unique[-1]])
plt.colorbar()

# 축 라벨 설정
plt.xlabel("X")
plt.ylabel("Y")

# 그래프 보이기
plt.title("Heatmap")
plt.show()