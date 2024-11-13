'''
import sys
input = sys.stdin.readline
books = {}

N = int(input())

# 반복문으로 input()값을 카운팅해서 Dict에 넣어주기
for _ in range(N):
    book, _ = input().split('\n')
    books[book] = books.get(book, 0) + 1
    print(books)

# Dict 안에 있는 값을 가져와서 가장 큰 숫자 비교
result = set()
for book in books:
    max_num = -float("INF")
    books[book]
    # print(books[book])


'''





# ===================================
# 집계하는 알고리즘
N = int(input())

# [ 구조화 ]

# 빈 딕셔너리 제작
sales_info = {}
# 반복문을 돌며
for _ in range(N):
    # 책 제목을 입력받고
    book_name = input()
    
# 1. 조건문을 통한 분기 
    # 만약 딕셔너리에 해당 제목이 없다면? -> 생성
    if book_name not in sales_info:
        sales_info[book_name] = 1
    # 있다면? -> 1 더해주기
    else:
        sales_info[book_name] += 1
        
# 2. get() 활용
    sales_info[book_name] = sales_info[book_name].get(book_name, 0) + 1
    
# 3. defaultdict 활용 -> 딕셔너리와 비슷한 별도의 객체 -> 외부에서 모듈 가져와서 작성해야함
from collections import defaultdict
# defaultdict 객체는 default 값이 정해져있는 dictionary
# 만약 없는 key값으로 접근한다면 내가 지정해준 default 값 출력해줌
sales_info = defaultdict(int)

for _ in range(N):
    book_name = input()
    sales_info[book_name] += 1

# 4. Counter 활용
from collections import Counter
# list comprehension -> 넣을거 반복문
sales_info = [input() for _ in range(N)]
sales_info = Counter(sales_info)

# [ 연산 ]
max_sales_cnt = 0
max_sales_book = ''
max_sales_book_list = []

# for name in sales_info:
#     if sales_info[name] >= max_sales_cnt and max_sales_book > name:
#         max_sales_book_list.append(name)

for name, cnt in sales_info.items():
    if cnt >= max_sales_cnt and max_sales_book > name:
        max_sales_book = name

# print(book for book in max_sales_book_list)

# 딕셔너리 정렬

# .sort() -> 리스트에서만 사용, 원본을 변경
# sorted() -> iterable을 받는다 -> return 값이 반드시 list가 되고, 원본을 변경하지 않음

# key값만 가져오려면 그냥 sorted(sales_info)를 하면 되지만 value값도 같이 가져와야 하기 때문에 items()를 사용
# 아주 구체적인 정렬기준을 만들기 위해 lambda를 사용
# key 값을 정렬할때는 임시함수인 lambda를 사용한다
# key 값은 각각의 값을 가져오는 것임
# 2개 이상의 정렬 기준을 작성할때는 튜플()로 묶어줘야함
# []
sorted_sales_info = sorted(sales_info.items(), key=lambda x: (-x[1], x[0]))

sorted_sales_info = sorted()