'''숫자 카드 문제 (SWEA 4834 번)'''

T = int(input())

for tc in range(1, T+1):                                
    N = int(input())                       # 카드 개수 N
    cards = list(map(int, input()))        # 스플릿 없이 N 만큼의 카드 리스트 입력
    count = [0] * 10                       # 카드의 숫자 별 인덱스 길이 만큼의 리스트 (0부터 9까지)

    for card in cards:
        count[card] += 1                   # 카운트의 card 인덱스 위치에 카드 번호 있을 시 카운팅 해서 추가

    max_count = max(count)                 # 카드 숫자별 카운팅 하는 리스트에서 max 값 찾은 후 지정
    max_card = 0                           # 최고 빈도수 카드는 일단 임시로 0으로 지정

    for i in range(9, -1, -1):             # 리스트를 거꾸로 뒤집어서 되돌아 보며 최빈 및 최대를 만족하는 카드 찾기
        if count[i] == max_count:          # 리스트 기본 순서가 0부터 9로 되어있기 때문에 각각의 빈도가 전부 1이거나 동일할 경우 최댓값을 출력해야 하기 때문
            max_card = i
            break                          # break를 사용해 처음 max_card를 찾으면 바로 조건문 종료(반복 방지)

    print(f'#{tc} {max_card} {max_count}')