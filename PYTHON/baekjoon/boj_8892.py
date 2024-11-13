import sys
input = sys.stdin.readline
# readline으로 input을 받으면 끝에 \n(개행)이 항상 붙게 된다.
# 반드시 strip() or rstrip()으로 공백을 없애준다.

from itertools import permutations

def find_palindrome():
    # 2중 for문을 활용해서 단어 두개를 뽑은 후,
    for i in range(k):
        for j in range(k):
            # 같은걸 뽑았다면 넘어간다
            if i == j:
                continue
            # 둘을 이어 붙이고
            word = word[i] + word[j]
            # 회문이라면?
            if word == word[::-1]:
                # 출력 후 break
                print(word)
                # 반드시 
                return word
            
    return 0                
            
T = int(input())
for _ in range(T):
    k = int(input())
    
    # list comprehension
    words = [input().rstrip() for _ in range(k)]
    # words = []
    # for _ in range(k):
    #     word = input().rstrip()
    #     words.append(word)
    
    
    
    # 2중 for문을 활용해서 단어 두개를 뽑은 후,
    for i in range(k):
        for j in range(k):
            # 같은걸 뽑았다면 넘어간다
            if i == j:
                continue
            # 둘을 이어 붙이고
            word = word[i] + word[j]
            # 회문이라면?
            if word == word[::-1]:
                # 출력 후 break
                print(word)
                # exit를 만나면 더이상 파일을 실행하지 않음
                exit(0)

        # 찾지 못했다면?
        # 0 출력
    print(0)    
                #
            
    '''
    # 순열 모듈을 활용해서 단어 두개를 뽑은 후,
    for w1, w2 in permutations(words, 2):
        # 둘을 이어 붙이고
        word = w1 + w2
        # 회문이라면?
        if word == word[::-1]:
            # 출력 후 break
            break
        
        # 찾지 못했다면?
    else:
        # 0 출력
        print(0)    
                #
    '''