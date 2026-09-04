process_list = []

n = int(input("Enter the number of processes: "))

print("Enter the Processes: PID AT BT PR")

for i in range(n):
    process_id, arrival_time, burst_time, priority = input().split()
    process_list.append(
        (process_id, int(arrival_time), int(burst_time), int(priority))
    )


current_time = 0
completed = 0
done = [False] * n
results = []

while completed < n:

    selected = -1
    highest_priority = float('inf')

    for i in range(n):

        process_id, arrival_time, burst_time, priority = process_list[i]

        if not done[i] and arrival_time <= current_time:

            if priority < highest_priority:
                highest_priority = priority
                selected = i

            elif priority == highest_priority:

                if selected == -1 or arrival_time < process_list[selected][1]:
                    selected = i

    if selected == -1:
        current_time += 1
        continue

    process_id, arrival_time, burst_time, priority = process_list[selected]

    completion_time = current_time + burst_time
    turnaround_time = completion_time - arrival_time
    waiting_time = turnaround_time - burst_time

    current_time = completion_time
    done[selected] = True
    completed += 1

    results.append(
        (
            process_id,
            arrival_time,
            burst_time,
            priority,
            completion_time,
            turnaround_time,
            waiting_time
        )
    )


total_wt = 0
total_tat = 0

print("\nNON PREEMPTIVE")
print("PID\tAT\tBT\tPR\tCT\tTAT\tWT")

for process_id, arrival_time, burst_time, priority, ct, tat, wt in results:

    print(
        f"{process_id}\t{arrival_time}\t{burst_time}\t"
        f"{priority}\t{ct}\t{tat}\t{wt}"
    )

    total_wt += wt
    total_tat += tat

np_avg_wt = total_wt / n
np_avg_tat = total_tat / n

print(f"Average waiting time = {np_avg_wt:.2f}")
print(f"Average turnaround time = {np_avg_tat:.2f}")


current_time = 0
completed_count = 0

remaining_time = [
    burst_time
    for process_id, arrival_time, burst_time, priority in process_list
]

completion_time = [0] * n
turnaround_time = [0] * n
waiting_time = [0] * n

while completed_count < n:

    selected_index = -1

    for i in range(n):

        process_id, arrival_time, burst_time, priority = process_list[i]

        if arrival_time <= current_time and remaining_time[i] > 0:

            if selected_index == -1:
                selected_index = i

            else:

                selected_pid, selected_arrival, selected_burst, selected_priority = process_list[selected_index]

                if priority < selected_priority:
                    selected_index = i

                elif priority == selected_priority:

                    if arrival_time < selected_arrival:
                        selected_index = i

    if selected_index == -1:
        current_time += 1
        continue

    remaining_time[selected_index] -= 1
    current_time += 1

    if remaining_time[selected_index] == 0:

        process_id, arrival_time, burst_time, priority = process_list[selected_index]

        completion_time[selected_index] = current_time
        turnaround_time[selected_index] = current_time - arrival_time
        waiting_time[selected_index] = turnaround_time[selected_index] - burst_time

        completed_count += 1


total_wt = 0
total_tat = 0

print("\nPREEMPTIVE")
print("PID\tAT\tBT\tPR\tCT\tTAT\tWT")

for i in range(n):

    process_id, arrival_time, burst_time, priority = process_list[i]

    print(
        f"{process_id}\t{arrival_time}\t{burst_time}\t"
        f"{priority}\t{completion_time[i]}\t"
        f"{turnaround_time[i]}\t{waiting_time[i]}"
    )

    total_wt += waiting_time[i]
    total_tat += turnaround_time[i]

p_avg_wt = total_wt / n
p_avg_tat = total_tat / n

print(f"Average waiting time = {p_avg_wt:.2f}")
print(f"Average turnaround time = {p_avg_tat:.2f}")


print("\nCOMPARISON")
print("METRIC\t\t\tNON PREEMPTIVE\tPREEMPTIVE")
print(f"Average waiting time\t{np_avg_wt:.2f}\t\t{p_avg_wt:.2f}")
print(f"Average turnaround time\t{np_avg_tat:.2f}\t\t{p_avg_tat:.2f}")


if p_avg_wt < np_avg_wt:
    print(
        f"\nPreemptive has lower average waiting time by "
        f"{np_avg_wt - p_avg_wt:.2f}"
    )
elif np_avg_wt < p_avg_wt:
    print(
        f"\nNon preemptive has lower average waiting time by "
        f"{p_avg_wt - np_avg_wt:.2f}"
    )
else:
    print("\nBoth have the same average waiting time")


if p_avg_tat < np_avg_tat:
    print(
        f"Preemptive has lower average turnaround time by "
        f"{np_avg_tat - p_avg_tat:.2f}"
    )
elif np_avg_tat < p_avg_tat:
    print(
        f"Non preemptive has lower average turnaround time by "
        f"{p_avg_tat - np_avg_tat:.2f}"
    )
else:
    print("Both have the same average turnaround time")


if p_avg_wt < np_avg_wt and p_avg_tat < np_avg_tat:
    print("Better algorithm = PREEMPTIVE")
elif np_avg_wt < p_avg_wt and np_avg_tat < p_avg_tat:
    print("Better algorithm = NON PREEMPTIVE")
else:
    print("Better algorithm = depends on which metric is prioritized")