n = int(input("Enter Total Number of Processes: "))
x = n
arrival = []
burst = []
temp = []
wait = 0
turnaround = 0
avg_wait = 0
avg_turnaround = 0
total = 0
counter = 0
quantum = 0

for i in range(n):
    print("Enter Details of Process[{}]".format(i + 1))
    arrival.append(int(input("Arrival Time: ")))
    burst.append(int(input("Burst Time: ")))
    temp.append(burst[i])

quantum = int(input("Enter Time Quantum: "))
print("\nProcess ID\tBurst Time\tTurnaround Time\tWaiting Time")

while x != 0:
    for i in range(n):
        if temp[i] <= quantum and temp[i] > 0:
            total += temp[i]
            temp[i] = 0
            counter = 1
        elif temp[i] > 0:
            temp[i] -= quantum
            total += quantum

        if temp[i] == 0 and counter == 1:
            x -= 1
            print("Process[{}]\t\t{}\t\t{}\t\t{}".format(i + 1, burst[i], total - arrival[i], total - arrival[i] - burst[i]))
            wait += total - arrival[i] - burst[i]
            turnaround += total - arrival[i]
            counter = 0

        if i == n - 1:
            i = 0
        elif arrival[i + 1] <= total:
            i += 1
        else:
            i = 0

avg_wait = wait * 1.0 / n
avg_turnaround = turnaround * 1.0 / n
print("\nAverage Waiting Time:", avg_wait)
print("Average Turnaround Time:", avg_turnaround)
