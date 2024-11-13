import sys
input = sys.stdin.readline

from itertools import accumulate

N, M = map(int, input().split())
nums = list(map(int, input().split()))

# 누적합 리스트 만들기
acc = [0] + accumulate(nums)

for num in nums:
    # 누적합이기 때문에 acc의 가장 오른쪽 값에 계속 더해주기 때문에 acc[-1]로 써도 된다!
    acc.append(acc[-1] + num)
    
for _ in range(M):