'''
N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산하는 것은 디지털 필터링의 기초연산이다.
M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력하는 프로그램을 작성하시오.

다음은 N=5, M=3이고 5개의 숫자 1 2 3 4 5가 배열 v에 들어있는 경우이다.
이웃한 M개의 합이 가장 작은 경우 1 + 2 + 3 = 6

이웃한 M개의 합이 가장 큰 경우 3 + 4 + 5 = 12

답은 12와 6의 차인 6을 출력한다.
'''

T = int(input())                                            # 테스트 케이스 개수 입력

for tc in range(1, T+1):
    N, M = map(int, input().split())                        # N개의 정수 개수/ 이웃한 개수 합 M 각각 입력
    num_list = list(map(int, input().split()))              # N개의 정수 배열 입력 후 리스트화
    sum_list = []                                           # 구간 합 각각을 담을 리스트 입력
    for i in range(N-M +1):
        current_sum = 0
        for j in range(i, i+M):
            current_sum += num_list[i]
        sum_list.append(current_sum)
        answer = max(sum_list) - min(sum_list)
    print(f'#{tc} {answer}')