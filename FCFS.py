# ---- Input ----
n = int(input("Number of processes: "))
processes = []

for i in range(n):
    at = int(input(f"Process {i+1} - Arrival Time: "))
    bt = int(input(f"Process {i+1} - Burst Time: "))
    processes.append([i + 1, at, bt])   # [Process No, AT, BT]

# ---- Sort (Arrival Time অনুযায়ী) ----
processes.sort(key=lambda x: x[1])

# ---- Time Calculation ----
current_time = 0
completion_time = []
turnaround_time = []
waiting_time = []

for pno, at, bt in processes:
    if current_time < at:
        current_time = at
    current_time += bt
    ct = current_time
    tat = ct - at
    wt = tat - bt

    completion_time.append(ct)
    turnaround_time.append(tat)
    waiting_time.append(wt)

# ---- Result ----
for i, (pno, at, bt) in enumerate(processes):
    print(f"P{pno}: AT={at}, BT={bt}, CT={completion_time[i]}, TAT={turnaround_time[i]}, WT={waiting_time[i]}")

# ---- Average TAT & WT ----
avg_tat = sum(turnaround_time) / n
avg_wt = sum(waiting_time) / n

print(f"\nAverage Turnaround Time: {avg_tat:.2f}")
print(f"Average Waiting Time: {avg_wt:.2f}")