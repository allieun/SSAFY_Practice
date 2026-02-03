'''
Flatten 문제 (SWEA 4831)
'''

T = 10

for tc in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))

    max_val = max(num_list)
    min_val = min(num_list)

    if max_val - min_val <= 1:
        break

    num_list[num_list.index(max_val)] -= 1
    num_list[num_list.index(min_val)] += 1

    answer = max(num_list) - min(num_list)

    print(f'#{tc} {answer}')