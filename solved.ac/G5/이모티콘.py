# 1 개의 입력이 있는 상태
# 복사, 붙여넣기, 하나 지우기 모두 1초 소요
# S개 이모티콘 되는데 최소시간
from collections import deque
import sys
input = sys.stdin.readline


def bfs(emoticons, clipboard, time):
    queue = deque()
    queue.append((emoticons, clipboard, time))
    while queue:
        curr_emo, curr_clip, curr_time = queue.popleft()
        if S_arr[S] != 999999999:
            break
        # 붙여넣기는 해당개수의 이모티콘의 시간이 현재 나보다 클때만 하면 되므로
        if (curr_emo + curr_clip, curr_clip) not in visited and curr_emo + curr_clip <= S * 2:
            S_arr[curr_emo + curr_clip] = curr_time + 1
            visited.append((curr_emo + curr_clip, curr_clip))
            queue.append((curr_emo + curr_clip, curr_clip, curr_time + 1))
        # 클립보드에 복사하기
        if (curr_emo, curr_emo) not in visited:
            visited.append((curr_emo, curr_emo))
            queue.append((curr_emo, curr_emo, curr_time + 1))
        # 지우기
        if (curr_emo-1, curr_clip) not in visited and curr_emo >= 1:
            S_arr[curr_emo-1] = curr_time + 1
            visited.append((curr_emo - 1, curr_clip))
            queue.append((curr_emo-1, curr_clip, curr_time + 1))


S = int(input())
S_arr = [999999999] * (S * 2 + 1)
emoticons = 1
S_arr[emoticons] = 0
clipboard = 0
visited = [(emoticons, clipboard)]
time = 0
bfs(emoticons, clipboard, time)
print(S_arr[S])

