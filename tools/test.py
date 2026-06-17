
from typing import List

def exclusiveTime(n: int, logs: List[str]) -> List[int]:
    exclusive_times = [0] * n
    call_stack = []

    for log in logs:
        log_id, action, time = log.split(":")
        log_id, time = int(log_id), int(time)

        if action == "start":
            if call_stack:
                previous_function = call_stack[-1]
                previous_function[2] += time-previous_function[1]
            call_stack.append([log_id, time, 0])

        else: # if action is "end", previous log should be the start of the same function
            previous_function = call_stack.pop()
            previous_function[2] += time-previous_function[1]
            exclusive_times[log_id] += previous_function[2]+1

            if call_stack:
                call_stack[-1][1] = time+1

    return exclusive_times


n = 2
logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]

print(exclusiveTime(n, logs))