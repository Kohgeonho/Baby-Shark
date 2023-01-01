monitor=True

def input_list():
    return [int(i) for i in input().split()]

N = int(input())
W = []
for _ in range(N):
    W.append(input_list())

from time import sleep

def show(board=W, t=1, opt="", emph=[]):
    string = opt + "\n"
    for i in range(N):
        for j in range(N):
            if board[i][j] == 9:
                string += f"\033[33m{board[i][j]}\033[0m "
            elif board[i][j] == 0:
                string += ". "
            else:
                string += str(board[i][j]) + " "
        string += "\n"
    string += "\n"
    print(string)
    sleep(t)

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
    queue = [(0, i, j, [])]
    visited[i][j] = True

    while len(queue) > 0:
        dist, _i, _j, path = min(queue)
        queue.remove((dist, _i, _j, path))

        if W[_i][_j] == weight or W[_i][_j] == 0 or W[_i][_j] == 9:
            if _i > 0 and not visited[_i-1][_j]:
                queue.append((dist+1, _i-1, _j, path + [(_i, _j)]))
                visited[_i-1][_j] = True
            if _j > 0 and not visited[_i][_j-1]:
                queue.append((dist+1, _i, _j-1, path + [(_i, _j)]))
                visited[_i][_j-1] = True
            if _j < N-1 and not visited[_i][_j+1]:
                queue.append((dist+1, _i, _j+1, path + [(_i, _j)]))
                visited[_i][_j+1] = True
            if _i < N-1 and not visited[_i+1][_j]:
                queue.append((dist+1, _i+1, _j, path + [(_i, _j)]))
                visited[_i+1][_j] = True
        elif W[_i][_j] < weight:
            return dist, _i, _j, path

    return (0, -1, -1, [])

while True:
    weight, exp, i, j = baby_shark
    dist, fish_i, fish_j, path = find(weight, i, j)

    if fish_i < 0:
        break

    if monitor:
        W[i][j] = 0
        for n, (_i, _j) in enumerate(path):
            temp = W[_i][_j]
            W[_i][_j] = 9
            show(W, t=0.1, opt=f"Lv: {weight}({exp}/{weight}), time: {time + n}s")
            W[_i][_j] = temp

    time += dist
    exp += 1
    if exp >= weight:
        weight += 1
        exp = 0
    W[fish_i][fish_j] = 9
    W[i][j] = 0
    baby_shark = (weight, exp, fish_i, fish_j)
    if monitor:
        show(opt=f"Lv: {weight}({exp}/{weight}), time: {time}s")

# print(time)
    
