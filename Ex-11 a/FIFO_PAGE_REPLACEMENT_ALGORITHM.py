class Page:
    def __init__(self, page_num):
        self.page_num = page_num

def fifo(page_frames, pages, num_frames):
    page_queue = []  # Queue to store page numbers in memory
    page_faults = 0
    for page in pages:
        if page.page_num not in page_frames:
            page_faults += 1
            if len(page_frames) == num_frames:
                # Remove the oldest page from memory (FIFO)
                oldest_page = page_queue.pop(0)
                page_frames.remove(oldest_page)
            page_frames.append(page.page_num)
            page_queue.append(page.page_num)  # Add the new page to the queue
    return page_faults

def main():
    num_frames = int(input("Enter the number of page frames: "))
    ref_string_size = int(input("Enter the size of the reference string: "))
    ref_string = []
    for i in range(ref_string_size):
        page_num = int(input("Enter page number {}: ".format(i+1)))
        ref_string.append(Page(page_num))  # Create Page objects and add them to the list

    page_frames = []
    page_faults = fifo(page_frames, ref_string, num_frames)

    print("Total page faults using FIFO:", page_faults)

if __name__ == "__main__":
    main()
