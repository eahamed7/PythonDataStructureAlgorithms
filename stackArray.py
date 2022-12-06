def isFull(): 
    global top, MAX_SIZE
    if top == MAX_SIZE:
        return True
    return False

def isEmpty (): # 
    global top
    if (top == -1):
        return True
    return False


def push (item):
    global top, s_array

    if isFull():
        print ("stack full")
        return
    top = top+1
    s_array[top] = item

def pop (): # return data from item from top of stack and remove it
    global top, s_array

    if isEmpty():
        print ("stack empty")
        return None
    item = s_array[top]
    top -= 1
    return item

def dump_stack():
    global s_array
    print ('top = ', top, s_array)
   
def initialise_stack():
    global top, MAX_SIZE, s_array

    s_array = ['','','','','']
    top = -1

    MAX_SIZE = len(s_array) - 1 #last possible entry

def print_stack ():
    global top, s_array
    if isEmpty():
        print ("stack empty")
    else:
        print ("top = ", top, "Stack = ", end=" ")
        i = top
        while (i>=0):
            print (s_array[i], end=" ")
            i-=1
        print ("")
    
      
def main():
    initialise_stack()

    while True:

        choice = int(input ("Enter 1 to push stack data, 2 to pop data, 3 to print stack, 4 to dump stack, anything else to quit: "))

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
        elif choice == 4:
            dump_stack()

        else:
            break
        

main()