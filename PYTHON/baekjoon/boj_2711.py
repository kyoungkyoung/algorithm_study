T = int(input())

# case1
'''
for _ in range(T):
    idx, word = input().split(' ')
    idx = int(idx)
    if idx > 2:
        print(word[0:(idx-1)] + word[idx:])
    elif idx == 1:
        print(word[1:])
    elif idx == 2:
        print(word[0] + word[2:])
    # new_word = word[0:(int(idx)-2)]+word[(int(idx)-1):]
    # print(new_word)
'''

# case2
for _ in range(T):
    idx, word = input().split()
    idx = int(idx)-1
    ans = word[:idx] + word[idx+1:]
    
    print(ans)
    
'''
# case3
for _ in range(T):
    idx, word = input().split()
    idx = int(idx)-1
    word = list(word)
    word.pop(idx)
    ans = ''.join(word)
    
    print(ans)
'''