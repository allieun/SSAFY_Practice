'''
**[입력]**

총 10개의 테스트케이스가 주어진다.

각 테스트케이스의 첫 번째 줄에는 건물의 개수 N이 주어진다. (4 ≤ N ≤ 1000)

그 다음 줄에는 N개의 건물의 높이가 주어진다. (0 ≤ 각 건물의 높이 ≤ 255)

맨 왼쪽 두 칸과 맨 오른쪽 두 칸에 있는 건물은 항상 높이가 0이다. (예시에서 빨간색 땅 부분)

**[출력]**

#부호와 함께 테스트케이스의 번호를 출력하고, 공백 문자 후 조망권이 확보된 세대의 수를 출력한다.
# '''


T = 10
# 테스트 케이스 개수는 10으로 지정


# 테스트 케이스의 범위 내에서 건물 갯수 N을 받고 그 개수만큼의 인자를 받아 리스트로
for tc in range(1, T-2):
    N = int(input())
    heights = list(map(int, input().split()))
    for i in range(2, N-2):
        current_height = 0
        max_height = [heights[i-2], heights[i-1], heights[i+1], heights[i+2]]
        if heights[i] > max_height:
            current_height += heights[i] - max_height
    
    print(f'#{tc} {current_height}')

