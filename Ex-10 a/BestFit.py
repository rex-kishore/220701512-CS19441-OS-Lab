def best_fit(block_size, m, process_size, n):
    allocation = [-1] * n
    
    for i in range(n):
        best_idx = -1
        for j in range(m):
            if block_size[j] >= process_size[i]:
                if best_idx == -1:
                    best_idx = j
                elif block_size[best_idx] > block_size[j]:
                    best_idx = j
        
        if best_idx != -1:
            allocation[i] = best_idx
            block_size[best_idx] -= process_size[i]
    
    print("\nProcess No.\tProcess Size\tBlock no.")
    for i in range(n):
        print(f"{i + 1}\t\t{process_size[i]}", end='')
        if allocation[i] != -1:
            print(f"\t\t{allocation[i] + 1}")
        else:
            print("\t\tNot Allocated")

if __name__ == "__main__":
    block_size = [100, 500, 200, 300, 600]
    process_size = [212, 417, 112, 426]
    m = len(block_size)
    n = len(process_size)
    best_fit(block_size, m, process_size, n)
