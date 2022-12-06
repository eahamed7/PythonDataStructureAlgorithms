def initialise_queue():
    global front, rear, size, MAX_SIZE, q_array

    MAX_SIZE = 6

    q_array = [''] * MAX_SIZE
    front = 0
    rear = -1
    size = 0

def enqueue (new_name):
    global rear, size, q_array

    if isFull():
        print ("Queue full")
        return
    rear = (rear + 1) % MAX_SIZE
    q_array[rear] = new_name
    size += 1


def dequeue (): # return data from item from top of queue and remove it
    global front, size, q_array

    if isEmpty():
        return None
    item = q_array[front]
    front = (front  + 1) % MAX_SIZE
    size -= 1
    return item

def isEmpty (): # 
    global size
    if (size == 0):
        return True
    return False

def isFull(): 
    global size, MAX_SIZE
    if size == MAX_SIZE:
        return True
    return False

def dump_queue():
    global q_array
    print ('front = ', front, 'rear = ', rear, q_array)

def print_queue_items():
    if isEmpty():
        print("Queue Empty")
    else:
        print("Queue: ", end="")
        p=front
        while p != rear:
            print (q_array[p], end =" ")
            p=(p  + 1) % MAX_SIZE
        print (q_array[rear])
   
     
def main():
    initialise_queue()

    while True:

        choice = int(input ("Enter 1 to enqueue data, 2 to dequeue data, anything else to quit: "))

        if choice==1:
            data_for_q=input("Enter order item for queue: ")

            while data_for_q!="":
                enqueue(data_for_q)
                data_for_q=input("Enter order item for queue: ")

            dump_queue()
            print_queue_items()
        elif choice == 2:

            ans=(input("Enter y to dequeue an item: ")).upper()

            while ans=="Y":
                item = dequeue()
                print ("Item from queue: ",item)
                ans=(input("Enter y to dequeue an item: ")).upper()
            dump_queue()
            print_queue_items()
        else:
            break
        

main()