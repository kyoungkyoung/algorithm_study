import sys
input = sys.stdin.readline
names = set()

T = int(input())

for i in range(T):
    name, el = input().split()
    if el == 'enter':
        names.add(name)
    else:
        names.discard(name)

names = list(names)
names.sort(reverse=True)

for i in range(len(names)):
    print(names[i])