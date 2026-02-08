'''
달팽이 문제 풀이의 핵심   
1. 행 우선 순회와 열 우선 순회가 섞인 것
2. 기준점 (가장 왼쪽 구석 상단) 에서 시작한 다음 행 우선 순회 시작
3. 첫 번째 행에서 끝까지 다 갔으면 열 우선 순회로 변경
4. 맨 오른쪽 열 맨 아래까지 다 내려갔다면 또 행 우선 순회로 변경
5. 이 과정을 더 이상 반복할 수 없을 때 까지 진행
6. 이렇기 때문에 방향 벡터를 쓰면 더 깔끔하게 해결 되기는 함 
'''


# 달팽이 숫자 (SWEA 1954)


T = int(input())

for tc in range(1, T+1):
  N = int(input())
  snail_box = [[0] * N for _ in range(N)]

  r, c = 0, -1
  fill = 1
  dist = N
  direction = 1

  while dist > 0:
    for _ in range(dist):
      c += direction
      snail_box[r][c] = fill
      fill += 1

    dist -= 1
    if dist == 0: break

    for _ in range(dist):
      r += direction
      snail_box[r][c] = fill
      fill += 1

    direction *= -1

  print(f'#{tc}')
  for row in snail_box:
    print(*(row))
