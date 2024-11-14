n = int(input())

# fibo(n) = fibo(n-1) + fibo(n-2) (단, n >= 2)

def fibo(N):
    # 리턴 조건
    if N <= 1:
        return N
    
    # 탐색 로직
    return fibo(N-1) + fibo(N-2)

print(fibo(n))
