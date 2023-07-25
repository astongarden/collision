import numpy as np


def parse_input_file(file_path):
    with open(file_path, 'r') as file:
        data = []
        for line in file:
            # 예상 형식: angle1,angle2,collision
            angle1, angle2, collision = map(float, line.strip().split(','))
            data.append((angle1, angle2, int(collision)))
        return data

def process_data(data):
    for angle1, angle2, collision in data:
        # 여기서 데이터 처리 또는 구분 작업을 수행합니다.
        if collision == 1:
            print(f"Angles: {angle1}, {angle2} - Collision: YES")
        else:
            print(f"Angles: {angle1}, {angle2} - Collision: NO")

if __name__ == "__main__":
    input_file_path = "/home/jeongil/collision/making_file/dataset.txt"  # 입력 파일 경로
    data = parse_input_file(input_file_path)
    process_data(data)
