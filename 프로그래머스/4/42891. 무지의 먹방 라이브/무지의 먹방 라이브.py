import heapq

def solution(food_times, k):

    if sum(food_times) <= k:
        return -1
    
    
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))
        
    sum_value = 0
    previous = 0 
    n = len(food_times)
    
    while sum_value + ((q[0][0] - previous)* n) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * n
        n -= 1
        previous = now
        
    result = sorted(q, key = lambda x : x[1])
    return result[(k - sum_value) % n][1]