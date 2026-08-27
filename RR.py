processes = []

n = int(input("Enter the number of processes: "))

print("Enter the processes PID AT BT")

for i in range(n):
    pid, at, bt = input().split()
    processes.append((pid, int(at), int(bt)))

quantum = int(input("Enter the time quantum: "))

order = sorted(range(n), key=lambda x: processes[x][1])

remaining = [bt for pid, at, bt in processes]

ct = [0] * n
tat = [0] * n
wt = [0] * n

current_time = 0
completed = 0
queue = []

while completed < n:

    while order and processes[order[0]][1] <= current_time:
        queue.append(order.pop(0))

    if not queue:
        current_time += 1
        continue

    index = queue.pop(0)

    execution_time = min(quantum, remaining[index])

    remaining[index] -= execution_time
    current_time += execution_time

    while order and processes[order[0]][1] <= current_time:
        queue.append(order.pop(0))

    if remaining[index] > 0:
        queue.append(index)

    else:
        pid, at, bt = processes[index]

        ct[index] = current_time
        tat[index] = ct[index] - at
        wt[index] = tat[index] - bt

        completed += 1

total_wt = sum(wt)
total_tat = sum(tat)

print("\nROUND ROBIN")
print("PID\tAT\tBT\tCT\tTAT\tWT")

for i in range(n):
    pid, at, bt = processes[i]

    print(f"{pid}\t{at}\t{bt}\t{ct[i]}\t{tat[i]}\t{wt[i]}")

print(f"\nAverage Waiting Time = {total_wt / n:.2f}")
print(f"Average Turnaround Time = {total_tat / n:.2f}")