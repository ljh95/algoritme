from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    wnum = 0
    bridge_sum = 0
    bridge = deque([0] * bridge_length)
    while wnum < len(truck_weights):
        time+=1
        bridge_sum -= bridge.popleft()
        if (bridge_sum + truck_weights[wnum]) <= weight:
            bridge.append(truck_weights[wnum])
            bridge_sum+= truck_weights[wnum]
            wnum+=1
        else:
            bridge.append(0)

    return time + bridge_length

bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]
print(solution(bridge_length, weight, truck_weights))