# 힙 정렬 문제
# 만약 현재 대기하고 있는 친구들이 많으면 종료시간이 빠른 친구를 먼저 처리해야 평균시간 감소
# 먼저들어온 친구가 있다면 뒤에 들어오는 애들 고려하지 않고 바로 처리하는 문제조건

import heapq

def solution(jobs):
    heap = []
    # 현재 시간(초), delay 계산 sum값, 처리한 작업의 수
    now, delay, done, cnt = 0, 0, 0, len(jobs)
    temp = []
    # jobs의 개수만큼 일을 할때 까지 진행
    while done < cnt:

        for job in jobs:
            if job[0] <= now and job not in temp:

                heapq.heappush(heap, [job[1], job[0]])
                temp.append(job)

        if heap:
            curr = heapq.heappop(heap)
            done += 1
            delay += (now - curr[1] + curr[0])
            now += curr[0]
        else:
            now += 1
        
    return delay // done

# solution([[0, 3], [1, 9], [2, 6]])