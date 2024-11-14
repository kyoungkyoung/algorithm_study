T = int(input())

# 재귀함수
def binary_search(l, r, target, cnt):
    # 가운데를 찝는다
    c = int((l+r)/2)
    
    # c가 타겟과 일치?
    if c == target:
        # return 탐색횟수
        return cnt
        
    # c가 타겟보다 크다면?
    elif c > target:
        # 왼쪽 절반으로 재귀(r 갱신)
        return binary_search(l, c, target, cnt+1)

    # c가 타겟보다 작다면?
    elif c < target:
        # 오른쪽 절반으로 재귀(l 갱신)
        return binary_search(c, r, target, cnt+1)

# while
def binary_search_2(l, r, target, cnt):

    while True:
        c = int((l+r)/2)
        
        if c == target:
            return cnt
        
        elif c > target:
            r = c
            
        elif c < target:
            l = c
            
        cnt += 1
    

for tc in range(1, T+1):
    p, a, b = map(int, input().split())
    # A = binary_search(1, p, a, 1)
    # B = binary_search(1, p, b, 1)
    
    A = binary_search_2(1, p, a, 1)
    B = binary_search_2(1, p, b, 1)
    
    
    
    # if A < B:
    #     print("A")
    # elif B < A:
    #     print("B")
    # else:
    #     print(0)
        
    print("A" if A<B else "B" if B<A else 0)