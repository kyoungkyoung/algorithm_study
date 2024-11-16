matrix = [[3, 7, 9],
          [4, 2, 6],
          [8, 1, 5]]

# 인덱싱
print(matrix[0][0])
print(matrix[0][2])

# 순회
# 행 우선 순회
for r in range(3):
    for c in range(3):
        print(matrix[r][c])

# 열 우선 순회
for c in range(3):
    for c in range(3):
        print(matrix[r][c])
        
# 전치 (y=x 대칭)
for r in range(3):
    for c in range(3):
        if c > r:
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
            
print(matrix)

# zip 함수를 이용한 전치
# zip 함수는 *로 가장 밖에 있는 Iterable 객체를 떼어줌 -> *matrix
# 튜플 : 불변인 리스트
# zip 함수는 값을 튜플로 리턴해줌
print(list(zip(*matrix))) #[(3, 7, 9), (4, 2, 6), (8, 1, 5)]
print(list(map(list,zip(*matrix)))) #[[3, 7, 9], [4, 2, 6], [8, 1, 5]]