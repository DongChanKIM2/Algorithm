# 테스트케이스 개수
t = int(input())
for tc in range(t):
    # 먼저 시작하는 사람
    person = input()
    # 주사위 a, b 각각
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    # a, b 위치
    a_idx = 0
    b_idx = 0
    # 먼저 도착한 사람 or 무승부 가리는 answer 변수 설정
    answer = 0
    for i in range(10):
        # A가 먼저 던지면
        if person == 'A':
            a_idx += a[i]
            # 바뀐 A가 19이상이면 GAME OVER
            if a_idx >= 19:
                answer = 'A'
                break
            # A와 B가 같으면 A가 움직인 상황이므로 B가 0
            if a_idx == b_idx:
                b_idx = 0
            # A와 B가 다르면 B를 움직이고 위의 과정을 반복함
            else:
                b_idx += b[i]
                if b_idx >= 19:
                    answer = 'B'
                    break
                if a_idx == b_idx:
                    a_idx = 0
        # B가 먼저 던지면
        elif person == 'B':
            b_idx += b[i]
            # B가 19이상이면 GAME OVER
            if b_idx >= 19:
                answer = 'B'
                break
            # B가 움직인 상황이므로 A가 0으로 바뀜
            if a_idx == b_idx:
                a_idx = 0
            # A, B가 다르면 A가 움직일 차례
            else:
                a_idx += a[i]
                # 위의 과정을 동일하게 수행
                if a_idx >= 19:
                    answer = 'A'
                    break
                if a_idx == b_idx:
                    b_idx = 0

    # 무승부일때
    if a_idx < 19 and b_idx < 19:
        answer = 'AB'
    print('#{} {}'.format(tc+1, answer))
