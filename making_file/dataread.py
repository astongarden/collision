import numpy as np


def dataset(file_path):
    with open(file_path, 'r') as file:
        data = []
        for line in file:
            angle1, angle2, collision = map(float, line.strip().split(','))
            data.append((angle1, angle2, int(collision)))
        return data



if __name__ == "__main__":
    datafile = "/home/jeongil/collision/making_file/dataset.txt"  # 입력 파일 경로
    data = dataset(datafile)
