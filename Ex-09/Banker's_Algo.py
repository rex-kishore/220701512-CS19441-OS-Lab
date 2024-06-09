def main():
    n = 5  # Number of processes
    m = 3  # Number of resources

    # Allocation Matrix: Resources currently allocated to each process
    alloc = [[0, 1, 0],
             [2, 0, 0],
             [3, 0, 2],
             [2, 1, 1],
             [0, 0, 2]]

    # MAX Matrix: Maximum demand of each process
    max = [[7, 5, 3],
           [3, 2, 2],
           [9, 0, 2],
           [2, 2, 2],
           [4, 3, 3]]

    # Available Resources: Total resources available initially
    avail = [3, 3, 2]

    # Flag array to indicate if a process is finished
    f = [0] * n

    # List to store the safe sequence
    ans = []

    # Need Matrix: Remaining resources needed by each process
    need = [[0] * m for _ in range(n)]

    # Calculate the Need Matrix
    for i in range(n):
        for j in range(m):
            need[i][j] = max[i][j] - alloc[i][j]

    # Banker's algorithm to find the safe sequence
    for k in range(n):  # Check for all processes
        for i in range(n):  # Go through all processes
            if f[i] == 0:  # If the process is not finished
                flag = 0  # Assume the process can be completed
                for j in range(m):
                    if need[i][j] > avail[j]:  # If resources needed are more than available
                        flag = 1  # Process cannot be completed
                        break

                if flag == 0:  # If the process can be completed
                    ans.append(i)  # Add this process to the safe sequence
                    for y in range(m):
                        avail[y] += alloc[i][y]  # Release the resources allocated to this process
                    f[i] = 1  # Mark this process as finished

    # Print the safe sequence
    print("The SAFE Sequence is")
    print(" -> ".join(["P{}".format(p) for p in ans]))

if __name__ == "__main__":
    main()
