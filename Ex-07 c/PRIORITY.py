n = int(input("Enter Number of Processes: "))
bt = []
pr = []
p = []

for i in range(n):
    print("\nProcess [{}]\n".format(i+1))
    bt.append(int(input("Burst Time: ")))
    pr.append(int(input("Priority: ")))
    p.append(i + 1)

# Sorting burst time, priority, and process number in ascending order using selection sort
for i in range(n):
    pos = i
    for j in range(i+1, n):
        if pr[j] < pr[pos]:
            pos = j
    pr[i], pr[pos] = pr[pos], pr[i]
    bt[i], bt[pos] = bt[pos], bt[i]
    p[i], p[pos] = p[pos], p[i]

wt = [0] * n
total = 0

# Calculate waiting time
for i in range(1, n):
    for j in range(i):
        wt[i] += bt[j]
    total += wt[i]

avg_wt = total / n  # Average waiting time
total = 0

print("\nProcess\t Burst Time \tWaiting Time\tTurnaround Time")
for i in range(n):
    tat = bt[i] + wt[i]  # Calculate turnaround time
    total += tat
    print("P[{}]\t\t {}\t\t {}\t\t\t{}".format(p[i], bt[i], wt[i], tat))

avg_tat = total / n  # Average turnaround time

print("\nAvg Waiting Time =", avg_wt)
print("Avg Turnaround Time =", avg_tat)
