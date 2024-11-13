import sys
input = sys.stdin.readline

N, K = int(input())
nums = list(map(int, input().split()))

# 첫 번째 구간의 합 -> 직접 구하기
max_num = tmp = sum(nums[:K])

# N-K번 반복하며
for i in range(N-K+1):
    # 왼쪽을 빼고 오른쪽은 더하기
    tmp = tmp - nums[i] + nums[i+K]
    tmp += - nums[i] + nums[i+K]
    
    # 갱신하기
    max_sum = max(max_num, tmp)