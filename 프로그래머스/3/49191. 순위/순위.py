def solution(n, results):
    graph = [[0] * (n+1) for _ in range(n+1)]

    # 1. 결과 반영
    for a, b in results:
        graph[a][b] = 1   # a가 b를 이김
        graph[b][a] = -1  # b는 a에게 짐

    # 2. 플로이드 워셜
    for k in range(1, n+1):  
        for i in range(1, n+1):  
            for j in range(1, n+1):
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1
                    graph[j][i] = -1
                if graph[i][k] == -1 and graph[k][j] == -1:
                    graph[i][j] = -1
                    graph[j][i] = 1
    print(graph)
    # 3. 정확한 순위를 알 수 있는 선수 수 세기
    answer = 0
    for i in range(1, n+1):
        cnt = 0
        for j in range(1, n+1):
            if i == j:
                continue
            if graph[i][j] != 0:
                cnt += 1
        if cnt == n - 1:
            answer += 1

    return answer
