t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())             # 리스트 A의 길이 n, 리스트 B의 길이 m
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))

    i, j = 0, 0                                   # 인덱스 기본값을 각각 0으로 설정(n_list와 m_list)

    while i < n and j < m:                        # 각각 리스트의 인덱스가 각각의 리스트 길이보다 작을 때
        if b_list[j] == a_list[i]:                # b_list의 값이 a_list에 있다면 j에 1 추가
            j += 1
        i += 1

    if j == m:                                    # j 값이 b_list 길이와 같아질 경우 YES, 아닐 경우 NO 출력
        answer = 'YES'
    else:
        answer = 'NO'

    print(f'#{tc} {answer}')