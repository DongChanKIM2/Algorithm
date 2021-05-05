def solution(numbers, hand):
    ans = ''
    left_x, left_y = 3, 0
    right_x, right_y = 3, 2

    for i in range(0, len(numbers)):
        # 왼쪽열 숫자 처리
        if numbers[i] == 1:
            ans += 'L'
            left_x, left_y = 0, 0
        elif numbers[i] == 4:
            ans += 'L'
            left_x, left_y = 1, 0
        elif numbers[i] == 7:
            ans += 'L'
            left_x, left_y = 2, 0

        # 오른쪽열 숫자 처리
        elif numbers[i] == 3:
            ans += 'R'
            right_x, right_y = 0, 2
        elif numbers[i] == 6:
            ans += 'R'
            right_x, right_y = 1, 2
        elif numbers[i] == 9:
            ans += 'R'
            right_x, right_y = 2, 2

        # 가운데 열 처리 해주자
        elif numbers[i] == 2:
            left_distance = abs(0-left_x) + abs(1-left_y)
            right_distance = abs(0-right_x) + abs(1-right_y)
            # 왼손이 오른손보다 거리가 더 멀면 오른손사용
            if left_distance > right_distance:
                ans += 'R'
                right_x, right_y = 0, 1
            # 오른손이 왼손보다 더 멀면 왼손사용
            elif left_distance < right_distance:
                ans += 'L'
                left_x, left_y = 0, 1
            # 같으면 손잡이에 따라 분류해주자
            elif left_distance == right_distance:
                if hand == 'right':
                    ans += 'R'
                    right_x, right_y = 0, 1
                elif hand == 'left':
                    ans += 'L'
                    left_x, left_y = 0, 1

        elif numbers[i] == 5:
            left_distance = abs(1-left_x) + abs(1-left_y)
            right_distance = abs(1-right_x) + abs(1-right_y)
            # 왼손이 오른손보다 거리가 더 멀면 오른손사용
            if left_distance > right_distance:
                ans += 'R'
                right_x, right_y = 1, 1
            # 오른손이 왼손보다 더 멀면 왼손사용
            elif left_distance < right_distance:
                ans += 'L'
                left_x, left_y = 1, 1
            # 같으면 손잡이에 따라 분류해주자
            elif left_distance == right_distance:
                if hand == 'right':
                    ans += 'R'
                    right_x, right_y = 1, 1
                elif hand == 'left':
                    ans += 'L'
                    left_x, left_y = 1, 1

        elif numbers[i] == 8:
            left_distance = abs(2-left_x) + abs(1-left_y)
            right_distance = abs(2-right_x) + abs(1-right_y)
            # 왼손이 오른손보다 거리가 더 멀면 오른손사용
            if left_distance > right_distance:
                ans += 'R'
                right_x, right_y = 2, 1
            # 오른손이 왼손보다 더 멀면 왼손사용
            elif left_distance < right_distance:
                ans += 'L'
                left_x, left_y = 2, 1
            # 같으면 손잡이에 따라 분류해주자
            elif left_distance == right_distance:
                if hand == 'right':
                    ans += 'R'
                    right_x, right_y = 2, 1
                elif hand == 'left':
                    ans += 'L'
                    left_x, left_y = 2, 1

        elif numbers[i] == 0:
            left_distance = abs(3-left_x) + abs(1-left_y)
            right_distance = abs(3-right_x) + abs(1-right_y)
            # 왼손이 오른손보다 거리가 더 멀면 오른손사용
            if left_distance > right_distance:
                ans += 'R'
                right_x, right_y = 3, 1
            # 오른손이 왼손보다 더 멀면 왼손사용
            elif left_distance < right_distance:
                ans += 'L'
                left_x, left_y = 3, 1
            # 같으면 손잡이에 따라 분류해주자
            elif left_distance == right_distance:
                if hand == 'right':
                    ans += 'R'
                    right_x, right_y = 3, 1
                elif hand == 'left':
                    ans += 'L'
                    left_x, left_y = 3, 1
    return ans



# numbers = list(map(int, input().split()))
# hand = input()
# print(solution(numbers, hand))

