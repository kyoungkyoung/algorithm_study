# 일곱난쟁이
'''
dwarfs = [int(input()) for _ in range(9)]
dwarfs.sort()

# 2중 for문을 활용 -> 시간복잡도 = N^2
flag = False
for i in range(8):
    for j in range(i+1, 9):
        # 만약 i번째 난쟁이 키와 j번째 난쟁이 키를 전체 합에서 빼서 100이 된다면?
        if sum(dwarfs) - dwarfs[i] - dwarfs[j] == 100:
        # i, j를 보관 -> 바로 pop()을 해버리는 순간 Index가 바뀌기 때문에!!
            spy = [i, j]
        # 2중 for문 종료
            flag = True
            break
    if flag:
        break
    
# 하나씩 출력
for idx in range(9):
# (i, j 번째는 출력하지 않음)
    if idx in spy:
        continue
    
    print(dwarfs[idx])
    
'''    
    
    
# module 사용
from itertools import combinations
dwarfs = [int(input()) for _ in range(9)]
dwarfs.sort()

# 9C7
# print(list(combinations(dwarfs, 7))) 
for combi in combinations(dwarfs, 7):
    if sum(combi) == 100:
        for dwarf in combi:
            print(dwarf)
        break