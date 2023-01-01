monitor=True

def input_list():
    return [int(i) for i in input().split()]

N = int(input())
W = []
for _ in range(N):
    W.append(input_list())

baby_shark = (2, 0, 0, 0)
time = 0
for i in range(N):
    for j in range(N):
        if W[i][j] == 9:
            baby_shark = (*baby_shark[0:2], i, j)

def find(weight, i, j):
    '''
    conduct BFS with queue
    '''
    visited = []
    for _ in range(N):
        visited.append([False] * N)
    queue = [(0, i, j)]
    visited[i][j] = True

    while len(queue) > 0:
        dist, _i, _j = min(queue)
        queue.remove((dist, _i, _j))

        if W[_i][_j] == weight or W[_i][_j] == 0 or W[_i][_j] == 9:
            if _i > 0 and not visited[_i-1][_j]:
                queue.append((dist+1, _i-1, _j))
                visited[_i-1][_j] = True
            if _j > 0 and not visited[_i][_j-1]:
                queue.append((dist+1, _i, _j-1))
                visited[_i][_j-1] = True
            if _j < N-1 and not visited[_i][_j+1]:
                queue.append((dist+1, _i, _j+1))
                visited[_i][_j+1] = True
            if _i < N-1 and not visited[_i+1][_j]:
                queue.append((dist+1, _i+1, _j))
                visited[_i+1][_j] = True
        elif W[_i][_j] < weight:
            return dist, _i, _j

    return (0, -1, -1)

while True:
    weight, exp, i, j = baby_shark
    dist, fish_i, fish_j = find(weight, i, j)

    if fish_i < 0:
        break

    time += dist
    exp += 1
    if exp >= weight:
        weight += 1
        exp = 0
    W[fish_i][fish_j] = 9
    W[i][j] = 0
    baby_shark = (weight, exp, fish_i, fish_j)

print(time)
    
