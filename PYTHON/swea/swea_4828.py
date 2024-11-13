# 3
# 5
# 477162 658880 751280 927930 297191
# 5
# 565469 851600 460874 148692 111090
# 10
# 784386 279993 982220 996285 614710 992232 195265 359810 919192 158175	 


T = int(input())

for tc in range(1, T+1):
    # map()을 이용해 형변환
    # map -> list로 바꾸기 위해 list() 사용
    N = int(input())
    nums = list(map(int,input().split()))
    
    # 초기값 설정
    # min_num = -float("INF") #float(infinite)
    # max_num = float("INF")
    min_num = nums[0]
    max_num = nums[0]
    
    for num in nums:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num

    ans = max_num - min_num
    print(f'#{tc} {ans}')