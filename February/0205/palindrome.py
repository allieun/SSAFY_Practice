def is_palindrome(string):
    return string == [string::-1]

T = 10

for tc in range(1, T+1):
    N = int(input())
    grid = [list(input()) for _ in range(8)]
    count = 0

    for r in range(8):
        for c in range(8-N+1):
            row_string = ''.join(grid[r][c:c+N])
            if is_palindrome(row_string):
                count += 1

    for c in range(8):
        for r in range(8-N+1):
            column_string = ''
            for dr in range(N):
                column_string += grid[dr+r][c]

            if is_palindrome(column_string):
                count += 1
    print(f'#{tc} {count}')