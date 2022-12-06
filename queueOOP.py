class QueueItem:
    def __init__ (self, data_stored):  #creates new QueueItem with data and next being None
        self.data_stored = data_stored
        self.next = None
        
def initialise_queue():
    global front, rear
   
    front = None
    rear = None

def enqueue (new_name):
    global front
    global rear

    if isEmpty(): # q was empty
        front= QueueItem(new_name)
        rear = front
    else: # add to rear of queue
        rear.next = QueueItem(new_name)
        rear = rear.next

def dequeue (): # return data from item from top of queue and remove it
    global front
    global rear

    if isEmpty():
        return None
    item = front.data_stored #get data from first item
    front=front.next
    if isEmpty():
        rear = None
    return item

def isFull(): # this tyoe of queue doesn't get full
    return False

def isEmpty (): # empty if front doesn't point to anything
    if (front is None):
        return True
    return False

def print_queue():
    if isEmpty():
        print("Queue Empty")
    else:
        print("Queue: ", end="")
        p=front
        while p != rear:
            print (p.data_stored, end =" ")
            p=p.next
        print (rear.data_stored)

def count_queue():
    if isEmpty():
        return 0
    else:
        count=1
        p=front
        while p != rear:
            p=p.next
            count+=1
        return count
      
def main():
    initialise_queue()

    data_for_q=input("Enter order item for queue: ")

    while data_for_q!="":
        enqueue(data_for_q)
        data_for_q=input("Enter order item for queue: ")

    print_queue()

    ans=(input("Enter y to take an order item off the queue: ")).upper()

    while ans=="Y":
        item = dequeue()
        print (item)
        ans=(input("Enter y to take an order item off the queue: ")).upper()
    print_queue()
main()