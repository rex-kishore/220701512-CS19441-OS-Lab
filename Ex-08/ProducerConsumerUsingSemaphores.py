from threading import Thread, Lock
import time
import sys

# Define global variables
mutex = Lock()  # Mutex lock to ensure thread safety
full = 0  # Number of items in the buffer
empty = 3  # Number of empty slots in the buffer
x = 0  # Placeholder for the item being produced/consumed

# Producer function
def producer():
    global mutex, full, empty, x
    mutex.acquire()  # Acquire the mutex lock to ensure exclusive access to shared variables
    if full < 3:  # Check if the buffer is not full
        full += 1  # Increment the number of items in the buffer
        empty -= 1  # Decrement the number of empty slots in the buffer
        x += 1  # Increment the placeholder for the item
        print(f"Producer produces the item {x}")  # Print the produced item
    else:
        print("Buffer is full!!")  # If the buffer is full, print a message
    mutex.release()  # Release the mutex lock

# Consumer function
def consumer():
    global mutex, full, empty, x
    mutex.acquire()  # Acquire the mutex lock
    if full > 0:  # Check if the buffer is not empty
        full -= 1  # Decrement the number of items in the buffer
        empty += 1  # Increment the number of empty slots in the buffer
        print(f"Consumer consumes item {x}")  # Print the consumed item
        x -= 1  # Decrement the placeholder for the item
    else:
        print("Buffer is empty!!")  # If the buffer is empty, print a message
    mutex.release()  # Release the mutex lock

# Main function
def main():
    while True:
        # Present menu options to the user
        print("\n1.Producer\n2.Consumer\n3.Exit")
        sys.stdout.flush()  # Flush the output buffer to ensure immediate display
        choice = int(input("Enter your choice: "))  # Get user's choice
        if choice == 1:  # If the user chooses to produce
            producer_thread = Thread(target=producer)  # Create a thread for the producer function
            producer_thread.start()  # Start the producer thread
            producer_thread.join()  # Wait for the producer thread to complete
        elif choice == 2:  # If the user chooses to consume
            consumer_thread = Thread(target=consumer)  # Create a thread for the consumer function
            consumer_thread.start()  # Start the consumer thread
            consumer_thread.join()  # Wait for the consumer thread to complete
        elif choice == 3:  # If the user chooses to exit
            break  # Exit the loop and end the program
        else:  # If the user enters an invalid choice
            print("Invalid choice!")  # Print a message indicating an invalid choice

# Check if the script is being run directly
if __name__ == "__main__":
    main()  # Call the main function to start the program
