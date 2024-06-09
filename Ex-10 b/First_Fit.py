MAX = 25

def main():
    frag = [0] * MAX
    b = [0] * MAX
    f = [0] * MAX
    bf = [0] * MAX
    ff = [0] * MAX
    
    nb = int(input("Enter the number of blocks: "))
    nf = int(input("Enter the number of files: "))
    
    print("Enter the size of the blocks:-")
    for i in range(1, nb + 1):
        b[i] = int(input(f"Block {i}: "))
    
    print("Enter the size of the files:-")
    for i in range(1, nf + 1):
        f[i] = int(input(f"File {i}: "))
    
    for i in range(1, nf + 1):
        for j in range(1, nb + 1):
            if bf[j] != 1:
                temp = b[j] - f[i]
                if temp >= 0:
                    ff[i] = j
                    break
        frag[i] = temp
        bf[ff[i]] = 1
    
    print("\nFile_no:\tFile_size:\tBlock_no:\tBlock_size\tFragment")
    for i in range(1, nf + 1):
        print(f"{i}\t\t{f[i]}\t\t{ff[i]}\t\t{b[ff[i]]}\t\t{frag[i]}")

if __name__ == "__main__":
    main()
