def lru_page_replacement(size, pages):
    frames = []  # List to store current frames
    page_faults = 0  # Counter for page faults

    for page in pages:
        if page not in frames:
            page_faults += 1
            if len(frames) >= size:
                # Remove the least recently used page
                frames.pop(0)
            frames.append(page)
        else:
            # Move the page to the end to mark it as recently used
            frames.remove(page)
            frames.append(page)
        print(f"Current Frames State: {frames}")

    # Display the total number of page faults
    print(f"Total Page Faults: {page_faults}")

# Input the number of frames
size = int(input("Enter the number of frames: "))

# Input the number of pages
num_pages = int(input("Enter the number of pages: "))

# Input the pages
pages = []
print("Enter the pages:")
for _ in range(num_pages):
    pages.append(int(input()))

# Start the LRU page replacement process
print("Starting LRU Page Replacement Process...\n")
lru_page_replacement(size, pages)
