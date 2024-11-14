a = 5
def my_func():
    b = 10
    b += a
    return b

# global 변수 재할당
def my_func2():
    global a
    a += 5
    
    
# Enclosed
def my_func3():
    a = 3
    
    def child_func():
        global a # 바로 위, a = 3인 my_func3()의 a값을 가져옴
        # nonlocal a
        a += 5
    
    child_func()
    return a
    

# print(my_func())
# my_func2()
# print(a)
print(my_func3())
print(a)


# list는 global로 정하지 않고, 그냥 사용한다.
a_list = [1,2,3,4,5]
def my_list_func():
    a_list.append(6)
    
my_list_func()
print(a_list)


# 재귀함수 =======================================
nums = [-5, 2, 7, -3, 2, 10, 8, 6, 5, -1]
ans = -float("INF")

def my_func_self(idx):
    global ans
    # 재귀의 종료 조건
    if idx > len(nums)-1:
        return ans
    # 탐색 로직
    if nums[idx] > ans:
        ans = nums[idx]
        
    my_func_self(idx+1)
    
    return ans     

result = my_func_self(0)
print(result)



ans2 = -float("INF")
def my_func_self2(idx):
    global ans2
    # 재귀의 종료 조건
    # idx가 len(nums)일 때 종료
    if idx == len(nums):
        return ans2
    
    # 탐색 로직
    # nums[idx]와 ans를 비교하여 큰 값으로 갱신
    ans2 = max(nums[idx], ans2)
    
    my_func_self2(idx+1)
    
my_func_self2(0)


# 재귀함수 example
def find(depth):
    if depth == 10:
        print("찾았다!!")
        return
    
    print(f'탐색하는 중... 깊이는 {depth}')
    
    find(depth+1)
    
    print(f'올라가는 중... 깊이는 {depth}')
    
find(0)
