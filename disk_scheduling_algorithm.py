n = int(input("Enter the number of requests: "))
print("Enter the disk requests (space separated):")
requests = list(map(int, input().split()))

head = int(input("Enter the initial head position: "))
direction = input("Enter the direction Left/Right: ").lower()


# FCFS
fcfs_requests = requests.copy()
movement = 0
position = head

print("\nFCFS DISK SCHEDULING")
print("Order:", position, end="")

for req in fcfs_requests:
    movement += abs(position - req)
    position = req
    print(" ->", position, end="")

fcfs_movement = movement
print("\nTotal Head Movement =", fcfs_movement)


# SSTF
sstf_requests = requests.copy()
position = head
seek_sequence = []
movement = 0

while len(sstf_requests) > 0:

    shortest_distance = float('inf')
    nearest_request = -1

    for request in sstf_requests:
        distance = abs(request - position)

        if distance < shortest_distance:
            shortest_distance = distance
            nearest_request = request

    movement += shortest_distance
    position = nearest_request

    seek_sequence.append(nearest_request)
    sstf_requests.remove(nearest_request)

sstf_movement = movement

print("\nSSTF DISK SCHEDULING")
print("Order:", head, end="")

for request in seek_sequence:
    print(" ->", request, end="")

print("\nTotal Head Movement =", sstf_movement)


# SCAN
scan_requests = requests.copy()
scan_requests.sort()

left = []
right = []

for request in scan_requests:
    if request < head:
        left.append(request)
    elif request > head:
        right.append(request)

seek_sequence = []

if direction == "right":
    seek_sequence = right + left[::-1]
else:
    seek_sequence = left[::-1] + right

current = head
movement = 0

print("\nSCAN DISK SCHEDULING")
print("Order:", current, end="")

for r in seek_sequence:
    movement += abs(current - r)
    current = r
    print(" ->", current, end="")

scan_movement = movement
print("\nTotal Head Movement =", scan_movement)


# COMPARISON
print("\nCOMPARISON")
print("ALGORITHM\t\tTOTAL HEAD MOVEMENT")
print("FCFS\t\t\t", fcfs_movement)
print("SSTF\t\t\t", sstf_movement)
print("SCAN\t\t\t", scan_movement)

minimum = min(fcfs_movement, sstf_movement, scan_movement)

best = []

if fcfs_movement == minimum:
    best.append("FCFS")

if sstf_movement == minimum:
    best.append("SSTF")

if scan_movement == minimum:
    best.append("SCAN")

if len(best) == 1:
    print("\nBetter algorithm =", best[0])
else:
    print("\nBetter algorithms =", " and ".join(best))