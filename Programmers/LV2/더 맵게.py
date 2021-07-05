# 가쟁 맵지 않은 + 2번째로 맵지 않은 * 2 = 새로운 음식
import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:
        if len(scoville) == 1 and scoville[0] < K:
            answer = -1
            break
        else:
            if scoville[0] >= K:
                break
            else:
                a = heapq.heappop(scoville)
                b = heapq.heappop(scoville)
                heapq.heappush(scoville, (a + b * 2))
                answer += 1
    return answer

# print(solution([1, 2, 3, 9, 10, 12], 7))