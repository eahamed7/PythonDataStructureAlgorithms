class StackItem:
    def __init__ (self, data_stored):  #creates new StackItem with data and next being None
        self.data_stored = data_stored
        self.next = None
        
def isFull(): # this tyoe of stack doesn't get full
    return False

def isEmpty (): # empty if top doesn't point to anything
    if (top is None):
        return True
    return False


def push (new_name):
    global top

    if isEmpty(): # stack was empty
        top= StackItem(new_name)
    else: # add to top of stack
        old_top = top
        top = StackItem(new_name)
        top.next = old_top

def pop (): # return data from item from top of stack and remove it
    global top

    if isEmpty():
        return None
    item = top.data_stored #get data from first item
    top=top.next

    return item


def print_stack():

    global top
    p=top
    if isEmpty(): # stack is empty
        print ("Empty stack")
        return
    print ("Stack Contents: ")
    #Go through q till find rear
    while not (p is None):
        print(p.data_stored, end=" ") # print data in stack
        p = p.next # move to next item
    print("")
        
    
def initialise_stack():
    global top
   
    top = None
        
      
def main():
    initialise_stack()

    while True:

        choice = int(input ("Enter 1 to push stack data, 2 to pop data, 3 to print stack, anything else to quit: "))

        if choice==1:
            data_for_s=input("Enter item for stack: ")
            while data_for_s!="":
                push(data_for_s)
                data_for_s=input("Enter item for stack: ")
        elif choice == 2:
            item = pop()
            print (item, "popped")
        elif choice == 3:
            print_stack()
        else:
            break
        
main()