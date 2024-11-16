#     상,하,좌,우
#     0, 1,2,3
dr = [-1,1,0,0]
dc = [0,0,-1,1]

matrix = [[3, 7, 9],
          [4, 2, 6],
          [8, 1, 5]]

r, c = 1, 1

for d in range(4):
    nr, nc = r+dr[d], c+dc[d]
    print(matrix[nr][nc])
