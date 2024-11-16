T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(N)]
    
    # 정답 초기화(0)
    result = 0
    
    # 2중 for문으로 flies를 순회하며
    for r in range(N-M+1):
        for c in range(N-M+1):
            # r, c를 기준으로
            tmp = 0
            
            for y in range(r, r+M):
                for x in range(c, c+M):
                    tmp += flies[y][x]